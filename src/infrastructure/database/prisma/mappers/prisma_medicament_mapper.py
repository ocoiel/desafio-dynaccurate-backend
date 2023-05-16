from prisma.models import Medicament as RawMedicament
from pydantic import UUID4
from src.domain.entities.medicament import Medicament


class PrismaMedicamentMapper:
    """
    Mappers are used to define how the data is visualized in the response.
    And converting the response to Prisma layer
    Disclaimer: There are the diffence between App Layer (Entitie Notification)
    and Persistent Layer (Prisma and Database)

    Martin Fowler Blog: https://martinfowler.com/eaaCatalog/dataMapper.html
    """

    @staticmethod
    def to_prisma(medicament: Medicament):
        return RawMedicament(
            id=str(medicament.id),
            name=medicament.name,
            price=medicament.price,
            description=medicament.description,
            status=medicament.status,
            priority=medicament.priority,
            expiration_date=medicament.expiration_date,
            image_url=medicament.image_url,
            created_at=medicament._created_at,
            updated_at=medicament._updated_at,
        )

    @staticmethod
    def to_domain(raw: RawMedicament) -> Medicament:
        medicament = Medicament(
            id=UUID4(raw.id),
            name=raw.name,
            price=raw.price,
            description=raw.description,
            status=raw.status,
            priority=raw.priority,
            expiration_date=raw.expiration_date,
            image_url=raw.image_url,
            _created_at=raw.created_at,
            _updated_at=raw.updated_at,
        )

        return medicament
