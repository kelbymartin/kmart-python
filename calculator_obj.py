import math

class Calculator():
    last = 0
    mem = []

    def add(self, x, y):
        self.last = (x + y)
        self.add_mem(self.last)
        return self.last

    def subtract(self, x, y):
        self.last = (x - y)
        self.add_mem(self.last)
        return self.last

    def multiply(self, x, y):
        self.last = (x * y)
        self.add_mem(self.last)
        return self.last

    def divide(self, x, y):
        self.last = (x / y)
        self.add_mem(self.last)
        return self.last

    def power(self, x, y):
        self.last = (x ** y)
        self.add_mem(self.last)
        return self.last
    
    def root(self, x):
        self.last = math.sqrt(x)
        self.add_mem(self.last)
        return self.last

    def get_last(self):
        return self.last
    
    def add_mem(self, value):
        if len(self.mem) < 5:
            self.mem.append(value)
        else:
            self.mem.pop(0)
            self.mem.append(value)
    
    def get_mem(self):
        return self.mem
    
    def clear_mem(self):
        self.mem.clear()
        


calc = Calculator()
while True:
    #User input
    ch = int(input("1-add 2-sub 3-mult 4-div 5-pow 6-root 7-viewlast 8-viewmem 9-clearmem 0-exit : "))
    #Calculator logic
    #Output
    if ch == 1:
        x = int(input("Number: "))
        y = int(input("Number: "))
        print(calc.add(x,y))
    elif ch == 2:
        x = int(input("Number: "))
        y = int(input("Number: "))
        print(calc.subtract(x,y))
    elif ch == 3:
        x = int(input("Number: "))
        y = int(input("Number: "))
        print(calc.multiply(x,y))
    elif ch == 4:
        x = int(input("Number: "))
        y = int(input("Number: "))
        print(calc.divide(x,y))
    elif ch == 5:
        x = int(input("Number: "))
        y = int(input("Number: "))
        print(calc.power(x,y))
    elif ch == 6:
        x = int(input("Number: "))
        print(calc.root(x))
    elif ch == 7:
        print(calc.get_last())
    elif ch == 8:
        print(calc.get_mem())
    elif ch == 9:
        calc.clear_mem()
    elif ch == 0:
        break
    else:
        print("You goofed")