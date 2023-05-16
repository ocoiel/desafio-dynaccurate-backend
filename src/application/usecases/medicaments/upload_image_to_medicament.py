from src.application.repositories.medicament_repository import MedicamentRepository


class UploadIamgeToMedicamentUseCase:
    """Use case to upload a image to a existing medicament"""

    def __init__(self, medicament_repository: MedicamentRepository) -> None:
        self.medicament_repository = medicament_repository

    async def execute(self, medicament_id: str, image_url: str) -> None:
        await self.medicament_repository.upload_image(medicament_id, image_url)
