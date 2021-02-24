import math

def center_zeroes(array):
    i = 0
    while i < len(array):
        if i <= math.floor(len(array) / 2):
            if array[i] == 0:
                temp = array[i + 1]
                array[i + 1] = array[i]
                array[i] = temp
        else:
            if array[i] == 0:
                temp = array[i - 1]
                array[i - 1] = array[i]
                array[i] = temp
        i += 1
    print(array)

#test arrays: [0, 3, 1], [1, 1, 3, 0], [1, 1, 3, 0, 6, 0]
arrays = [[0, 3, 1], [1, 1, 3, 0], [1, 1, 3, 0, 6, 0]]
for array in arrays:
    center_zeroes(array)
#result:
