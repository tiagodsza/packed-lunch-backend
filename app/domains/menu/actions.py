from fastapi import Depends
from starlette.exceptions import HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from app import CreateMenuRequest, Repository, get_repository
from app.domains.menu.model import Menu


def update_menu(
        id: int,
        create_menu_request: CreateMenuRequest,
        repository: Repository = Depends(get_repository)
):
    menu = repository.get_by_id(Menu, id)
    if not menu:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND)
    menu.update(create_menu_request)
    repository.insert(menu)
    return menu
