from pydantic import BaseModel

from app.domains.menu.model import Menu


class CreateMenuRequest(BaseModel):
    number:int
    food: str
    categorie: str
    restaurant: str

    def to_domain(self):
        return Menu(
            number=self.number,
            food=self.food,
            categorie=self.categorie,
            restaurant=self.restaurant,
        )