def printDiamond(n):
  space = n - 1
  for i in range(0, n):
    for j in range(0, space):
      print(" ", end="")
    for j in range(0, i + 1):
      print("* ", end = "")
    print()
    space -= 1
  for i in range(n, 0, -1):
    for j in range(0, space):
      print(" ", end="")
    for j in range(0, i):
      print("* ", end="")
    print()
    space += 1

printDiamond(5)
