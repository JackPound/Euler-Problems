# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def add_numbers(big):
  total_number = 0
  for x in range (1, big):
    if (x % 3 == 0 or x % 5 == 0):
      total_number = total_number + x
  else:
    print(total_number)
add_numbers(1000)