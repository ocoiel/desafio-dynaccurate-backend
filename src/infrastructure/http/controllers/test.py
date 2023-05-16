# pylint: disable = ["W0212"]
from PIL import Image
from io import BytesIO
from fastapi import APIRouter, HTTPException, File, status
from fastapi_pagination import Page, paginate
from src.domain.entities.medicament import Medicament
from src.infrastructure.http.dtos.create_medicament_dto import CreateMedicamentRequest
from src.infrastructure.http.dtos.update_medicament_dto import UpdateMedicamentRequest
from src.infrastructure.database.prisma.prisma_connection import PrismaConnection

from src.infrastructure.database.prisma.repositories.prisma_medicament_repository import (
    PrismaMedicamentRepository,
)

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
from src.application.usecases.medicaments.upload_image_to_medicament import (
    UploadIamgeToMedicamentUseCase,
)

medicament_router = APIRouter(prefix="/med", tags=["med"])

prisma_connection = PrismaConnection()

repo = PrismaMedicamentRepository(prisma=prisma_connection.client)

create = CreateMedicamentUseCase(repo)
upload = UploadIamgeToMedicamentUseCase(repo)
find_all = FindAllMedicamentUseCase(repo)
find_by_id = FindByIdMedicamentUseCase(repo)
update = UpdateMedicamentUseCase(repo)
delete = DeleteMedicamentUseCase(repo)


# Talvez eu deva colocar prisma._connect() no aquivo de server.py
@medicament_router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
)
async def create_medicament(medicament: CreateMedicamentRequest):
    """Create medicament"""
    await prisma_connection.connect()
    return await create.execute(medicament)


@medicament_router.put(
    "/{medicament_id}/upload-image", status_code=status.HTTP_201_CREATED
)
# changing type of file from UplaodFile (FastAPI) to bytes (instrisic)
async def upload_image(medicament_id: str, file: bytes = File(...)):
    """Upload image"""
    await prisma_connection.connect()

    image = Image.open(BytesIO(file))

    # ignore
    extension = image.format.lower()

    print(f"EXTENSION: {extension}")

    image.save(f"uploads/{medicament_id}.{extension}")

    file_path = f"uploads/{medicament_id}.{extension}"

    image_url = f"http://localhost:3334/{file_path}"

    print(f"File path: {file_path}")

    await upload.execute(medicament_id, image_url)

    if not update_medicament:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Medicament not found",
        )

    return {"url": image_url}


@medicament_router.get(
    "/", status_code=status.HTTP_200_OK, response_model=Page[Medicament]
)
async def find_all_medicament():
    """Find all medicament"""
    await prisma_connection.connect()

    all_medicaments = await find_all.execute()

    return paginate(all_medicaments)


@medicament_router.get(
    "/{medicament_id}",
    status_code=status.HTTP_200_OK,
)
async def find_medicament_by_id(medicament_id: str):
    """Find medicament by id"""
    await prisma_connection.connect()
    return await find_by_id.execute(medicament_id)


@medicament_router.put(
    "/{medicament_id}/update",
    status_code=status.HTTP_201_CREATED,
)
async def update_medicament(medicament: UpdateMedicamentRequest):
    """Update medicament"""
    await prisma_connection.connect()
    return await update.execute(medicament)


@medicament_router.delete(
    "/{medicament_id}/delete",
    status_code=status.HTTP_200_OK,
)
async def delete_medicament(medicament_id: str):
    """Delete medicament"""
    await prisma_connection.connect()

    return await delete.execute(medicament_id)
