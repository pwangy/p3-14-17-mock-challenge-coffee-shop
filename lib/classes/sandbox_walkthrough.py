class Coffee:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >=3 and not hasattr(self, "_name") :
            self._name = name
        else:
            raise AttributeError('coffee name must be a string with char length of 3 or greater AND attribute already exists')

    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        pass

    def num_orders(self):
        pass

    def average_price(self):
        pass


class Customer:
    def __init__(self, name):
        self.name = name

    def orders(self):
        pass

    def coffees(self):
        pass

    def create_order(self, coffee, price):
        pass


class Order:
    
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee is not instance of Coffee class")
        self._coffee = coffee

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("customers is not instance of Customer class")
        self._customer = customer

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if not isinstance(price, float):
            raise ValueError("price must be a float value")
        self._price = price