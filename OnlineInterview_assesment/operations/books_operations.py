from schemas import  *

class BookOperations:
    def __init__(self ,db_conn):
        self.db_conn = db_conn


    def book_aviavlable(self,title):

        return self.db_conn.query(Book).filter(Book.title == title).first()

    def add_books(self,book_info):
        try:
            new_book = Book(**book_info.dict())
            self.db_conn.add(new_book)
            self.db_conn.commit()
            self.db_conn.refresh(new_book)
            return new_book
        except Exception as exp:
            return False

    def get_book(self,book_id):
        return self.db_conn.query(Book).filter(Book.id == book_id).first()

    def update_book(self,book,updated_book):
        try:
            for key, value in updated_book.items():
                setattr(book, key, value)
            self.db_conn.commit()
            self.db_conn.refresh(book)
            return book
        except:
            return False

    def book_deleted(self,book):
        try:
            self.db_conn.delete(book)
            self.db_conn.commit()
            return {"message": "Book deleted successfully"}
        except:
            return False