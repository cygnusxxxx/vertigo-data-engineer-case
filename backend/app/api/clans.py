from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.models.clan import Clan

router = APIRouter(prefix="/clans", tags=["clans"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_clan(name: str, region: str, db: Session = Depends(get_db)):
    clan = Clan(name=name, region=region)
    db.add(clan)
    db.commit()
    db.refresh(clan)
    return clan

@router.get("/")
def list_clans(db: Session = Depends(get_db)):
    return db.query(Clan).all()
from sqlalchemy import func

@router.get("/search")
def search_clans(q: str, db: Session = Depends(get_db)):
    if len(q) < 3:
        return []

    return (
        db.query(Clan)
        .filter(func.lower(Clan.name).contains(q.lower()))
        .all()
    )
@router.delete("/{clan_id}")
def delete_clan(clan_id: str, db: Session = Depends(get_db)):
    clan = db.query(Clan).filter(Clan.id == clan_id).first()

    if not clan:
        return {"detail": "Clan not found"}

    db.delete(clan)
    db.commit()

    return {"detail": "Clan deleted"}
