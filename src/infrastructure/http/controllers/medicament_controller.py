from fastapi import APIRouter, status

from src.infrastructure.http.dtos.create_medicament_dto import CreateMedicamentRequest
from src.infrastructure.http.dtos.update_medicament_dto import UpdateMedicamentRequest

from src.application.usecases.medicaments.create_medicament import (
    CreateMedicamentUseCase,
)
from src.application.usecases.medicaments.find_all_medicament import (
    FindAllMedicamentUseCase,
)
from src.application.usecases.medicaments.find_medicament_by_id import (
    FindByIdMedicamentUseCase,
)
from src.application.usecases.medicaments.update_medicament import (
    UpdateMedicamentUseCase,
)
from src.application.usecases.medicaments.delete_medicament import (
    DeleteMedicamentUseCase,
)


medicament_router = APIRouter(prefix="/med", tags=["med"])


class MedicamentController:
    """Controller"""

    def __init__(
        self,
        create_medicament: CreateMedicamentUseCase,
        find_all_medicament: FindAllMedicamentUseCase,
        find_by_id_medicmanet: FindByIdMedicamentUseCase,
        update_medicament: UpdateMedicamentUseCase,
        delete_medicamente: DeleteMedicamentUseCase,
    ):
        self.create = create_medicament
        self.find_all = find_all_medicament
        self.find_by_id = find_by_id_medicmanet
        self.update = update_medicament
        self.deleteUseCase = delete_medicamente
        self.router = APIRouter()
        self.router.add_api_route("/create", self.create_medicament, methods=["POST"])
        self.router.add_api_route("/", self.find_all_medicament, methods=["GET"])
        self.router.add_api_route(
            "/{medicament_id}", self.find_medicament_by_id, methods=["GET"]
        )
        self.router.add_api_route(
            "/{medicament_id}/update", self.update_medicament, methods=["PUT"]
        )
        self.router.add_api_route(
            "/{medicament_id}/delete", self.delete_medicament, methods=["DELETE"]
        )

    @medicament_router.post(
        "/create",
        status_code=status.HTTP_201_CREATED,
    )
    async def create_medicament(self, medicament: CreateMedicamentRequest):
        """Create medicament"""
        return await self.create.execute(medicament)

    @medicament_router.get(
        "/",
        status_code=status.HTTP_200_OK,
    )
    async def find_all_medicament(self):
        """Find all medicament"""
        return await self.find_all.execute()

    @medicament_router.get(
        "/{medicament_id}",
        status_code=status.HTTP_200_OK,
    )
    async def find_medicament_by_id(self, medicament_id: str):
        """Find medicament by id"""
        return await self.find_by_id.execute(medicament_id)

    @medicament_router.put(
        "/{medicament_id}/update",
        status_code=status.HTTP_201_CREATED,
    )
    async def update_medicament(self, medicament: UpdateMedicamentRequest):
        """Update medicament"""
        return await self.update.execute(medicament)

    @medicament_router.delete(
        "{medicament_id}/delete",
        status_code=status.HTTP_200_OK,
    )
    async def delete_medicament(self, medicament_id: str):
        """Delete medicament"""
        return await self.deleteUseCase.execute(medicament_id)
