
from models import *

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from operations.books_operations import BookOperations
from models import *
from database import *


router = APIRouter(tags=["BOOK MANAGEMENT"])



@router.post("/books", response_model=BookOut, status_code=status.HTTP_201_CREATED)
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    book_instance = BookOperations(db)
    if book_instance.book_aviavlable(book.title):
        raise HTTPException(status_code=400, detail="Book with this title already exists")
    if book_instance.add_books(book) is not False:
        return {"book added"}
    return {"book not added"}



@router.get("/books/{book_id}", response_model=BookOut)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book_instance = BookOperations(db)
    book =  book_instance.get_book(book_id)
    if book_instance.get_book(book_id):
        return book
    return {"book not found"}


@router.put("/books/{book_id}", response_model=BookOut)
def update_book(book_id: int, updated_book: BookCreate, user_email: str, db: Session = Depends(get_db)):

    book_instance = BookOperations(db)
    book = book_instance.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    if book_instance.update_book(book,updated_book.dict()) is not False:
        return {"book is updated "}
    return {"book not updated"}



@router.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book_instance = BookOperations(db)
    book = book_instance.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    if book_instance.update_book(book, book.dict()) is not False:
        return {"book is deleted "}
    return {"book not deleted"}