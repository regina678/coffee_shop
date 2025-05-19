import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from coffee import Coffee
from customer import Customer

def test_coffee_initialization_valid():
    coffee = Coffee("Cappuccino")
    assert coffee.name == "Cappuccino"

def test_coffee_initialization_invalid():
    with pytest.raises(Exception):
        Coffee("")  # Too short

def test_num_orders_and_average_price():
    coffee = Coffee("Latte")
    customer = Customer("Dora")
    customer.create_order(coffee, 4.0)
    customer.create_order(coffee, 6.0)
    assert coffee.num_orders() == 2
    assert coffee.average_price() == 5.0
