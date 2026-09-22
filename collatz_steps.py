# if number is even divide by 2 and number is odd add + 
# for example: calculate steps to reach 1 from n number 
# let n = 5
# (5+1) = 6, (6/2) = 3, (3+1) = 4, (4/2) = 2, (2/2) = 1
# 5, 3, 4, 2, 1

n = int(input())
steps = 0
while n != 1:
    if n % 2 == 0:
        n //=2
    else:
        n = 3 * n + 1
    steps += 1
print(steps)