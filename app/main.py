from fastapi import FastAPI
from .database import engine, Base
from .routers import auth, transactions

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Personal Finance Tracker")

app.include_router(auth.router)
app.include_router(transactions.router)

@app.get("/")
def root():
    return {"message": "Welcome to Personal Finance Tracker API"}
