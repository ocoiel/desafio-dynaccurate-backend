from datetime import datetime

from src.application.repositories.medicament_repository import MedicamentRepository
from src.domain.entities.medicament import Medicament
from src.infrastructure.http.dtos.update_medicament_dto import UpdateMedicamentRequest


class UpdateMedicamentUseCase:
    """Use case to update a already existing medicament."""

    def __init__(self, medicament_repository: MedicamentRepository):
        self.medicament_repository = medicament_repository

    async def execute(self, request: UpdateMedicamentRequest) -> str:
        new_medicament = Medicament(
            name=request.name or "",
            price=request.price or 0,
            description=request.description or "",
            status=request.status or "",
            priority=request.priority or "",
            image_url=request.image_url,
            expiration_date=request.expiration_date or datetime.now(),
        )

        await self.medicament_repository.update(
            medicament_id=request.id, medicament=new_medicament
        )

        return f"Medicament with id {request.id} updated successfully"
