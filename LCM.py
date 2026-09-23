# lcm = a * b // gcd(a, b)
# gcd: a, b = b, a % b

a = int(input())
b = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b

    return a

lcm = a * b // gcd(a, b)
print("LCM: " + str(lcm))