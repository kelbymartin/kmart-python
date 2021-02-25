#------------ import space ---------------------
import math

#--------------- function, constant etc space -----------------
PI = math.pi
E = math.e

def function1():
    pass

#-------------- main function space -------------------------
#runs if file is run directly
if __name__ == "__main__":
    print("According to Python internals, the name of the file is currently:", __name__)

#always executed (on imports)
print("According to Python internals, the name of the file is currently:", __name__)