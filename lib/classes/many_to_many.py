from statistics import StatisticsError
from statistics import mean

class Coffee: #has many orders
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        elif len(name) < 3:
            raise ValueError("Name must be 3 or more characters.")
        elif hasattr(self, "name"):
            raise AttributeError("Coffee names cannot be reset.")
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
            return "Value is incorrect!"


class Customer: #has many orders
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        elif not 1 <= len(name) <= 15:
            raise ValueError("Names must be between 1 and 15 characters.")
        else:
            self._name = name

    def orders(self):
        return [order for order in Order.all if order.customer is self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)


class Order: # an order can belong to a customer and a coffee
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
                raise TypeError("Prices must be floats.")
            elif not 1.00 <= price <= 10.00:
                raise ValueError("Price must be between $1.00-$10.00!")
            elif hasattr(self, "price"):
                raise AttributeError("Prices cannot be reset.")
            else:
                self._price = price

        @property
        def customer(self):
            return self._customer

        @customer.setter
        def customer(self, customer):
            if not isinstance(customer, Customer):
                raise TypeError("customers must be Customer!")
            else:
                self._customer = customer

        @property
        def coffee(self):
            return self._coffee

        @coffee.setter
        def coffee(self, coffee):
            if not isinstance(coffee, Coffee):
                raise TypeError("coffees must be Coffee.")
            else:
                self._coffee = coffee
