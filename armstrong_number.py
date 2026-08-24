def is_armstrong(num):
  temp = num
  num_digits = len(str(num))
  digit_sum = 0
  while temp > 0:
    digit = temp % 10
    digit_sum += digit ** num_digits
    temp //= 10
  return num == digit_sum

is_armstrong(153)
