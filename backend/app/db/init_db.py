from app.db.database import engine, Base
from app.models.clan import Clan

def init_db():
    Base.metadata.create_all(bind=engine)
