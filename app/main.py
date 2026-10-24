"""APP_COM_ESPECIALISTA MVP API."""
import hashlib, hmac, json, os, secrets, sqlite3, time, base64
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from fastapi import FastAPI, Depends, HTTPException, Request, Response, Header
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, Field, field_validator

DB_PATH=os.getenv("CPE_DB_PATH","data/cpe.sqlite3")
JWT_SECRET=os.getenv("CPE_JWT_SECRET","")
JWT_TTL=int(os.getenv("CPE_JWT_TTL_SECONDS","3600"))
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY","")
OPENAI_MODEL=os.getenv("CPE_OPENAI_MODEL","gpt-4.1-mini")
ADMIN_BOOTSTRAP_TOKEN=os.getenv("CPE_ADMIN_BOOTSTRAP_TOKEN","")
MAX_CHARS=8000
RATE_LIMIT=int(os.getenv("CPE_RATE_LIMIT_PER_MINUTE","60"))
bearer=HTTPBearer(auto_error=False)
app=FastAPI(title="APP_COM_ESPECIALISTA API",version="1.0.0")
rate_buckets={}
SPECIALISTS=[
 {"id":"general","version":"1.0.0","name":"Orientador Geral","domain":"general","description":"Clarificação de problemas e orientação geral.","status":"active","limits":["Não substitui aconselhamento profissional em áreas reguladas."]},
 {"id":"software","version":"1.0.0","name":"Especialista de Software","domain":"software","description":"Arquitetura, programação, testes e operações.","status":"active","limits":["Não executa ações externas sem autorização explícita."]},
]
def now(): return datetime.now(timezone.utc).isoformat()
def connect():
 Path(DB_PATH).parent.mkdir(parents=True,exist_ok=True)
 c=sqlite3.connect(DB_PATH,timeout=10); c.row_factory=sqlite3.Row; c.execute("PRAGMA foreign_keys=ON"); return c
@contextmanager
def db():
 c=connect()
 try: yield c; c.commit()
 except Exception: c.rollback(); raise
 finally: c.close()
def init_db():
 with db() as c:
  c.executescript("""
  CREATE TABLE IF NOT EXISTS users(id TEXT PRIMARY KEY,email TEXT UNIQUE NOT NULL,password_hash TEXT NOT NULL,role TEXT NOT NULL DEFAULT 'user',created_at TEXT NOT NULL,disabled INTEGER NOT NULL DEFAULT 0);
  CREATE TABLE IF NOT EXISTS conversations(id TEXT PRIMARY KEY,user_id TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,specialist_id TEXT NOT NULL,specialist_version TEXT NOT NULL,title TEXT NOT NULL,created_at TEXT NOT NULL,updated_at TEXT NOT NULL);
  CREATE TABLE IF NOT EXISTS messages(id TEXT PRIMARY KEY,conversation_id TEXT NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,user_id TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,role TEXT NOT NULL,content TEXT NOT NULL,accepted INTEGER NOT NULL DEFAULT 0,created_at TEXT NOT NULL);
  CREATE TABLE IF NOT EXISTS curated_memory(id TEXT PRIMARY KEY,specialist_id TEXT NOT NULL,source_message_id TEXT NOT NULL,content TEXT NOT NULL,state TEXT NOT NULL DEFAULT 'pending',reviewer_id TEXT,created_at TEXT NOT NULL,reviewed_at TEXT);
  CREATE TABLE IF NOT EXISTS audit(id TEXT PRIMARY KEY,actor_id TEXT,action TEXT NOT NULL,resource_type TEXT NOT NULL,resource_id TEXT,metadata_json TEXT NOT NULL,created_at TEXT NOT NULL);
  CREATE INDEX IF NOT EXISTS idx_conversations_user ON conversations(user_id,updated_at);
  CREATE INDEX IF NOT EXISTS idx_messages_user ON messages(user_id,created_at);
  CREATE INDEX IF NOT EXISTS idx_memory_state ON curated_memory(state,specialist_id);
  """)
@app.on_event("startup")
def startup():
 init_db()
 if len(JWT_SECRET.encode())<32: raise RuntimeError("CPE_JWT_SECRET é obrigatório e deve ter pelo menos 32 bytes.")
