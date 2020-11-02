from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.database.repository import get_repository, Repository
from app.domains.food.menu_request import CreateMenuRequest
from app.routes import api_router

app = FastAPI()

app.include_router(api_router)

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
