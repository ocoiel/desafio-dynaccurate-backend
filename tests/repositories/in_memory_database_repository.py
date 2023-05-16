from pydantic import UUID4
from src.application.repositories.medicament_repository import MedicamentRepository

from src.domain.entities.medicament import Medicament


class InMemoryDatabaseMedicamentRepository(MedicamentRepository):
    def __init__(self):
        self.database = {}

    async def create(self, medicament: Medicament):
        medicament = Medicament(
            id=medicament.id,
            name=medicament.name,
            price=medicament.price,
            expiration_date=medicament.expiration_date,
            image_url=medicament.image_url,
        )
        self.database[medicament.id] = medicament

        return medicament

    async def find_all(self):
        return list(self.database.values())

    async def find_by_id(self, medicament_id: str):
        return [
            medicament
            for _, medicament in self.database.items()
            if medicament.id == medicament_id
        ][0]

    async def update(self, medicament: Medicament):
        raise NotImplementedError

    async def delete(self, medicament_id: str):
        await self.database.pop(UUID4(medicament_id))
