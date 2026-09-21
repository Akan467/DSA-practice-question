day = int(input())
names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

if 1 <= day <= 7:
    print(names[day-1])
else:
    print("Invalid")