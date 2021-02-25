import math

def center_zeroes(array):
    i = 0
    zcount = 0
    temparray = array
    while i < len(array):
        if array[i] == 0:
            array.pop(i)
            temparray = array[int(math.floor(len(array)) / 2 + (zcount / 2)):len(array)]
            array = array[0:int(math.floor(len(array)) / 2 + (zcount / 2))]
            array.append(0)
            array = array + temparray
            zcount += 1
        i += 1
    print(array)

#test arrays: [0, 3, 1], [1, 1, 3, 0], [1, 1, 3, 0, 6, 0]
arrays = [[0, 3, 1], [1, 1, 3, 0], [1, 1, 3, 0, 6, 0], [1, 0, 3, 0, 5, 0]]
for array in arrays:
    center_zeroes(array)
#result: [3, 0, 1], [1, 0, 1, 3], [1, 1, 0, 0, 3, 6]
