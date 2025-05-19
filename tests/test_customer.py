import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_initialization_valid():
    customer = Customer("Regina")
    assert customer.name == "Regina"

def test_customer_initialization_invalid():
    with pytest.raises(Exception):
        Customer("")  # Empty name

    with pytest.raises(Exception):
        Customer("A" * 16)  # Name too long

def test_customer_create_order():
    customer = Customer("Kariuki")
    coffee = Coffee("Espresso")
    order = customer.create_order(coffee, 5.0)
    assert isinstance(order, Order)
    assert order.customer == customer
    assert order.coffee == coffee

def test_customer_coffees():
    customer = Customer("Clara")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Mocha")
    customer.create_order(coffee1, 3.0)
    customer.create_order(coffee2, 4.0)
    assert coffee1 in customer.coffees()
    assert coffee2 in customer.coffees()

def test_most_aficionado():
    coffee = Coffee("Americano")
    regina = Customer("Regina")
    kariuki = Customer("Kariuki")
    regina.create_order(coffee, 3.0)
    kariuki.create_order(coffee, 4.0)
    kariuki.create_order(coffee, 5.0)
    assert Customer.most_aficionado(coffee) == kariuki
