import pandas as pd

from app.data.weather import get_historical_weather


latitude = float(input("Enter farm latitude: "))
longitude = float(input("Enter farm longitude: "))

weather = get_historical_weather(latitude, longitude)


# Calculate climate statistics
average_temperature = weather["temperature_2m_mean"].mean()
average_max_temperature = weather["temperature_2m_max"].mean()
average_min_temperature = weather["temperature_2m_min"].mean()
annual_rainfall = weather["precipitation_sum"].sum()
annual_et0 = weather["et0_fao_evapotranspiration"].sum()


print("\nAGROAI FARM CLIMATE PROFILE")
print("=" * 40)

print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")

print("\nTEMPERATURE")
print(f"Average: {average_temperature:.2f} °C")
print(f"Average maximum: {average_max_temperature:.2f} °C")
print(f"Average minimum: {average_min_temperature:.2f} °C")

print("\nRAINFALL")
print(f"Annual rainfall: {annual_rainfall:.2f} mm")

print("\nWATER")
print(f"Annual reference ET0: {annual_et0:.2f} mm")


# Calculate monthly rainfall
weather["month"] = pd.to_datetime(weather["time"]).dt.month

monthly_rainfall = (
    weather
    .groupby("month")["precipitation_sum"]
    .sum()
)

print("\nMONTHLY RAINFALL")
print("=" * 40)

for month, rainfall in monthly_rainfall.items():
    print(f"Month {month}: {rainfall:.1f} mm")


# Save raw weather data
weather.to_csv(
    "data/raw/weather/farm_weather_2025.csv",
    index=False
)

print("\nWeather data saved successfully.")