from fastapi import FastAPI
from src.controller import api

app = FastAPI(title="Link Checker", description="Checks for affiliate links in the database.")

app.include_router(api.app)


@app.get("/")
def read_root():
    return {"message": "Welcome to Link Checker API!"}
