from fastapi import APIRouter, Depends
from starlette.status import HTTP_201_CREATED, HTTP_200_OK

from app.database.repository import Repository, get_repository
from app.domains.menu.actions import update_menu, get_menu_by_id, create_menu
from app.domains.menu.model import Menu
from app.routes.menu.menu_request import CreateMenuRequest

router = APIRouter()


@router.get('/', status_code=HTTP_200_OK)
def get():
    repository = get_repository()
    response = repository.get(Menu)
    return response


@router.get('/{id}')
def get_by_id(
        id: int,
):
    response = get_menu_by_id(id)
    return response


@router.post('/', status_code=HTTP_201_CREATED)
def post(
        create_menu_request: CreateMenuRequest,
):
    response = create_menu(create_menu_request)
    return response


@router.put('/{id}')
def update(
        id: int,
        create_menu_request: CreateMenuRequest,
):
    response = update_menu(id, create_menu_request)
    return response
