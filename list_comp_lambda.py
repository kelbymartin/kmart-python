l = [1, 2, 3, 4, 5, 6, 7, 8]

#Original
for elem in l:
    if elem >= 5:
        print(elem)

#List comprehension
[print(elem) for elem in l if elem >= 5]

#Generator
(print(elem) for elem in l if elem >= 5)


#Lambda
lambda x: x**2
# == 
#def square(x)
#   return x**2

print(list(map(lambda x: x**2, l)))