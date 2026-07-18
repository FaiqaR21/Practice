import pytest

def calculate_discount(price, discount_percentage):
    return price - (price * discount_percentage / 100)

def test_normal_discount():
    assert calculate_discount(1000, 20) == 800

def test_zero_discount():
    assert calculate_discount(1000, 0) == 1000

def test_full_discount():
    assert calculate_discount(1000, 100) == 0

def test_negative_values():
    assert calculate_discount(-1000, 20) == -800

def test_invalid_data_type():
    with pytest.raises(TypeError):
        calculate_discount("1000", 20)