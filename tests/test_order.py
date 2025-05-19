import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_valid():
    customer = Customer("Eli")
    coffee = Coffee("Macchiato")
    order = Order(customer, coffee, 3.5)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 3.5

def test_order_invalid_price():
    customer = Customer("Finn")
    coffee = Coffee("Cortado")

    with pytest.raises(Exception):
        Order(customer, coffee, 0.5)  # Too low

    with pytest.raises(Exception):
        Order(customer, coffee, 15.0)  # Too high
