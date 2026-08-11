from fastapi import FastAPI, HTTPException

app = FastAPI(title="FactLens API")

# Temporary in-memory storage — Day 2 mein isse MySQL se replace karenge
claims_db = []
next_id = 1


@app.get("/")
def root():
    return {"message": "Welcome to FactLens"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/claims")
def create_claim(claim_text: str):
    global next_id
    claim = {
        "id": next_id,
        "text": claim_text,
        "status": "pending"
    }
    claims_db.append(claim)
    next_id += 1
    return claim


@app.get("/claims")
def get_all_claims():
    return claims_db


@app.get("/claims/{claim_id}")
def get_claim(claim_id: int):
    for claim in claims_db:
        if claim["id"] == claim_id:
            return claim
    raise HTTPException(status_code=404, detail="Claim not found")


@app.delete("/claims/{claim_id}")
def delete_claim(claim_id: int):
    global claims_db
    for claim in claims_db:
        if claim["id"] == claim_id:
            claims_db.remove(claim)
            return {"message": "Claim deleted"}
    raise HTTPException(status_code=404, detail="Claim not found")