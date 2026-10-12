import pytest

from src.inventory import Inventory


def test_inventory_starts_empty():
    assert Inventory().stock == {}


def test_add_stock_accumulates_quantities():
    inventory = Inventory()
    inventory.add_stock('widget', 3)
    inventory.add_stock('widget', 4)

    assert inventory.stock['widget'] == 7


def test_remove_stock_decreases_quantity():
    inventory = Inventory()
    inventory.add_stock('widget', 5)
    inventory.remove_stock('widget', 2)

    assert inventory.stock['widget'] == 3


def test_remove_all_stock_leaves_zero():
    inventory = Inventory()
    inventory.add_stock('widget', 2)
    inventory.remove_stock('widget', 2)

    assert inventory.stock['widget'] == 0


@pytest.mark.parametrize('name', ['widget', 'unknown'])
def test_remove_stock_rejects_insufficient_quantity(name):
    inventory = Inventory()
    inventory.add_stock('widget', 2)

    with pytest.raises(ValueError, match='not enough stock'):
        inventory.remove_stock(name, 3)