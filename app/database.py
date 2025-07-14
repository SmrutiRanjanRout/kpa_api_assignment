from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 🔴 Hardcoded DB URL — fallback since dotenv isn't working
DATABASE_URL = "postgresql://postgres:admin123@localhost/kpa_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
