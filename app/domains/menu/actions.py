<<<<<<< HEAD
from starlette.exceptions import HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from app.database.repository import Repository, get_repository
from app.domains.menu.model import Menu
from app.routes.menu.menu_request import CreateMenuRequest
from app.routes.menu.menu_response import MenuResponse
=======
from fastapi import Depends
from starlette.exceptions import HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from app import CreateMenuRequest, Repository, get_repository
from app.domains.menu.model import Menu
>>>>>>> feature/create_update_menu


def update_menu(
        id: int,
        create_menu_request: CreateMenuRequest,
<<<<<<< HEAD
        repository: Repository = next(get_repository())
):
    menu = repository.get_by_id(Menu, id)
    print(menu)
    if not menu:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND)
    menu.update(create_menu_request)
    repository.save(menu)
    response = MenuResponse.from_domain(menu)
    return response
=======
        repository: Repository = Depends(get_repository)
):
    menu = repository.get_by_id(Menu, id)
    if not menu:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND)
    menu.update(create_menu_request)
    repository.insert(menu)
    return menu
>>>>>>> feature/create_update_menu
