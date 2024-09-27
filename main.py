from fastapi import FastAPI
from fastapi import HTTPException
from schema import Books
import uuid

app = FastAPI()

# In-memory list to store books
books_list = [

]

# GET ALL RECORD
@app.get("/books/",response_model=list[Books])
def get_all_books():
    return books_list

# GET SPECIFIC RECORD/ BY ID
@app.get("/books/{book_id}",response_model=Books)
def get_book_by_id(book_id:uuid.UUID):
    for book in books_list:
        if book.id==book_id:
            return book
    return {"message":"books not found"}

# ADD NEW BOOK
@app.post("/books/add/",response_model=Books)
def add_book(book:Books):
    books_list.append(book)
    return books_list

# UPDATE ALREADY EXISTING BOOK
@app.put("books/{book_id}",response_model=Books)
def update_books(book_id:uuid.UUID,books:Books):
    for book in books_list:
        if book.id==book_id:
            book.title=books.title
            book.author=books.author
            book.description=books.description
            return book
    raise HTTPException(status_code=404, detail="Book not found")

#DELETE RECORD
@app.delete("/books/{book_id}")
def delete_book(book_id:uuid.UUID):
    for book in books_list:
        if book.id==book_id:
            books_list.remove(book)
    return {"message":"books deleted"}



