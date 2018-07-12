# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_squares(target):
  total_1 = 0
  total_2 = 0
  for x in range (1, target+1):
    total_1 = total_1 + (x*x)
    total_2 = total_2 + x
  total_2 = total_2**2
  print("sum of squares", total_1)
  print("square of sums", total_2)
  print("difference", total_2 - total_1)

sum_squares(100)