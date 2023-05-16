from src.domain.entities.medicament import Medicament


class MedicamentViewModel:
    """The MVVM patterns was created by John Gossman, software architect
    at at Microsoft, and this pattern is used normally in C# .NET ."""

    @staticmethod
    def to_http(medicament: Medicament):
        return {
            "id": medicament.id,
            "name": medicament.name,
            "price": medicament.price,
            "expiration_date": medicament.expiration_date,
            "image_url": medicament.image_url,
            "created_at": medicament.created_at,
            "updated_at": medicament.updated_at,
        }