def audit(actor,action,typ,rid=None,metadata=None):
 with db() as c: c.execute("INSERT INTO audit VALUES(?,?,?,?,?,?,?)",(secrets.token_hex(16),actor,action,typ,rid,json.dumps(metadata or {},ensure_ascii=False),now()))
def password_hash(pw,salt=None):
 salt=salt or secrets.token_bytes(16); d=hashlib.pbkdf2_hmac("sha256",pw.encode(),salt,310000)
 return salt.hex()+"$"+d.hex()
def verify_password(pw,encoded):
 try:
  s,d=encoded.split("$",1); return hmac.compare_digest(password_hash(pw,bytes.fromhex(s)),encoded)
 except Exception: return False
def b64(b): return base64.urlsafe_b64encode(b).rstrip(b"=").decode()
def token_for(uid,role):
 head=b64(json.dumps({"alg":"HS256","typ":"JWT"},separators=(",",":")).encode())
 payload=b64(json.dumps({"sub":uid,"role":role,"iat":int(time.time()),"exp":int(time.time())+JWT_TTL},separators=(",",":")).encode())
 signed=head+"."+payload; sig=b64(hmac.new(JWT_SECRET.encode(),signed.encode(),hashlib.sha256).digest()); return signed+"."+sig
def claims_for(token):
 try:
  head,payload,sig=token.split("."); expected=b64(hmac.new(JWT_SECRET.encode(),(head+"."+payload).encode(),hashlib.sha256).digest())
  if not hmac.compare_digest(sig,expected): raise ValueError()
  claims=json.loads(base64.urlsafe_b64decode(payload+"="*(-len(payload)%4)))
  if claims["exp"]<=int(time.time()): raise ValueError()
  return claims
 except Exception: raise HTTPException(401,detail={"code":"AUTH_INVALID_TOKEN","message":"Token inválido ou expirado."})
def current_user(creds:HTTPAuthorizationCredentials|None=Depends(bearer)):
 if not creds: raise HTTPException(401,detail={"code":"AUTH_REQUIRED","message":"Autenticação obrigatória."},headers={"WWW-Authenticate":"Bearer"})
 cl=claims_for(creds.credentials)
 with db() as c: u=c.execute("SELECT id,email,role,disabled FROM users WHERE id=?",(cl["sub"],)).fetchone()
 if not u or u["disabled"]: raise HTTPException(401,detail={"code":"AUTH_USER_DISABLED","message":"Conta indisponível."})
 return dict(u)
def admin_user(u=Depends(current_user)):
 if u["role"]!="admin": raise HTTPException(403,detail={"code":"AUTH_FORBIDDEN","message":"Permissão administrativa necessária."})
 return u
@app.post("/api/v1/admin/bootstrap")
def bootstrap_admin(bootstrap_token:str=Header(default="",alias="X-Admin-Bootstrap-Token"),user=Depends(current_user)):
 if not ADMIN_BOOTSTRAP_TOKEN or not hmac.compare_digest(bootstrap_token,ADMIN_BOOTSTRAP_TOKEN):
  raise HTTPException(403,detail={"code":"ADMIN_BOOTSTRAP_DENIED","message":"Bootstrap administrativo inválido ou desativado."})
 with db() as c:
  if c.execute("SELECT 1 FROM users WHERE role='admin' LIMIT 1").fetchone():
   raise HTTPException(409,detail={"code":"ADMIN_ALREADY_EXISTS","message":"Já existe um administrador; bootstrap fechado."})
  c.execute("UPDATE users SET role='admin' WHERE id=?",(user["id"],))
 audit(user["id"],"admin.bootstrap","user",user["id"])
 return {"status":"admin_created","user_id":user["id"],"note":"Obtenha um novo token para refletir o papel atualizado."}
@app.middleware("http")
async def limit_requests(request:Request,call_next):
 rid=request.headers.get("X-Request-ID",secrets.token_hex(12))[:128]
 if request.url.path not in ("/health","/api/v1/health"):
  ip=request.client.host if request.client else "unknown"; ts=time.time()
  recent=[t for t in rate_buckets.get(ip,[]) if ts-t<60]
  if len(recent)>=RATE_LIMIT:
   return Response(json.dumps({"error":{"code":"RATE_LIMITED","message":"Limite de pedidos excedido."},"request_id":rid}),429,media_type="application/json",headers={"Retry-After":"60","X-Request-ID":rid})
  recent.append(ts); rate_buckets[ip]=recent
 response=await call_next(request); response.headers["X-Request-ID"]=rid; response.headers["X-Content-Type-Options"]="nosniff"; response.headers["Cache-Control"]="no-store"; return response
