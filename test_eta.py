
import pytest

from eta import eta_hours


def test_standard_delivery_zero_km():

    distance = 0
    express = False

    result = eta_hours(distance, express)

    assert result == 24


def test_standard_delivery_250_km():
    distance = 250
    express = False

    result = eta_hours(distance, express)

    assert result == 26


def test_express_delivery_250_km():
    distance = 250
    express = True

    result = eta_hours(distance, express)

    assert result == 13


def test_distance_boundary_100_km():
    distance = 100
    express = False

    result = eta_hours(distance, express)

    assert result == 25


def test_negative_distance_raises_error():
    distance = -10
    express = False

    with pytest.raises(ValueError):
        eta_hours(distance, express)
