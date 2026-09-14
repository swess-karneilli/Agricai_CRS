import pandas as pd
def add_month_column(weather):
    """
    adds a month column to the weather dataset.
    """
    weather=weather.copy()
    weather["time"]=pd.to_datetime(weather["time"])
    weather["month"]=weather["time"].dt.month
    return weather


def calculate_rainfall_features(weather):
    """
    calculates rainfall features
    """
    annual_rainfall = (weather["precipitation_sum"].sum()
    )

    monthly_rainfall = (weather.groupby("month")["precipitation_sum"].sum()
    )

    monthly_rainfall_mean = (monthly_rainfall.mean()
    )

    monthly_rainfall_std = (monthly_rainfall.std()
    )

    if monthly_rainfall_mean > 0:

        rainfall_variability = (monthly_rainfall_std / monthly_rainfall_mean
        )
    else:
        rainfall_variability = 0

    return {
        "annual_rainfall": annual_rainfall,
        "monthly_rainfall_mean": monthly_rainfall_mean,
        "monthly_rainfall_std": monthly_rainfall_std,
        "rainfall_variability": rainfall_variability
    }

def calculate_temperature_features(weather):
    """
    Calculate temperature-related features.
    """

    return {
        "avg_temperature": (
            weather[
                "temperature_2m_mean"
            ].mean()
        ),

        "avg_max_temperature": (
            weather[
                "temperature_2m_max"
            ].mean()
        ),

        "avg_min_temperature": (
            weather[
                "temperature_2m_min"
            ].mean()
        ),

        "absolute_max_temperature": (
            weather[
                "temperature_2m_max"
            ].max()
        ),

        "absolute_min_temperature": (
            weather[
                "temperature_2m_min"
            ].min()
        )
    }


def calculate_water_features(weather):
    """
    Calculate basic water-related climate indicators.
    """

    annual_et0 = (
        weather[
            "et0_fao_evapotranspiration"
        ].sum()
    )

    annual_rainfall = (
        weather[
            "precipitation_sum"
        ].sum()
    )

    rainfall_et0_balance = (
        annual_rainfall - annual_et0
    )

    return {
        "annual_et0": annual_et0,

        "rainfall_et0_balance":
            rainfall_et0_balance
    }


def calculate_dry_spell_features(
    weather,
    rainfall_threshold=1.0
):
    """
    Calculate the longest consecutive dry period.

    A day with rainfall below the threshold
    is considered dry.
    """

    rainfall = (
        weather["precipitation_sum"]
        .fillna(0)
    )

    dry_days = (
        rainfall < rainfall_threshold
    )

    max_dry_spell = 0
    current_dry_spell = 0

    for is_dry in dry_days:

        if is_dry:

            current_dry_spell += 1

            max_dry_spell = max(
                max_dry_spell,
                current_dry_spell
            )

        else:

            current_dry_spell = 0

    return {
        "maximum_dry_spell_days":
            max_dry_spell
    }


def build_climate_features(weather):
    """
    Build all climate features from
    the weather dataset.
    """

    weather = add_month_column(
        weather
    )

    rainfall_features = (
        calculate_rainfall_features(
            weather
        )
    )

    temperature_features = (
        calculate_temperature_features(
            weather
        )
    )

    water_features = (
        calculate_water_features(
            weather
        )
    )

    dry_spell_features = (
        calculate_dry_spell_features(
            weather
        )
    )

    features = {}

    features.update(
        rainfall_features
    )

    features.update(
        temperature_features
    )

    features.update(
        water_features
    )

    features.update(
        dry_spell_features
    )

    return features
            