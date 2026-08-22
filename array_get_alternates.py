def getAlternates(arr):
  skip = []
  for i in range(0, len(arr), 2):
    skip.append(arr[i])
  return skip
