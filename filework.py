

# file = open('generictext.txt', 'r')
# print(file.read())
# file.close()

# with open('generictext.txt', 'r') as f:
    #print(f.read(2)) #param = num of chars to read
    # print(f.readlines())
    # print(f.readline().strip())
    # print(f.readline().strip())

with open('generictext.txt', 'a') as f:
    f.write("\nanother line")


