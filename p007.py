# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?
def is_prime(number_to_check):
  prime = True
  for x in range (2, number_to_check):
    if number_to_check % x == 0:
      prime = False
      break
  return prime

def prime_position(at_position):
  prime_list = []
  count = 2
  while len(prime_list) < at_position:
    if is_prime(count):
      prime_list.append(count)
      count += 1
    else:
      count += 1
  print(prime_list[-1])

prime_position(10001) 