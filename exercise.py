#q1
# for i in range(1,8):
#     print(i)

# i = 1
# while i < 8:
#     print(i)
#     i += 1

#q2 = 100
# x = 0
# while x < 100:
#     x += 2
# print(x)

#q3
def weird_conditions(n):
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 5 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")
    else:
        print("Somehow missed")

#test cases: 1, 2, 3, 4, 6, 8, 11, 18, 20
tests = [1, 2, 3, 4, 6, 8, 11, 18, 20]
for i in tests:
    weird_conditions(i)
#results: Weird, Not Weird, Weird, Not Weird,
# Weird, Weird, Weird, Weird, Weird