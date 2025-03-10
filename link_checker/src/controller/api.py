from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.configs.db import SessionLocal
from src.logics.link_checker import analyze_links

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/check-links/")
def check_links(db: Session = Depends(get_db)):
    """API endpoint to check affiliate links."""
    result = analyze_links(db)
    return result
