import numpy as np
def second_maximum(array):
    if len(array) < 2:
        raise ValueError('Array must contain atleast two element.')
    if array[0] > array[1]:
        max1 = array[0]
        max2 = array[1]
    else:
        max2 = array[0]
        max1 = array[1]

    for i in range(2, len(array)):
        if array[i] > max1:
            max2 = max1
            max1 = array[i]

        elif array[i] > max2:
            max2 = array[i]
    
    return max2

array = [24, 34, 21, 90, 56]
x = second_maximum(array)
print(x)
