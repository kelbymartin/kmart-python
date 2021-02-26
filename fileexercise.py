#using variable
with open('fileexercise.txt', 'r') as f:
   orig = f.read().strip()

with open('fileexercise.txt', 'w') as f:
    f.write("write in:\n")
    f.write("new line 1\n")
    f.write("new line 2\n")

with open('fileexercise.txt', 'a') as f:
    f.write(orig)


#using list
# text = []
# with open('fileexercise.txt', 'r') as f:
#     for line in f:
#         text.append(line)

# with open('fileexercise.txt', 'w') as f:
#     f.write("write in:\n")
#     f.write("new line 1\n")
#     f.write("new line 2\n")

# with open('fileexercise.txt', 'a') as f:
#     for line in text:
#         f.write(str(line))