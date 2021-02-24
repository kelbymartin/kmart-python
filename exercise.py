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
n = 22
if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 5 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")
else:
    print("Somehow missed")