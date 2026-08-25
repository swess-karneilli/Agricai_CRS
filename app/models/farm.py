from dataclasses import dataclass


@dataclass
class Farm:

    farm_id: str

    latitude: float

    longitude: float

    area_hectares: float

    irrigation: bool

    def __post_init__(self):

        if not -90 <= self.latitude <= 90:
            raise ValueError(
                "Latitude must be between -90 and 90."
            )

        if not -180 <= self.longitude <= 180:
            raise ValueError(
                "Longitude must be between -180 and 180."
            )

        if self.area_hectares <= 0:
            raise ValueError(
                "Farm area must be greater than zero."
            )