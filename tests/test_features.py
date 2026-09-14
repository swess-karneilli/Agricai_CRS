from app.config import (
    DEFAULT_START_DATE,
    DEFAULT_END_DATE
)

from app.data.weather import (
    get_historical_weather
)

from app.services.weather_service import (
    clean_weather_data
)

from app.services.feature_engineering import (
    build_climate_features
)


latitude = 7.9276
longitude = -1.189


weather = get_historical_weather(
    latitude,
    longitude,
    DEFAULT_START_DATE,
    DEFAULT_END_DATE
)


weather = clean_weather_data(
    weather
)


features = build_climate_features(
    weather
)


print("\nCLIMATE FEATURES")
print("=" * 40)


for name, value in features.items():

    print(
        f"{name}: {value:.2f}"
    )