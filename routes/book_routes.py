from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.books import Book
from models.user import User
from schema.user_schema import UserRegister, UserLogin
from schema.books_schema import BookSchema
from Database.db import get_db
from commons.authentication import jwt_required_decorator
from commons.authentication import user_authentication

router = APIRouter()


# User registration route
@router.post("/register/", response_model=UserRegister)
def register_user(user: UserRegister, db: Session = Depends(get_db)):
    try:
        # Check if the user already exists
        existing_user = db.query(User).filter(User.username == user.username).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already registered")

        new_user = User(
            username=user.username,
            password=user.password,
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return {"message": "User registered successfully", "username": new_user.username}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# User login route
@router.post("/login/")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    print(f"Found user: {db_user.username}")
    if db_user.password != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = user_authentication(user.username, user.password, db)
    return {"access_token": token, "token_type": "bearer"}
# GET ALL RECORD
@router.get("/books/",response_model=list[BookSchema])
@jwt_required_decorator
def get_all_books(db:Session=Depends(get_db)):
    books = db.query(Book).all()
    return books


# GET SPECIFIC RECORD/ BY ID
@router.get("/books/{book_id}",response_model=BookSchema)
@jwt_required_decorator
def get_book_by_id(book_id:int,db:Session=Depends(get_db)):
    book=db.query(Book).filter(Book.id==book_id).first()
    if book is None:
        raise HTTPException(status_code=404,detail="Book not found")
    return book


# ADD NEW BOOK
@router.post("/books/add/",response_model=BookSchema)
@jwt_required_decorator
def add_book_record(book:BookSchema,db:Session=Depends(get_db)):
    add_book=Book(
        title=book.title,
        author=book.author,
        description=book.description
    )
    db.add(add_book)
    db.commit()
    db.refresh(add_book)
    return add_book


#DELETE RECORD
@router.delete("book/{book_id")
@jwt_required_decorator
def delete_book_record(book_id:int,db:Session=Depends(get_db)):
    delete_book=db.query(Book).filter(Book.id==book_id).first()
    if delete_book is None:
        raise HTTPException(status_code=404,detail="Book not found")
    db.delete(delete_book)
    db.commit()
    return "Book deleted"
