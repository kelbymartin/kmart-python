import math

class Calculator():
    #history attributes
    last = 0
    mem = []

    #Calculator methods... Add, Subtract, Multiply, etc
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

    #History methods
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

### end of calculator class

if __name__ == "__main__":
    #Initialize calculator
    calc = Calculator()
    while True:
        #User input
        ch = 0
        try:
            ch = int(input("1-add 2-sub 3-mult 4-div 5-pow 6-root 7-viewlast 8-viewmem 9-clearmem 0-exit : "))
            #Calculator logic
            #Output
            if ch == 1:
                #User input
                x = float(input("Number: "))
                y = float(input("Number: "))
                #call calculator
                print(calc.add(x,y))
            elif ch == 2:
                #User input
                x = float(input("Number: "))
                y = float(input("Number: "))
                #call calculator
                print(calc.subtract(x,y))
            elif ch == 3:
                #User input
                x = float(input("Number: "))
                y = float(input("Number: "))
                #call calculator
                print(calc.multiply(x,y))
            elif ch == 4:
                #User input
                x = float(input("Number: "))
                y = float(input("Number: "))
                #call calculator
                print(calc.divide(x,y))
            elif ch == 5:
                #User input
                x = float(input("Number: "))
                y = float(input("Number: "))
                #call calculator
                print(calc.power(x,y))
            elif ch == 6:
                #User input
                x = float(input("Number: "))
                #call calculator
                print(calc.root(x))
            elif ch == 7:
                #call calculator
                print(calc.get_last())
            elif ch == 8:
                #call calculator
                print(calc.get_mem())
            elif ch == 9:
                #call calculator
                calc.clear_mem()
            elif ch == 0:
                break
            else:
                print("Use menu options")

        except ValueError:
            print("Not a number")