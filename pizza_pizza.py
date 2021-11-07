def counter(x,y,z):
    x = 5
    y = 4
    z = 1
    count = int(x)+int(y)+int(z)
    print(count)
    return count
counter(5,4,1)
class Pizza:
    __slots__ = ['price', 'cheese', 'meats', 'veggies']
    def __init__(self): # cheese, meats, veggies)
        self.price = 5.0
        self.cheese = 'c' #cheese #
        self.meats = 'm' #set() #meats #
        self.veggies = 'v' #set() #veggies #
        print(self.price)
        return None
        #print(self.price, self.cheese, self.meats, self.veggies)
        #return self.price, self.cheese, self.meats, self.veggies
pizza = Pizza()
print(pizza.price)
print(pizza.meats, ":", pizza.price)
class Topping:
    __slots__ = ['code', 'name', 'price']

    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price
        #print(self.code, self.name, self.price)
        #return self.code, self.name, self.price
_CHEESES = {'f': Topping('f', 'Fresh Mozzeralla', 1.50), 's': Topping('s', 'Shredded Cheese', 1.0), 'c': Topping('c', 'Cheddar Cheese', 0.50)}
#print(dict(_CHEESES))
_MEATS = {'p': Topping('p', 'Pepperoni', 1.0), 's': Topping('s', 'Sausage', 0.75), 'm': Topping('m', 'Meatballs', 0.50)}
_VEGGIES = {'m': Topping('m', 'Mushroom', 1.0), 'bp': Topping('bp','Bell Peppers', 1.0), 'jp': Topping('jp', 'Jalapeno peppers', 1.0), 'p': Topping('p', 'Pineapple', 1.50), 'n': Topping('n', 'None', 0.0)}
#print(_CHEESES)
#topping = Topping(_CHEESES)
#print(topping)
def menu_plan(menu):
    if menu == 'O' or menu == 'o':
        print('Cheese Options: ')
        print(_CHEESES['f'])
        print(_CHEESES['s'])
        print(_CHEESES['c'])
        #print(topping.name)
        #print(_CHEESES[topping.name])
        #print(_CHEESES[.name(Topping.code): Topping.price])
        op1 = input('Choose one type of cheese: ')
        if op1 == 'f' or op1 == 's' or op1 == 'c':
            print(op1)
        #meat_dish = input('Choose your meats: ')
        print('Meat Options: ')
        print(_MEATS['p'])
        print(_MEATS['s'])
        print(_MEATS['m'])
        #print(_MEATS['p', 's', 'm'])
        #print(_MEATS[topping.name(topping.code): topping.price])
        op2 = input('Choose your meats: ')
        print(op2)
        #veggie_dish = input('Choose your veggies: ')
        print('Veggie Options: ')
        print(_VEGGIES['m'])
        print(_VEGGIES['bp'])
        print(_VEGGIES['jp'])
        print(_VEGGIES['p'])
        print(_VEGGIES['n'])
        #print(_VEGGIES[topping.name(topping.code): topping.price])
        op3 = input('Choose your veggies: ')
        print(op3)
        print('For your second pizza ...')
        s_op1 = input('Choose one type of cheese (o for options): ')
        s_op2 = input('Choose your meats: ')
        s_op3 = input('Choose your veggies: ')
    print(op1, op2, op3, s_op1, s_op2, s_op3)
    #return op1, op2, op3, s_op1, s_op2, s_op3
def print_pizza(pizza):
    print("One pizza with", _CHEESES[pizza.cheese].name,end = ',') #pizza.cheese
    f_amount = print('$', round(pizza.price, 2), sep = '' )
    #print(f_amount, sep = '' )
    print("One pizza with",_CHEESES[pizza.cheese].name, _MEATS[pizza.cheese].name, _VEGGIES[pizza.cheese].name, end = ',')
    s_amount = print('$', round(pizza.price, 2), sep = '' )
    #print(s_amount, sep = '')
    t_amount = int(f_amount) + int(s_amount)
    print('Total price is ',t_amount)
#    for meat in pizza.meats:
#        name = _MEATS[meat].name
#        if name != 'None':
#            print (name, end= ',')
#    for veggie in pizza.veggies:
#        name = _VEGGIES[veggie].name
#        if name != 'None':
#            print(name, end= ",")
    #f_amount = print('\b\b : $', round(pizza.price, 2), sep = '')
def main():
    print("Welcome to Papa Joe's Pizza Factory, where all orders include two pizzas!")
    print('For your first pizza ...')
    menu = input('Choose one type of cheese (O for options): ')
    menu_plan(menu)
    pizza = Pizza()
    print('Your order is: ')
    print_pizza(pizza)
    #menu = Topping()
    #print(pizza)
main()