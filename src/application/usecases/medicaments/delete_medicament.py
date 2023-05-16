from src.application.repositories.medicament_repository import MedicamentRepository


class DeleteMedicamentUseCase:
    """Use Case to delete a medicament by id"""

    def __init__(self, medicament_repository: MedicamentRepository):
        self.medicament_repository = medicament_repository

    async def execute(self, medicament_id: str) -> str:
        if not medicament_id:
            raise ValueError("Medicament id is required")

        await self.medicament_repository.delete(medicament_id)

        return f"Medicament {medicament_id} was successfully deleted"
