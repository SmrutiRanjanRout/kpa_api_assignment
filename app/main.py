from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal, Base

# Create DB tables
Base.metadata.create_all(bind=engine)

# FastAPI app instance
app = FastAPI(title="KPA Form API")

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST form
@app.post("/forms", response_model=schemas.FormOut)
def submit_form(form: schemas.FormCreate, db: Session = Depends(get_db)):
    return crud.create_form(db, form)

# GET forms
@app.get("/forms", response_model=list[schemas.FormOut])
def list_forms(db: Session = Depends(get_db)):
    return crud.get_all_forms(db)
