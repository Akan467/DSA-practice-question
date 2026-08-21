def sum_of_digits(n):
  total = 0
  while n > 0:
    digits = n % 10
    total = total + digits
    n = n // 10
  return total

sum_of_digits(123)
