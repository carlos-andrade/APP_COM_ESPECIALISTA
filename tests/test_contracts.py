import os, tempfile
os.environ.setdefault("CPE_JWT_SECRET","test-secret-that-is-at-least-32-bytes-long")
os.environ.setdefault("CPE_DB_PATH",tempfile.mktemp(suffix=".sqlite3"))
os.environ.setdefault("CPE_ADMIN_BOOTSTRAP_TOKEN","test-bootstrap-secret")
from fastapi.testclient import TestClient
from app.main import app, init_db, db, now
init_db()
client=TestClient(app)
def register(email="test@example.com"):
 return client.post("/api/v1/auth/register",json={"email":email,"password":"a-long-test-password-123"})
def test_health_public():
 assert client.get("/api/v1/health").status_code==200
def test_auth_required():
 assert client.get("/api/v1/specialists").status_code==401
def test_register_catalog():
 r=register(); assert r.status_code==201
 token=r.json()["access_token"]
 result=client.get("/api/v1/specialists",headers={"Authorization":"Bearer "+token})
 assert result.status_code==200 and {x["id"] for x in result.json()["items"]}>={"general","software"}
def test_duplicate_user_conflict():
 assert register("dupe@example.com").status_code==201
 assert register("dupe@example.com").status_code==409
def test_triage_software():
 token=register("triage@example.com").json()["access_token"]
 r=client.post("/api/v1/triage",headers={"Authorization":"Bearer "+token},json={"content":"Tenho um bug em Python na API"})
 assert r.status_code==200 and r.json()["specialist"]["id"]=="software"
def test_conversation_isolation():
 a=register("owner@example.com").json()["access_token"]; b=register("other@example.com").json()["access_token"]
 created=client.post("/api/v1/conversations",headers={"Authorization":"Bearer "+a},json={"specialist_id":"general","title":"private"})
 assert created.status_code==201
 leaked=client.get("/api/v1/conversations/"+created.json()["id"],headers={"Authorization":"Bearer "+b})
 assert leaked.status_code==404
def test_message_length_validation():
 token=register("limits@example.com").json()["access_token"]
 r=client.post("/api/v1/triage",headers={"Authorization":"Bearer "+token},json={"content":"x"*8001})
 assert r.status_code==422

def test_bootstrap_admin_is_one_time():
    email="admin-bootstrap@example.com"
    token=register(email).json()["access_token"]
    headers={"Authorization":"Bearer "+token,"X-Admin-Bootstrap-Token":os.environ["CPE_ADMIN_BOOTSTRAP_TOKEN"]}
    first=client.post("/api/v1/admin/bootstrap",headers=headers)
    assert first.status_code==200
    second=client.post("/api/v1/admin/bootstrap",headers=headers)
    assert second.status_code==409

def test_export_and_delete_own_account():
    token=register("privacy@example.com").json()["access_token"]
    headers={"Authorization":"Bearer "+token}
    exported=client.get("/api/v1/me/export",headers=headers)
    assert exported.status_code==200
    assert exported.json()["user"]["email"]=="privacy@example.com"
    deleted=client.delete("/api/v1/me",headers=headers)
    assert deleted.status_code==204
    assert client.get("/api/v1/specialists",headers=headers).status_code==401

def test_invalid_bearer_token_rejected():
    response=client.get("/api/v1/specialists",headers={"Authorization":"Bearer invalid.token.value"})
    assert response.status_code==401

def test_regular_user_cannot_read_admin_memory():
    token=register("not-admin@example.com").json()["access_token"]
    response=client.get("/api/v1/admin/memory",headers={"Authorization":"Bearer "+token})
    assert response.status_code==403

def test_feedback_requires_explicit_acceptance_and_curates_pending():
    token=register("memory-owner@example.com").json()["access_token"]
    headers={"Authorization":"Bearer "+token}
    conv=client.post("/api/v1/conversations",headers=headers,json={"specialist_id":"general","title":"memory test"})
    assert conv.status_code==201
    cid=conv.json()["id"]
    with db() as connection:
        connection.execute("INSERT INTO messages VALUES(?,?,?,?,?,?,?)",("assistant-test-id",cid,client.get("/api/v1/me/export",headers=headers).json()["user"]["id"],"assistant","Resposta de teste para curadoria.",0,now()))
    accepted=client.post("/api/v1/feedback",headers=headers,json={"message_id":"assistant-test-id","accepted":True})
    assert accepted.status_code==200 and accepted.json()["curation_status"]=="pending"
    with db() as connection:
        item=connection.execute("SELECT state FROM curated_memory WHERE source_message_id=?",("assistant-test-id",)).fetchone()
        assert item["state"]=="pending"
    withdrawn=client.post("/api/v1/feedback",headers=headers,json={"message_id":"assistant-test-id","accepted":False})
    assert withdrawn.status_code==200 and withdrawn.json()["curation_status"]=="not_submitted"
    with db() as connection:
        assert connection.execute("SELECT 1 FROM curated_memory WHERE source_message_id=?",("assistant-test-id",)).fetchone() is None
