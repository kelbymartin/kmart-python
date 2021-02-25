try:
    user_int = int(input("Please give integer: "))
except ValueError:
    print("That is not an integer.")
except Exception:
    print("General exception")

print("End of program")