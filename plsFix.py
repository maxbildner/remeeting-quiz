# 2. Fix (optional for frontend candidates)
# Improve this function:
from functools import reduce

# Original function
def function(data):
  ss, s, n = reduce(lambda a, b: map(sum, zip(a,b)), [(x*x, x, 1) for x in data])
  return (ss - s*s/n) / n


# My Solution 
# O(N) Worst Case Time Complexity, N = input data list length
# O(1) Space Complexity
def my_function(data):

  # initialize total as an array with 3 numbers, using first number in data list
  total = [ data[0]*data[0], data[0], 1 ]   # O(1) TIME Complexity

  # loop through data list
  idx = 1
  while idx < len(data):                    # O(N) TIME Complexity, N = input list length
    total[0] += data[idx] * data[idx]
    total[1] += data[idx]
    total[2] += 1
    idx += 1

  # multivariable assignment              
  ss, s, n = total                          # O(1) TIME Complexity

  return (ss - s*s/n) / n


# print(my_function([]))                          # error
# print(my_function([1]))                         # 0
# print(my_function([1, 2]))                      # 0
# print(my_function([1, 2, 3]))                   # 0
# print(my_function([3, 2, 1]))                   # 0
# print(my_function([1, 2, 3, 4]))                # 1
# print(my_function([1, 2, 3, 4, 5]))             # 2
# print(my_function([1, 2, 3, 4, 5, 6]))          # 3
# print(my_function([6, 5, 4, 3, 2, 1]))          # 3
# print(my_function([1, 1, 1, 2, 2, 2]))          # 0
# print(my_function([2, 2, 2, 1, 1, 1]))          # 0
# print(my_function([5, 1, 1, 1, 1, 1]))          # 2
# print(my_function([5, -3, 30, 20, 12, -2]))     # 140