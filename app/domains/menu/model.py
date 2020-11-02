from sqlalchemy import Column, Integer, String

from app.database.config import Base
from app.database.model import AbstractModelMixin


class Menu(Base, AbstractModelMixin):
    __tablename__ = 'menu'

    number = Column(Integer, unique=True, nullable=False)
    food = Column(String(length=200), nullable=False)
    categorie = Column(String(), nullable=True)
    restaurant = Column(String(), nullable=False)

    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
