from starlette.exceptions import HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from app.database.repository import get_repository
from app.domains.menu.model import Menu
from app.routes.menu.menu_request import CreateMenuRequest
from app.routes.menu.menu_response import MenuResponse


def update_menu(
        id: int,
        create_menu_request: CreateMenuRequest,
):
    repository = next(get_repository())
    menu = repository.get_by_id(Menu, id)
    if not menu:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND)
    menu.update(create_menu_request)
    repository.save(menu)
    response = MenuResponse.from_domain(menu)
    return response


def get_menu_by_id(id: int):
    repository = next(get_repository())
    response = repository.get_by_id(Menu, id)
    if not response:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND)
    return response


def create_menu(create_menu_request):
    repository = next(get_repository())
    menu = create_menu_request.to_domain()
    repository.save(menu)
