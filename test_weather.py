import pandas as pd
from app.models.farm import Farm
from app.utils.conversions import acres_to_hectares

from app.config import (
    DEFAULT_START_DATE,
    DEFAULT_END_DATE
)


from app.data.weather import get_historical_weather

from app.services.weather_service import (
    clean_weather_data,
    calculate_climate_summary
)


latitude = float(input("Enter farm latitude: "))
longitude = float(input("Enter farm longitude: "))

farm_id = input("Enter farm ID: ")

acres = float(
    input("Enter farm area in acres: ")
)

area_hectares = acres_to_hectares(acres)

irrigation_input = input(
    "Does the farm have irrigation? (yes/no): "
).lower()

irrigation = irrigation_input == "yes"


farm = Farm(
    farm_id=farm_id,
    latitude=latitude,
    longitude=longitude,
    area_hectares=area_hectares,
    irrigation=irrigation
)

weather = get_historical_weather(
    latitude,
    longitude,
    DEFAULT_START_DATE,
    DEFAULT_END_DATE
)


weather = clean_weather_data(weather)

summary = calculate_climate_summary(weather)


print("\nFARM INFORMATION")
print("=" * 40)

print(f"Farm ID: {farm.farm_id}")

print(
    f"Area: "
    f"{farm.area_hectares:.2f} hectares"
)

print(
    f"Irrigation: "
    f"{'Yes' if farm.irrigation else 'No'}"
)

print("\nAGROAI FARM CLIMATE PROFILE")
print("=" * 40)

print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")

print("\nTEMPERATURE")

print(
    f"Average: "
    f"{summary['average_temperature']:.2f} °C"
)

print(
    f"Average maximum: "
    f"{summary['average_max_temperature']:.2f} °C"
)

print(
    f"Average minimum: "
    f"{summary['average_min_temperature']:.2f} °C"
)

print("\nRAINFALL")

print(
    f"Annual rainfall: "
    f"{summary['annual_rainfall']:.2f} mm"
)

print("\nWATER")

print(
    f"Annual reference ET0: "
    f"{summary['annual_et0']:.2f} mm"
)


# Monthly rainfall
weather["month"] = weather["time"].dt.month

monthly_rainfall = (
    weather
    .groupby("month")["precipitation_sum"]
    .sum()
)

print("\nMONTHLY RAINFALL")
print("=" * 40)

for month, rainfall in monthly_rainfall.items():
    print(f"Month {month}: {rainfall:.1f} mm")


# Save data
weather.to_csv(
    "data/raw/weather/farm_weather_2025.csv",
    index=False
)

print("\nWeather data saved successfully.")