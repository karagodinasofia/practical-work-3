
def eta_hours(distance_km, express):
    if distance_km < 0:
        raise ValueError("Distance cannot be negative")

    hours = 24 + int(distance_km // 100)

    if express:
        hours = max(hours / 2, 4)

    return hours
