from datetime import datetime
from pydantic import BaseModel


class CreateMedicamentRequest(BaseModel):
    name: str
    price: float
    description: str | None
    status: str | None
    priority: str | None
    image_url: str | None
    expiration_date: datetime
