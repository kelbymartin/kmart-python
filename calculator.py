def add(x, y):
    #code
    output = (x + y)
    return output

def subtract(x, y):
    #code
    output = (x - y)
    return output

def multiply(x, y):
    #code
    Output = (x * y)
    return Output

def divide(x, y):
    #code
    Output = (x / y)
    return Output

def power(x, y):
    #code
    output = (x ** y)
    return output

#User input
ch = int(input("1-add 2-sub 3-mult 4-div 5-pow : "))
x = int(input("Number: "))
y = int(input("Number: "))

#Calculator logic
#Output
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