from fastapi import FastAPI, Depends
from starlette.status import HTTP_201_CREATED

from app.database.repository import get_repository, Repository
from app.domains.food.menu_request import CreateMenuRequest

app = FastAPI()

@app.post("/", status_code=HTTP_201_CREATED)
def create_menu(
        create_menu_request : CreateMenuRequest,
        repository:Repository = Depends(get_repository),
):
    menu = create_menu_request.to_domain()
    repository.insert(menu)


