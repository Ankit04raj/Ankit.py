#5q> create a class called order which stores item & its price.
# use Dunder function __gt__() to cover that
# order1 > order2 if prive of order1 > prive of order2

class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,ord2):
        return self.price > ord2.price
    
ord1 = Order("chips",20)
ord2 = Order("tea",12)
print(ord1 > ord2)   #True