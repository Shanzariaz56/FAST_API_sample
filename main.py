# main.py
from fastapi import FastAPI
from Database.db import engine
from models.books import Base
from routes.book_routes import router as books_router

app = FastAPI()

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Include the books router
app.include_router(books_router, prefix="/api")
