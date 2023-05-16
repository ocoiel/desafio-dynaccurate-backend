from src.application.repositories.medicament_repository import MedicamentRepository
from src.domain.entities.medicament import Medicament


class FindAllMedicamentUseCase:
    """Use Case to find all medicaments"""

    def __init__(self, medicament_repository: MedicamentRepository):
        self.medicament_repository = medicament_repository

    async def execute(self) -> list[Medicament]:
        medicaments = await self.medicament_repository.find_all()

        return medicaments or []
