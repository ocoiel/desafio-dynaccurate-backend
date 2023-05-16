from datetime import datetime
from pydantic import BaseModel


class UpdateMedicamentRequest(BaseModel):
    id: str
    name: str | None
    price: float
    description: str | None
    status: str | None
    priority: str | None
    image_url: str | None
    expiration_date: datetime
