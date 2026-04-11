from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config import settings


class Base(DeclarativeBase):
    pass


engine = create_engine(url=settings.DATABASE_URL, echo=False)
SessionLocal = sessionmaker(expire_on_commit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
