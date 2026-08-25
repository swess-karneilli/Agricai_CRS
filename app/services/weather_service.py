import pandas as pd


def clean_weather_data(weather):
    """Clean and validate weather data."""

    weather = weather.copy()

    # Convert date column
    weather["time"] = pd.to_datetime(weather["time"])

    # Remove duplicate dates
    weather = weather.drop_duplicates(subset=["time"])

    # Sort chronologically
    weather = weather.sort_values("time")

    # Check for missing values
    required_columns = [
        "temperature_2m_mean",
        "temperature_2m_max",
        "temperature_2m_min",
        "precipitation_sum",
        "et0_fao_evapotranspiration"
    ]

    for column in required_columns:

        if weather[column].isna().any():
            weather[column] = weather[column].interpolate()

    # Rainfall cannot be negative
    weather["precipitation_sum"] = (
        weather["precipitation_sum"].clip(lower=0)
    )

    # ET0 cannot be negative
    weather["et0_fao_evapotranspiration"] = (
        weather["et0_fao_evapotranspiration"].clip(lower=0)
    )

    return weather


def calculate_climate_summary(weather):

    summary = {
        "average_temperature": weather[
            "temperature_2m_mean"
        ].mean(),

        "average_max_temperature": weather[
            "temperature_2m_max"
        ].mean(),

        "average_min_temperature": weather[
            "temperature_2m_min"
        ].mean(),

        "annual_rainfall": weather[
            "precipitation_sum"
        ].sum(),

        "annual_et0": weather[
            "et0_fao_evapotranspiration"
        ].sum()
    }

    return summary