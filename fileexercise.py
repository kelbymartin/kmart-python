#using variable
# with open('fileexercise.txt', 'r') as f:
#    orig = f.read().strip()

# with open('fileexercise.txt', 'w') as f:
#     f.write("write in:\n")
#     f.write("new line 1\n")
#     f.write("new line 2\n")

# with open('fileexercise.txt', 'a') as f:
#     f.write(orig)


#using list
# with open('fileexercise.txt', 'r') as f:
#     text = f.readlines()

# with open('fileexercise.txt', 'w') as f:
#     f.write("write in:\n")
#     f.write("new line 1\n")
#     f.write("new line 2\n")

# with open('fileexercise.txt', 'a') as f:
#     for line in text:
#         f.write(str(line))


#using map to strip new lines exercise
with open('fileexercise.txt', 'r') as f:
    lines_list = list(map(lambda line: line.rstrip('\n'), f.readlines()))

with open('fileexercise.txt', 'w') as f:
    f.write("write in:\n")
    f.write("new line 1\n")
    f.write("new line 2\n")

with open('fileexercise.txt', 'a') as f:
    for line in lines_list:
        f.write(str(line) + "\n")
