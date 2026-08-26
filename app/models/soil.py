from dataclasses import dataclass


@dataclass
class SoilProfile:

    ph: float | None

    clay_percent: float | None

    sand_percent: float | None

    silt_percent: float | None

    organic_carbon: float | None