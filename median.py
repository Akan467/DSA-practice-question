def findMedian(arr):
  n = len(arr)
  arr.sort()
  result = 0
  if n % 2 == 0:
    result = (arr[n // 2] + arr[(n // 2) -1]) // 2
  else:
    result = arr[n // 2]
  return result
