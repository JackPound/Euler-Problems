# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# def is_prime(number_to_check):
#   for x in range (2, number_to_check):
#     if (number_to_check % x == 0):
#       print('is not prime')
#       return
#   else:
#     return number_to_check

# is_prime(197)

  
def get_factors(number_to_factor):
  largest_factor = 0
  while largest_factor < number_to_factor:
    for x in range (2, number_to_factor):
      if (number_to_factor % x == 0):
        while number_to_factor % x == 0:
          largest_factor = x
          print(largest_factor)
          number_to_factor = number_to_factor / x
  print('largest factor is :', largest_factor)

get_factors(600851475143)