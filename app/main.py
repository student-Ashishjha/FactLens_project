from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from app.db.database import Base, engine, get_db
from app.models.claim import Claim
from app.schemas.claim import ClaimCreate, ClaimResponse

# Tables banao agar exist nahi karte (sirf development ke liye, production mein migrations use karte hain)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FactLens API")


@app.get("/")
def root():
    return {"message": "Welcome to FactLens"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/claims", response_model=ClaimResponse)
def create_claim(claim: ClaimCreate, db: Session = Depends(get_db)):
    new_claim = Claim(text=claim.text)
    db.add(new_claim)
    db.commit()
    db.refresh(new_claim)
    return new_claim


@app.get("/claims", response_model=list[ClaimResponse])
def get_all_claims(db: Session = Depends(get_db)):
    return db.query(Claim).all()


@app.get("/claims/{claim_id}", response_model=ClaimResponse)
def get_claim(claim_id: int, db: Session = Depends(get_db)):
    claim = db.query(Claim).filter(Claim.id == claim_id).first()
    if not claim:
        raise HTTPException(status_code=404, detail="Claim not found")
    return claim


@app.put("/claims/{claim_id}/verify", response_model=ClaimResponse)
def verify_claim(claim_id: int, db: Session = Depends(get_db)):
    claim = db.query(Claim).filter(Claim.id == claim_id).first()
    if not claim:
        raise HTTPException(status_code=404, detail="Claim not found")
    claim.status = "verified"
    db.commit()
    db.refresh(claim)
    return claim


@app.delete("/claims/{claim_id}")
def delete_claim(claim_id: int, db: Session = Depends(get_db)):
    claim = db.query(Claim).filter(Claim.id == claim_id).first()
    if not claim:
        raise HTTPException(status_code=404, detail="Claim not found")
    db.delete(claim)
    db.commit()
    return {"message": "Claim deleted"}