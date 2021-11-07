class Pizza:
    __slots__ = ['price', 'cheese', 'meats', 'veggies']
    def __init__(self):
        self.price = 5.0
        self.cheese = 's'
        self.meats = set()
        self.veggies = set()
pizza = Pizza()

class Topping:
    __slots__ = ['code', 'name', 'price']

    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

_CHEESES = {'f': Topping('f', 'Fresh Mozzeralla', 1.5), 's': Topping('s', 'Shredded Cheese', 1.0), 'c': Topping('c', 'Cheddar Cheese', 0.5)}
_MEATS = {}
_VEGGIES = {}
def print_pizza(pizza):
    print("One pizza with", _CHEESES[pizza.cheese].name, end = ',')
    for meat in pizza.meats:
        name = _MEATS[meat].name
        if name != 'None':
            print (name, end= ',')
    for veggie in pizza.veggies:
        name = _VEGGIES[veggie].name
        if name != 'None':
            print(name, end= ",")
    print('\b\b : $', round(pizza.price, 2), sep = '')
def main():
    pizza = Pizza()
    print_pizza(pizza)
    #menu = Topping()
    #print(pizza)
main()