from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

app = FastAPI()

# Define the Base for your models
Base = declarative_base()


# Database configuration using a dictionary (similar to Django)
DATABASES = {
    "default": {
        "ENGINE": "postgresql",
        "NAME": "Shanza",
        "USER": "postgres",
        "PASSWORD": "123",
        "HOST": "localhost",
        "PORT": "5433",
    }
}

print(DATABASE_URL)

DATABASE_URL = f"postgresql+psycopg2://{DATABASES['default']['USER']}:{DATABASES['default']['PASSWORD']}@" \
               f"{DATABASES['default']['HOST']}:{DATABASES['default']['PORT']}/{DATABASES['default']['NAME']}"

# Create an engine and session factory
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()  # Create a new database session
    try:
        yield db  # Allow the session to be used in the endpoint
    finally:
        db.close()