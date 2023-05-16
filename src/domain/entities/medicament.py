from uuid import uuid4
from datetime import datetime
from pydantic import BaseModel, Field, UUID4, PrivateAttr


class Medicament(BaseModel):
    """It represents an user domain entity."""

    id: UUID4 = Field(default_factory=uuid4)
    name: str
    price: float
    status: str | None
    priority: str | None
    description: str | None
    image_url: str | None = "https://via.placeholder.com/300x200"
    expiration_date: datetime
    _created_at: datetime = PrivateAttr(default_factory=datetime.now)
    _updated_at: datetime = PrivateAttr(default_factory=datetime.now)

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value) -> None:
        self._updated_at = value
