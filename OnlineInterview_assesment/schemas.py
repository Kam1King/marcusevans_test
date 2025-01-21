from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False )
    email = Column(String)
    hashed_password = Column(String)
    role = Column(String )

class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    is_available = Column(Boolean)


class BorrowRecord(Base):
    __tablename__ = "borrowrecord"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id"))
    book_id = Column(Integer, ForeignKey("Book.id"))
    due_date = Column(String)

    # user = relationship("User")
    # book = relationship("Book")