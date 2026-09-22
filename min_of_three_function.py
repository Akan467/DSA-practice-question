def min_of_three(a, b, c):
    smallest = a
    if b < smallest:
        smallest = b
    if c < smallest:
        smallest = c 
    return smallest

a = int(input())
b = int(input())
c = int(input())
print("Min: " + str(min_of_three(a, b, c)))