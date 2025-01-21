from routes.book_management import router as book_router
from routes.user_management import router as user_router
from fastapi import FastAPI
from starlette.requests import Request

app = FastAPI()
app.include_router(book_router)
app.include_router(user_router)