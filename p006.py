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