@app.exception_handler(HTTPException)
async def http_error(request,exc):
 detail=exc.detail if isinstance(exc.detail,dict) else {"code":"REQUEST_ERROR","message":str(exc.detail)}
 return Response(json.dumps({"error":detail,"request_id":request.headers.get("X-Request-ID")},ensure_ascii=False),exc.status_code,media_type="application/json",headers=exc.headers)
class RegisterIn(BaseModel):
 email:str=Field(min_length=5,max_length=254); password:str=Field(min_length=12,max_length=128)
 @field_validator("email")
 @classmethod
 def normalize(cls,v):
  v=v.strip().lower()
  if "@" not in v or v.startswith("@") or v.endswith("@"): raise ValueError("email inválido")
  return v
class LoginIn(BaseModel): email:str; password:str
class ConversationIn(BaseModel): specialist_id:str=Field(min_length=1,max_length=80); title:str=Field(default="Nova conversa",max_length=160)
class MessageIn(BaseModel): content:str=Field(min_length=1,max_length=MAX_CHARS)
class FeedbackIn(BaseModel): message_id:str; accepted:bool
class CurateIn(BaseModel): state:str=Field(pattern="^(approved|rejected)$"); rationale:str=Field(min_length=3,max_length=1000)
@app.get("/health")
@app.get("/api/v1/health")
def health(): return {"status":"ok","service":"APP_COM_ESPECIALISTA","api_version":"v1"}
@app.post("/api/v1/auth/register",status_code=201)
def register(body:RegisterIn):
 uid=secrets.token_hex(16)
 role="user"
 try:
  with db() as c: c.execute("INSERT INTO users(id,email,password_hash,role,created_at) VALUES(?,?,?,?,?)",(uid,body.email,password_hash(body.password),role,now()))
 except sqlite3.IntegrityError: raise HTTPException(409,detail={"code":"USER_EXISTS","message":"Já existe uma conta com este email."})
 audit(uid,"user.register","user",uid)
 return {"access_token":token_for(uid,role),"token_type":"bearer","expires_in":JWT_TTL}
@app.post("/api/v1/auth/token")
def login(body:LoginIn):
 with db() as c: u=c.execute("SELECT * FROM users WHERE email=?",(body.email.strip().lower(),)).fetchone()
 if not u or u["disabled"] or not verify_password(body.password,u["password_hash"]): raise HTTPException(401,detail={"code":"AUTH_INVALID_CREDENTIALS","message":"Credenciais inválidas."})
 audit(u["id"],"user.login","user",u["id"]); return {"access_token":token_for(u["id"],u["role"]),"token_type":"bearer","expires_in":JWT_TTL}
@app.get("/api/v1/specialists")
def specialists(q:str|None=None,user=Depends(current_user)):
 items=SPECIALISTS
 if q:
  q=q.lower(); items=[s for s in items if q in (s["name"]+" "+s["domain"]+" "+s["description"]).lower()]
 return {"items":items,"count":len(items)}
@app.get("/api/v1/specialists/{sid}")
def specialist(sid:str,user=Depends(current_user)):
 s=next((x for x in SPECIALISTS if x["id"]==sid and x["status"]=="active"),None)
 if not s: raise HTTPException(404,detail={"code":"SPECIALIST_NOT_FOUND","message":"Especialista ativo não encontrado."})
 return s
@app.post("/api/v1/triage")
def triage(body:MessageIn,user=Depends(current_user)):
 text=body.content.lower()
 if any(w in text for w in ("suicídio","suicidio","quero morrer","emergência médica","emergencia medica")):
  return {"status":"escalate","specialist":None,"reason":"Possível situação de alto risco. Procure serviços de emergência ou apoio humano adequado.","requires_human_support":True}
 sid="software" if any(w in text for w in ("python","código","codigo","api","software","programar","bug","servidor")) else "general"
 s=next(x for x in SPECIALISTS if x["id"]==sid); audit(user["id"],"triage.completed","specialist",sid,{"input_length":len(body.content)})
 return {"status":"matched","specialist":s,"reason":"Correspondência inicial baseada em regras; confirme adequação em temas especializados.","requires_human_support":False}
