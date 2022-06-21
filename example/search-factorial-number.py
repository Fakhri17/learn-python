def print_factors(n, i):
  if (i <= n):
    if (n % i == 0):
      print(i, end = " ");
    print_factors(n, i + 1);

num = 5
print("factor dari",num,"adalah:")
print_factors(num, 1)