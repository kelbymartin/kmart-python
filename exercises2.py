#squares
# n = int(input("Enter number: "))
# for i in range(n):
#     print(i**2)

#print fib less than 1000
n1 = 0
n2 = 1
print(n1)
print(n2)
while n2 < 1000:
    temp = n1 + n2
    n1 = n2
    n2 = temp
    if(n2 < 1000):
        print(n2)

#warmup
# n = int(input("Enter number of scores: "))
# i = 0
# # highest = 0
# ru = 0
# scores = []
# while i < n:
#     score = int(input("Enter score: "))
#     # if score > highest:
#     #     ru = highest
#     #     highest = score
#     # elif score > ru:
#     #     ru = score
#     scores.append(score)
#     i += 1
# def runner(scores):
#     scores.sort(reverse=True)
#     highest = scores[0]
#     for i in scores:
#         if i < highest:
#             return i
# print("Runner-up:", runner(scores))