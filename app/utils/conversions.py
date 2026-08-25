def acres_to_hectares(acres):

    if acres <= 0:
        raise ValueError(
            "Acres must be greater than zero."
        )

    return acres * 0.404686