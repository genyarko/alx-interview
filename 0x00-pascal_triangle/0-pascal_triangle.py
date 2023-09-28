#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""
def pascal_triangle(n):
  """Returns a list of lists of integers representing the Pascal’s triangle of `n`.
  Returns an empty list if `n <= 0`.

  Args:
    n: An integer.

  Returns:
    A list of lists of integers, representing the Pascal’s triangle of `n`.
  """

  if n <= 0:
    return []

  triangle = [[1]]
  for i in range(1, n):
    row = [0] * (i + 1)
    for j in range(i + 1):
      if j == 0 or j == i:
        row[j] = 1
      else:
        row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    triangle.append(row)
  return triangle

