total = int(input("Enter total seconds: "))
h = total // 3600
print(f"{h} hours")
m = (total % 3600) // 60
print(f"{m} minutes")
s = total % 60
print(f"{s} seconds")