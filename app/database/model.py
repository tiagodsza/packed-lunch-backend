from datetime import datetime

from sqlalchemy import Column, Integer, DateTime

from app.exception.models import NotFoundException


class AbstractModelMixin:
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=lambda: datetime.now())
    updated_at = Column(DateTime, default=lambda: datetime.now(), onupdate=lambda: datetime.now(),
    )
    deleted_at = Column(DateTime,nullable=True,)

    def is_inactive(self) -> bool:
        return self.deleted_at is not None

    def inactivate(self) -> None:
        self._validate()
        self.deleted_at = datetime.now()

    def _validate(self) -> None:
        if self.is_inactive():
            raise NotFoundException(f'{self.__class__.__name__} not found.')
