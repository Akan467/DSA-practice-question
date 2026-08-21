def sumofmatrix(mat):
  total = 0
  n = len(mat)
  m = len(mat[0])
  for i in range(n):
    for j in range(m):
      total += mat[i][j]
  return total
