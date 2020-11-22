from datetime import datetime

from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declared_attr

from app.exception.models import NotFoundException


class AbstractModelMixin:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=lambda: datetime.now())
    updated_at = Column(DateTime, default=lambda: datetime.now(), onupdate=lambda: datetime.now())
    deleted_at = Column(DateTime, nullable=True, )

    def is_inactive(self) -> bool:
        return self.deleted_at != None

    def __validate(self) -> None:
        if self.is_inactive():
            raise NotFoundException(f'{self.__class__.__name__} not found.')

    def inactivate(self) -> None:
        self.__validate()
        self.deleted_at = datetime.now()

