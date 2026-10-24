"""Cliente de exemplo; usa apenas o contrato público."""
import os
import requests
base=os.getenv("CPE_API_BASE_URL","http://127.0.0.1:8000/api/v1")
email=os.environ["CPE_CLIENT_EMAIL"]
password=os.environ["CPE_CLIENT_PASSWORD"]
s=requests.Session()
r=s.post(base+"/auth/token",json={"email":email,"password":password},timeout=10); r.raise_for_status()
s.headers["Authorization"]="Bearer "+r.json()["access_token"]
r=s.get(base+"/specialists",timeout=10); r.raise_for_status()
print("Catálogo:",[x["id"] for x in r.json()["items"]])
r=s.post(base+"/triage",json={"content":"Preciso de ajuda com um bug Python"},timeout=10); r.raise_for_status()
print("Triagem:",r.json()["status"],r.json().get("specialist",{}).get("id"))
