import requests
import pandas as pd

from app.config import WEATHER_API_URL


def validate_coordinates(latitude, longitude):
    """Validate latitude and longitude."""

    if not -90 <= latitude <= 90:
        raise ValueError("Latitude must be between -90 and 90.")

    if not -180 <= longitude <= 180:
        raise ValueError("Longitude must be between -180 and 180.")


def get_historical_weather(
    latitude,
    longitude,
    start_date,
    end_date
):
    """Retrieve historical weather data from Open-Meteo."""

    validate_coordinates(latitude, longitude)

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "daily": [
            "temperature_2m_mean",
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_sum",
            "et0_fao_evapotranspiration"
        ],
        "timezone": "auto"
    }

    try:
        response = requests.get(
            WEATHER_API_URL,
            params=params,
            timeout=30
        )

        response.raise_for_status()

    except requests.RequestException as error:
        raise ConnectionError(
            f"Unable to retrieve weather data: {error}"
        )

    data = response.json()

    if "daily" not in data:
        raise ValueError("Weather API returned no daily data.")

    weather = pd.DataFrame(data["daily"])

    return weather