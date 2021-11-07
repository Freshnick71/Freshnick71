class Pizza:
    __slots__ = ['price', 'cheese', 'meats', 'veggies']
    def __init__(self):
        self.price = 5.0
        self.cheese = 's'
        self.meats = set()
        self.veggies = set()

class Topping:
    __slots__ = ['code', 'name', 'price']

    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

def main():
    delicacy = Pizza()
    print(delicacy)
main()