def own_conversation(c,cid,uid):
 r=c.execute("SELECT * FROM conversations WHERE id=? AND user_id=?",(cid,uid)).fetchone()
 if not r: raise HTTPException(404,detail={"code":"CONVERSATION_NOT_FOUND","message":"Conversa não encontrada."})
 return r
def provider_reply(s,history):
 if not OPENAI_API_KEY: raise HTTPException(503,detail={"code":"AI_PROVIDER_NOT_CONFIGURED","message":"Defina OPENAI_API_KEY antes de usar conversas."})
 try:
  from openai import OpenAI
  client=OpenAI(api_key=OPENAI_API_KEY,timeout=30.0,max_retries=1)
  system=("És um especialista virtual de IA, não um profissional humano. Explicita incerteza, respeita limites e encaminha riscos. Especialidade: "+s["name"]+". Limites: "+str(s["limits"]))
  result=client.chat.completions.create(model=OPENAI_MODEL,messages=[{"role":"system","content":system},*history],max_tokens=1200)
  return result.choices[0].message.content or "Não foi possível produzir uma resposta."
 except HTTPException: raise
 except Exception: raise HTTPException(502,detail={"code":"AI_PROVIDER_ERROR","message":"O fornecedor de IA não respondeu com sucesso."})
@app.post("/api/v1/conversations",status_code=201)
def create_conversation(body:ConversationIn,user=Depends(current_user)):
 s=next((x for x in SPECIALISTS if x["id"]==body.specialist_id and x["status"]=="active"),None)
 if not s: raise HTTPException(404,detail={"code":"SPECIALIST_NOT_FOUND","message":"Especialista ativo não encontrado."})
 cid=secrets.token_hex(16); ts=now()
 with db() as c: c.execute("INSERT INTO conversations VALUES(?,?,?,?,?,?,?)",(cid,user["id"],s["id"],s["version"],body.title,ts,ts))
 audit(user["id"],"conversation.created","conversation",cid,{"specialist_id":s["id"]})
 return {"id":cid,"specialist_id":s["id"],"specialist_version":s["version"],"title":body.title,"created_at":ts}
@app.post("/api/v1/conversations/{cid}/messages",status_code=201)
def send_message(cid:str,body:MessageIn,user=Depends(current_user)):
 with db() as c:
  conv=own_conversation(c,cid,user["id"]); rows=c.execute("SELECT role,content FROM messages WHERE conversation_id=? AND user_id=? ORDER BY created_at DESC LIMIT 20",(cid,user["id"])).fetchall()
 history=[{"role":r["role"],"content":r["content"]} for r in reversed(rows)]+[{"role":"user","content":body.content}]
 s=next(x for x in SPECIALISTS if x["id"]==conv["specialist_id"]); answer=provider_reply(s,history); ts=now(); um,am=secrets.token_hex(16),secrets.token_hex(16)
 with db() as c:
  c.execute("INSERT INTO messages VALUES(?,?,?,?,?,?,?)",(um,cid,user["id"],"user",body.content,0,ts))
  c.execute("INSERT INTO messages VALUES(?,?,?,?,?,?,?)",(am,cid,user["id"],"assistant",answer,0,ts))
  c.execute("UPDATE conversations SET updated_at=? WHERE id=? AND user_id=?",(ts,cid,user["id"]))
 audit(user["id"],"conversation.message","conversation",cid,{"input_chars":len(body.content),"specialist_version":conv["specialist_version"]})
 return {"user_message_id":um,"message_id":am,"role":"assistant","content":answer,"created_at":ts,"specialist_version":conv["specialist_version"]}
@app.get("/api/v1/conversations")
def list_conversations(user=Depends(current_user)):
 with db() as c: rows=c.execute("SELECT id,specialist_id,specialist_version,title,created_at,updated_at FROM conversations WHERE user_id=? ORDER BY updated_at DESC LIMIT 100",(user["id"],)).fetchall()
 return {"items":[dict(r) for r in rows]}
