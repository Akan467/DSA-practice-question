def isDigitSumPalindrome(n):
  sum = 0
  while n != 0:
    temp = (n % 10)
    sum += temp
    n //= 10
  s = str(sum)
  str_rev = s[::-1]
  return s == str_rev 
