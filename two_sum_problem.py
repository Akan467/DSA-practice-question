def sum(array, target):
    left = 0
    right = len(array)-1
    while (left < right):
        current_sum = array[left] + array[right]
        
        if (current_sum == target):
            return {left, right}
        elif (current_sum < target):
            left +=1
        else:
            right -= 1

    return current_sum

array = [1, 2, 3, 5, 7, 10, 11, 15]
target = 17
x = sum(array, target)
print(x)