from fastapi import APIRouter, Depends
from starlette.exceptions import HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_404_NOT_FOUND

from app import CreateMenuRequest, get_repository, Repository
from app.domains.menu.actions import update_menu
from app.domains.menu.model import Menu

router = APIRouter()

@router.post('/', status_code=HTTP_201_CREATED)
def create_menu(
        create_menu_request: CreateMenuRequest,
        repository: Repository = Depends(get_repository),
):
    menu = create_menu_request.to_domain()
    repository.insert(menu)

@router.get('/', status_code=HTTP_200_OK)
def get(
    repository: Repository = Depends(get_repository),
):
    response = repository.get(Menu)
    return response

@router.get('/{id}')
def get_by_id(
        id: int,
        repository: Repository = Depends(get_repository)
):
    response = repository.get_by_id(Menu, id)
    if not response:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND)
    return response

@router.put('/{id}')
def update(
        id: int,
        create_menu_request: CreateMenuRequest,
):
    response = update_menu(id, create_menu_request)
    return response




