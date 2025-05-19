# order.py
from customer import Customer

class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

    
    def get_customer(self):
        return self._customer

    def set_customer(self, value):
        if isinstance(value, Customer):
            self._customer = value
        else:
            raise Exception("Customer must be an instance of the Customer class.")

    customer = property(get_customer, set_customer)

    
    def get_coffee(self):
        return self._coffee

    def set_coffee(self, value):
        from coffee import Coffee
        if isinstance(value, Coffee):
            self._coffee = value
        else:
            raise Exception("Coffee must be an instance of the Coffee class.")

    coffee = property(get_coffee, set_coffee)

    
    def get_price(self):
        return self._price

    def set_price(self, value):
        if isinstance(value, float) and 1.0 <= value <= 10.0:
            self._price = value
        else:
            raise Exception("Price must be a float between 1.0 and 10.0.")

    price = property(get_price, set_price)
