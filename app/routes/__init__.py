from fastapi import APIRouter
from app.routes.menu import menu_routes

api_router = APIRouter()

api_router.include_router(
    menu_routes.router,
    prefix='/menu',
    tags=['menu'],
)

