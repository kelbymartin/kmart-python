import math

def center_zeroes(array):
    i = 0
    zcount = 0
    while i < len(array):
        if array[i] == 0:
            zcount += 1
            array = array[0:int(math.floor(len(array)) / 2 + (zcount / 2))]
            array.append(0)
            array.append(array[math.floor(len(array)) / 2 + (zcount / 2):])
        i += 1
    print(array)

#test arrays: [0, 3, 1], [1, 1, 3, 0], [1, 1, 3, 0, 6, 0]
arrays = [[0, 3, 1], [1, 1, 3, 0], [1, 1, 3, 0, 6, 0]]
for array in arrays:
    center_zeroes(array)
#result:
