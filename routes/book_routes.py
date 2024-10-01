from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.books import Book
from schema.books_schema import BookSchema
from Database.db import get_db

router = APIRouter()

# GET ALL RECORD
@router.get("/books/",response_model=list[BookSchema])
def get_all_books(db:Session=Depends(get_db)):
    books = db.query(Book).all()
    return books


# GET SPECIFIC RECORD/ BY ID
@router.get("/books/{book_id}",response_model=BookSchema)
def get_book_by_id(book_id:int,db:Session=Depends(get_db)):
    book=db.query(Book).filter(Book.id==book_id).first()
    if book is None:
        raise HTTPException(status_code=404,detail="Book not found")
    return book


# ADD NEW BOOK
@router.post("/books/add/",response_model=BookSchema)
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
def delete_book_record(book_id:int,db:Session=Depends(get_db)):
    delete_book=db.query(Book).filter(Book.id==book_id).first()
    if delete_book is None:
        raise HTTPException(status_code=404,detail="Book not found")
    db.delete(delete_book)
    db.commit()
    return "Book deleted"
