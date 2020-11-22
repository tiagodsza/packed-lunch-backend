from datetime import datetime

from pydantic import BaseModel


class MenuResponse(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime = None
    number: int
    food: str
    categorie: str
    restaurant: str

    @classmethod
    def from_domain(cls, data):
        return MenuResponse(
            id=data.id,
            created_at=data.created_at,
            updated_at=data.updated_at,
            deleted_at=data.deleted_at,
            number=data.number,
            food=data.food,
            categorie=data.categorie,
            restaurant=data.restaurant,
        )
