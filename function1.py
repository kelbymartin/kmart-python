
def weird_arithmetic(x, y, z):
    output = ((x**x + y**z) // z )
    #print(output)
    return output

result = weird_arithmetic(5, 6, 7)
print("weird_arithmetic result:", result)

def custom_greeting(greeting, name):
    print(greeting + " " + name)

#custom_greeting("Hi", "Jeff")