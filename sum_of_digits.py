# Using Digit Extraction
def sum_of_digits(n):
  total = 0
  while n > 0:

    # Extract the last digit
    last = n % 10
    sum += last

    # Remove the last digit
    n = n // 10
  return last

sum_of_digits(123)


## using recursion
def sumofdigit(n):
  # base case
  if n == 0:
    return 0
  # recursive case
  return n % 10 + sumofdigit(n // 10)

## using string conversion
def sumofdigits(n):
  s = str(n)
  sum = 0
  for ch in s:
    sum += int(ch)
  return sum 
