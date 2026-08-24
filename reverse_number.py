# 1st way to convert into list 
def reverseDigits(n):
  s = str(n)
  s = list(s)
  s.reverse()
  s = ''.join(s)
  n = int(s)
  return n

# 2nd way using string slicing in python
def reverseDigits(n):
  s = str(n)
  s = s[::-1]
  n = int(s)
  return n

# 3rd way reversing digit by digit
n = 4562 
rev = 0
while (n > 0):
  a = n % 10
  rev = rev * 10 + a
  n = n // 10
print(rev)
