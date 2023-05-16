from fastapi import HTTPException
from src.application.repositories.medicament_repository import MedicamentRepository
from src.infrastructure.database.prisma.mappers.prisma_medicament_mapper import (
    PrismaMedicamentMapper,
)
from src.infrastructure.database.prisma.prisma_connection import Prisma
from src.domain.entities.medicament import Medicament


class PrismaMedicamentRepository(MedicamentRepository):
    def __init__(self, prisma: Prisma):
        self.prisma = prisma

    async def create(self, medicament: Medicament):
        raw = PrismaMedicamentMapper.to_prisma(medicament)
        await self.prisma.medicament.create(
            data={
                "name": raw.name,
                "id": raw.id,
                # "created_at": raw.created_at,
                "description": raw.description,
                "status": raw.status,
                "priority": raw.priority,
                "expiration_date": raw.expiration_date,
                "image_url": raw.image_url,
                "price": raw.price,
                # "updated_at": raw.updated_at,
            }
        )

    async def upload_image(self, medicament_id: str, image_url: str):
        await self.prisma.medicament.update(
            where={"id": medicament_id}, data={"image_url": image_url}
        )

    async def find_all(self):
        """Mapper in each medicament to domain layer"""
        medicaments = await self.prisma.medicament.find_many()

        return medicaments

    async def find_by_id(self, medicament_id: str):
        medicament = await self.prisma.medicament.find_unique(
            where={"id": medicament_id}
        )

        if not medicament:
            return None

        return PrismaMedicamentMapper.to_domain(raw=medicament)

    async def update(self, medicament_id: str, medicament: Medicament):
        raw = PrismaMedicamentMapper.to_prisma(medicament)
        try:
            hasMed = await self.prisma.medicament.find_unique(
                where={"id": medicament_id}
            )

            if not hasMed:
                raise HTTPException(detail="Medicament not found", status_code=404)
            else:
                await self.prisma.medicament.update(
                    where={"id": medicament_id},
                    data={
                        "name": raw.name,
                        "id": medicament_id,
                        "price": raw.price,
                        "description": raw.description,
                        "status": raw.status,
                        "priority": raw.priority,
                        "image_url": raw.image_url,
                        "expiration_date": raw.expiration_date,
                    },
                )
                return f"Medicament {medicament_id} updated"
        except Exception as e:
            print(e)

    async def delete(self, medicament_id: str):
        try:
            hasMed = await self.prisma.medicament.find_unique(
                where={"id": medicament_id}
            )

            print("koe n eh possivel")

            if not hasMed:
                raise HTTPException(detail="Medicament not found", status_code=404)
            else:
                await self.prisma.medicament.delete(where={"id": medicament_id})
                return f"Medicament {medicament_id} deleted"
        except Exception as e:
            print(e)
