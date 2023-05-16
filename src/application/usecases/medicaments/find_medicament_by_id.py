# pylint: disable=broad-exception-raised
from src.application.repositories.medicament_repository import MedicamentRepository
from src.domain.entities.medicament import Medicament


class FindByIdMedicamentUseCase:
    """Use Case to find a medicament by id"""

    def __init__(self, medicament_repository: MedicamentRepository):
        self.medicament_repository = medicament_repository

    async def execute(self, medicament_id: str) -> Medicament:
        medicament = await self.medicament_repository.find_by_id(medicament_id)

        if not medicament:
            raise Exception("Medicament not found!")

        return medicament
