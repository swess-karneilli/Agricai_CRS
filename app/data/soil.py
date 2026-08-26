from owslib.wcs import WebCoverageService


SOILGRIDS_WCS_URL = (
    "https://maps.isric.org/mapserv"
    "?map=/map/phh2o.map"
)


def get_soil_data(latitude, longitude):
    """
    Retrieve soil data for a farm location.

    Parameters
    ----------
    latitude : float
        Farm latitude.

    longitude : float
        Farm longitude.

    Returns
    -------
    dict
        Soil properties for the farm location.
    """

    # Validate coordinates
    if not -90 <= latitude <= 90:
        raise ValueError(
            "Latitude must be between -90 and 90."
        )

    if not -180 <= longitude <= 180:
        raise ValueError(
            "Longitude must be between -180 and 180."
        )

    # Connect to SoilGrids WCS
    wcs = WebCoverageService(
        SOILGRIDS_WCS_URL,
        version="2.0.1"
    )

    # For now, return the available WCS connection.
    # Actual soil extraction will be added next.
    return {
        "latitude": latitude,
        "longitude": longitude,
        "wcs_connected": True
    }