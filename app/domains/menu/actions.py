from app.database.repository import get_repository
from app.domains.menu.model import Menu
from app.exception.models import NotFoundException
from app.routes.menu.menu_request import CreateMenuRequest
from app.routes.menu.menu_response import MenuResponse


def update_menu(
        id: int,
        create_menu_request: CreateMenuRequest,
):
    repository = get_repository()
    menu = repository.get_by_id(Menu, id)
    if not menu:
        raise NotFoundException('Menu not found!')
    menu.update(create_menu_request)
    repository.save(menu)
    response = MenuResponse.from_domain(menu)
    return response


def get_menu_by_id(id: int):
    repository = get_repository()
    menu = repository.get_by_id(Menu, id)
    if not menu:
        raise NotFoundException('Menu not found!')
    response = MenuResponse.from_domain(menu)
    return response


def create_menu(create_menu_request):
    repository = get_repository()
    menu = create_menu_request.to_domain()
    repository.save(menu)
    response = MenuResponse.from_domain(menu)
    return response

def delete_menu(id: int):
    repository = get_repository()
    menu = repository.get_by_id(Menu, id)
    if not menu:
        raise NotFoundException('Menu not found!')
    menu.inactivate()
    repository.save(menu)
    response = MenuResponse.from_domain(menu)
    return response