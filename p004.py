# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
def largest_pal(up_to):
  largest = 0
  my_list = []
  for x in range (1, up_to +1):
    for y in range (1, up_to + 1):
      xy = x * y
      my_list.append(xy)
  my_list.sort()
  my_list = list(set(my_list))
  for x in my_list:
    x = str(x)
    half = len(x)//2
    is_palindrome = True
    for y in range (half):
      if x[y] != x[-1*(y+1)]:
        is_palindrome = False
        break
    if is_palindrome:
      x = int(x)
      if x > largest:
        largest = x
  print(largest)
      
largest_pal(999)

