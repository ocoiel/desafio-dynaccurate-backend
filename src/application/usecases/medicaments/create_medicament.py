from src.application.repositories.medicament_repository import MedicamentRepository
from src.domain.entities.medicament import Medicament
from src.infrastructure.http.dtos.create_medicament_dto import CreateMedicamentRequest


class CreateMedicamentUseCase:
    """Use case to create a new medicament."""

    def __init__(self, medicament_repository: MedicamentRepository):
        self.medicament_repository = medicament_repository

    async def execute(self, request: CreateMedicamentRequest) -> Medicament:
        medicament = Medicament(
            name=request.name,
            description=request.description,
            status=request.status,
            priority=request.priority,
            price=request.price,
            image_url=request.image_url,
            expiration_date=request.expiration_date,
        )

        await self.medicament_repository.create(medicament)

        return medicament
