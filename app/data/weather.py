import requests
import pandas as pd


def get_historical_weather(latitude, longitude):
    url = "https://archive-api.open-meteo.com/v1/archive"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": "2025-01-01",
        "end_date": "2025-12-31",
        "daily": [
            "temperature_2m_mean",
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_sum",
            "et0_fao_evapotranspiration"
        ],
        "timezone": "auto"
    }

    response = requests.get(url, params=params)

    response.raise_for_status()

    data = response.json()

    weather = pd.DataFrame(data["daily"])

    return weather