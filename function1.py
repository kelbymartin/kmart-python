
def weird_arithmetic(x, y, z):
    output = ((x**x + y**z) // z )
    #print(output)
    return output

#result = weird_arithmetic(5, 6, 7)
#print("weird_arithmetic result:", result)

def custom_greeting(greeting, name):
    print(greeting + " " + name)

#custom_greeting("Hi", "Jeff")


r = 4
h = 10

def area_circle(radius):
    return (3.14 * radius**2)

def vol_cylinder(area, height):
    print(area * height)

c_area = area_circle(r)
vol_cylinder(c_area, h)
#print("Radius:", r)
#print("Height:", h)
#print("Area:", c_area)
#print("Volume of Cylinder:", result)