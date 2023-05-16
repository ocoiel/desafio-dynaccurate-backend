from abc import ABC, abstractmethod
from src.domain.entities.medicament import Medicament


class MedicamentRepository(ABC):
    @abstractmethod
    async def create(self, medicament: Medicament) -> Medicament:
        raise NotImplementedError

    @abstractmethod
    async def upload_image(self, medicament_id: str, image_url: str):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self) -> list[Medicament] | None:
        raise NotImplementedError

    @abstractmethod
    async def find_by_id(self, medicament_id: str) -> Medicament | None:
        raise NotImplementedError

    @abstractmethod
    async def update(self, medicament_id: str, medicament: Medicament) -> Medicament:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, medicament_id: str):
        raise NotImplementedError
