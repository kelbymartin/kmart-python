#using variable
with open('fileexercise.txt', 'r') as f:
   orig = f.read().strip()
#using array
# text = []
# with open('fileexercise.txt', 'r') as f:
#     for line in f:
#         text.append(line)

with open('fileexercise.txt', 'w') as f:
    f.write("write in:\n")
    f.write("new line 1\n")
    f.write("new line 2\n")

#using variable
with open('fileexercise.txt', 'a') as f:
    f.write(orig)
#using array
# with open('fileexercise.txt', 'a') as f:
#     for line in text:
#         f.write(str(line))