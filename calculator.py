def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def power(x, y):
    return x ** y

ch = int(input("1-add 2-sub 3-mult 4-div 5-pow : "))
x = int(input("Number: "))
y = int(input("Number: "))

if ch == 1:
    print(add(x,y))
elif ch == 2:
    print(subtract(x,y))
elif ch == 3:
    print(multiply(x,y))
elif ch == 4:
    print(divide(x,y))
elif ch == 5:
    print(power(x,y))
else:
    print("You goofed")