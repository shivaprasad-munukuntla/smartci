import pytest

from src.pricing import add_tax, apply_discount


@pytest.mark.parametrize(
    ('price', 'percent', 'expected'),
    [
        (100, 0, 110.0),
        (100, 100, 0.0),
        (19.99, 20, 15.99),
        (10, 12.34, 8.77),
    ],
)
def test_apply_discount(price, percent, expected):
    assert apply_discount(price, percent) == expected


@pytest.mark.parametrize('percent', [-0.01, 100.01])
def test_apply_discount_rejects_percent_outside_range(percent):
    with pytest.raises(ValueError, match='percent must be between 0 and 100'):
        apply_discount(100, percent)


def test_add_tax_uses_default_rate():
    assert add_tax(100) == 118.0


@pytest.mark.parametrize(
    ('price', 'rate', 'expected'),
    [
        (0, 0.18, 0.0),
        (100, 0, 100.0),
        (10, 0.1234, 11.23),
    ],
)
def test_add_tax_with_rate_boundaries_and_rounding(price, rate, expected):
    assert add_tax(price, rate) == expected