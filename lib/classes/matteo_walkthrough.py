from statistics import mean
from statistics import StatisticsError

class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("names must be strings")
        elif len(name) < 3:
            raise ValueError("names must be longer than 2 chars")
        elif hasattr(self, "name"):
            raise AttributeError("Names cannot be reset")
        else:
            self._name = name

    def orders(self):
        return [
            order
            for order in Order.all
            if order.coffee is self
        ]

    def customers(self):
        return list({
            order.customer
            for order in self.orders()
        })

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        try:
            return mean([order.price for order in self.orders()])
        except StatisticsError:
            return 0
        except ValueError:
            return "Value is incorrect"

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("names must be strings")
        elif not 1 <= len(name) <= 15:
            raise ValueError("names must be within 1.0 <= name <= 10.0")
        else:
            self._name = name

    def orders(self):
        return [order for order in Order.all if order.customer is self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

class Order:
    all = [] #! class attribute
    
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if not isinstance(price, float):
            raise TypeError("Prices must be floats")
        elif not 1.0 <= price <= 10.0:
            raise ValueError("Prices must be within 1.0 <= price <= 10.0")
        elif  hasattr(self, "price"):
            raise AttributeError("Prices cannot be reset")
        else:
            self._price = price
            
    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Customers must be Customer")
        else:
            self._customer = customer

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        if not isinstance(coffee, Coffee):
            raise TypeError("coffees must be Coffee")
        else:
            self._coffee = coffee