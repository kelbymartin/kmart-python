nums = [0, 1, 2, "red", 3, 4, 5]

#for loops
#for i in nums:
#    print(i)

for elem in nums:
    if type(elem) == str:
        continue
    print(elem)


#range loop
#for i in range(5,20,2):
#    print(i)

#while
#i = 0
#while i < 10:
#    print(i)
#    i += 1

#while True:
#    i += 1
#    print(i)
#    if i > 10:
#        break