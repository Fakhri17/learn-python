def print_pascal_triangle(size):
  result = []
  for i in range(0, size):
    row = []
    for j in range(0, i + 1):
      row.append(decide_number(i, j))
    result.append(row)
  return result
 
def decide_number(n, k):
    num = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        num = num * (n - i)
        num = num // (i + 1)
    return num

rows = 7
for row in print_pascal_triangle(7):
  print(row)