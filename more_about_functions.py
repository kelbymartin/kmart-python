PI = 3.14

def some_function(x, y, z):
    final = x + y + z
    return(final)

output = some_function(5, 6, 7)
#print output

def greet_friend(name, greeting, sentence):
    output = "{2}, {0}! {1}".format(greeting, name, sentence)
    return(output)
greeting = greet_friend("John", "Hi", "How are ya?")
#print greeting

def greet_user(greeting):
    user = input("Please enter your name: ")
    print("{}, {}!".format(greeting, user))

greet_user("Hello")