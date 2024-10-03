# main.py
from fastapi import FastAPI
from Database.db import engine
from models.books import Base
from models.user import Base as User
from routes.book_routes import router as books_router
from Middleware.Response_time import add_process_time_header

app = FastAPI()

# Add the middleware to the FastAPI application
add_process_time_header(app)

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)
User.metadata.create_all(bind=engine)

# Include the books router
app.include_router(books_router, prefix="/api")