@app.get("/api/v1/conversations/{cid}")
def get_conversation(cid:str,user=Depends(current_user)):
 with db() as c:
  conv=own_conversation(c,cid,user["id"]); msgs=c.execute("SELECT id,role,content,accepted,created_at FROM messages WHERE conversation_id=? AND user_id=? ORDER BY created_at",(cid,user["id"])).fetchall()
 out=dict(conv); out["messages"]=[dict(m) for m in msgs]; return out
@app.post("/api/v1/feedback")
def feedback(body:FeedbackIn,user=Depends(current_user)):
 with db() as c:
  m=c.execute("SELECT m.*,v.specialist_id FROM messages m JOIN conversations v ON v.id=m.conversation_id WHERE m.id=? AND m.user_id=? AND v.user_id=? AND m.role='assistant'",(body.message_id,user["id"],user["id"])).fetchone()
  if not m: raise HTTPException(404,detail={"code":"MESSAGE_NOT_FOUND","message":"Resposta não encontrada."})
  c.execute("UPDATE messages SET accepted=? WHERE id=? AND user_id=?",(int(body.accepted),body.message_id,user["id"]))
  if body.accepted: c.execute("INSERT INTO curated_memory(id,specialist_id,source_message_id,content,state,created_at) VALUES(?,?,?,?,?,?)",(secrets.token_hex(16),m["specialist_id"],m["id"],m["content"],"pending",now()))
 audit(user["id"],"feedback.recorded","message",body.message_id,{"accepted":body.accepted})
 return {"message_id":body.message_id,"accepted":body.accepted,"curation_status":"pending" if body.accepted else "not_submitted"}
@app.get("/api/v1/me/export")
def export_data(user=Depends(current_user)):
 with db() as c:
  conv=c.execute("SELECT * FROM conversations WHERE user_id=?",(user["id"],)).fetchall(); msgs=c.execute("SELECT * FROM messages WHERE user_id=?",(user["id"],)).fetchall()
 audit(user["id"],"privacy.export","user",user["id"])
 return {"exported_at":now(),"user":{"id":user["id"],"email":user["email"]},"conversations":[dict(x) for x in conv],"messages":[dict(x) for x in msgs]}
@app.delete("/api/v1/me",status_code=204)
def delete_account(user=Depends(current_user)):
 with db() as c:
  c.execute("DELETE FROM users WHERE id=?",(user["id"],))
  c.execute("DELETE FROM audit WHERE actor_id=? AND action!='privacy.delete_requested'",(user["id"],))
  c.execute("INSERT INTO audit VALUES(?,?,?,?,?,?,?)",(secrets.token_hex(16),user["id"],"privacy.delete_requested","user",user["id"],"{}",now()))
 return Response(status_code=204)
@app.get("/api/v1/admin/memory")
def pending_memory(user=Depends(admin_user)):
 with db() as c: rows=c.execute("SELECT id,specialist_id,content,state,created_at FROM curated_memory WHERE state='pending' ORDER BY created_at LIMIT 100").fetchall()
 return {"items":[dict(r) for r in rows]}
@app.post("/api/v1/admin/memory/{mid}/review")
def review_memory(mid:str,body:CurateIn,user=Depends(admin_user)):
 with db() as c:
  r=c.execute("SELECT * FROM curated_memory WHERE id=? AND state='pending'",(mid,)).fetchone()
  if not r: raise HTTPException(404,detail={"code":"MEMORY_ITEM_NOT_FOUND","message":"Item pendente não encontrado."})
  c.execute("UPDATE curated_memory SET state=?,reviewer_id=?,reviewed_at=? WHERE id=?",(body.state,user["id"],now(),mid))
 audit(user["id"],"memory.reviewed","memory",mid,{"state":body.state,"rationale":body.rationale})
 return {"id":mid,"state":body.state,"reviewed_by":user["id"]}
@app.get("/api/v1/admin/audit")
def audit_log(limit:int=100,user=Depends(admin_user)):
 limit=max(1,min(limit,500))
 with db() as c: rows=c.execute("SELECT id,actor_id,action,resource_type,resource_id,metadata_json,created_at FROM audit ORDER BY created_at DESC LIMIT ?",(limit,)).fetchall()
 return {"items":[dict(r) for r in rows]}
