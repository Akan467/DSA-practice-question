def evenOddSum(arr):
  evenSum = 0
  oddSum = 0
  for i in range(len(arr)):
    if (i + 1) % 2 != 0:
      oddSum += arr[i]
  for i in range(len(arr)):
    if (i + 1) % 2 == 0:
      evenSum += arr[i]
  return [evenSum, oddSum]
