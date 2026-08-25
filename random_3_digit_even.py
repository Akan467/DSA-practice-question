import random

def main():
  number = random.randit(100, 999)
  if number == 999:
    number -= 1
  elif number % 2 != 0:
    number += 1
  print(number)

