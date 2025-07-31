def multiply_matrix(A, B):
  C = [[0, 0], [0, 0]]
  C[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0]
  C[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1]
  C[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0]
  C[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1]
  return C


def matrix_power(x, p : int):
  if p == 1:
    return x

  if p % 2 == 0:
    half = matrix_power(x, p//2)
    return multiply_matrix(half, half)

  else:
    half = matrix_power(x, (p-1) // 2)
    squared_half = multiply_matrix(half, half)
    return multiply_matrix(squared_half, x)


def fibonachi(n):

  if(n <= 1):
    return n
  
  base = [[1, 1], [1, 0]]

  result_matrix = [[0,0], [0,0]]
  result_matrix = matrix_power(base, n-1)

  return result_matrix[0][0]
  
  