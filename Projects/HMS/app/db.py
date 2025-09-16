from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from app.config import DB_URL

engine = create_engine(DB_URL, echo=False, future=True)
SessionLocal = scoped_session(sessionmaker(bind=engine))

def init_db(Base):
    Base.metadata.create_all(bind=engine)