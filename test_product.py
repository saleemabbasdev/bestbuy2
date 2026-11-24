from products import Product
import pytest

def test_creating_prod():
    p = Product("MacBook Air M2", price=1450, quantity=100)
    assert p.name == "MacBook Air M2"
    assert p.price == 1450
    assert p.quantity == 100
    assert p.is_active()


def test_creating_prod_invalid_details():
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_prod_becomes_inactive():
    p = Product("MacBook Air M2", price=1450, quantity=1)
    p.buy(1)
    assert p.quantity == 0
    assert not p.is_active()


def test_buy_modifies_quantity():
    p = Product("MacBook Air M2", price=1450, quantity=100)
    total = p.buy(10)
    assert total == 14500.0
    assert p.quantity == 90


def test_buy_too_much():
    p = Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(ValueError):
        p.buy(101)