import pytest

from src.cart import Cart


def test_empty_cart_total_is_zero():
    assert Cart().total() == 0.0


def test_add_uses_default_quantity():
    cart = Cart()
    cart.add('widget', 10)

    assert cart.items == [('widget', 10, 1)]
    assert cart.total() == 11.8


def test_total_sums_quantities_and_items():
    cart = Cart()
    cart.add('widget', 10, 2)
    cart.add('gadget', 5, 3)

    assert cart.total() == 41.3


def test_total_applies_discount_before_tax():
    cart = Cart()
    cart.add('widget', 50, 2)

    assert cart.total(discount=10) == 106.2


def test_total_rejects_invalid_discount():
    cart = Cart()
    cart.add('widget', 10)

    with pytest.raises(ValueError, match='percent must be between 0 and 100'):
        cart.total(discount=101)