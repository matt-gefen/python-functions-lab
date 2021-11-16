# challenge 1
def sum_to(num):
  total = 0
  for i in range(1, num + 1):
    total += i
  return total

# challenge 2
def largest(lst):
  max = 0
  for i in lst:
    if i > max:
      max = i
  return max

## this is the easy way lol 
def also_largest(lst):
  return max(lst)

  