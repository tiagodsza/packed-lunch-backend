from sqlalchemy import Column, Integer, String

from app.database.config import Base
from app.database.model import AbstractModelMixin


class Menu(Base, AbstractModelMixin):
    number = Column(Integer, unique=True, nullable=False)
    food = Column(String(length=200), nullable=False)
    categorie = Column(String(), nullable=True)
    restaurant = Column(String(), nullable=False)

    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)

    def update(
            self,
            create_menu_request,
    ):
        self.number = create_menu_request.number or self.number
        self.food = create_menu_request.food or self.food
        self.categorie = create_menu_request.categorie or self.categorie
        self.restaurant = create_menu_request.restaurant or self.restaurant
