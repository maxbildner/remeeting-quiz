# 2. Fix (optional for frontend candidates)
# Improve this function:
import functools

def my_function(data):
  ss, s, n = functools.reduce(lambda a, b: map(sum, zip(a,b)), [(x*x, x, 1) for x in data])
  return (ss - s*s/n) / n


# print(my_function([]))                        # error
print(my_function([1]))                         # 0
print(my_function([1, 2]))                      # 0
print(my_function([1, 2, 3]))                   # 0
print(my_function([1, 2, 3, 4]))                # 1
print(my_function([1, 2, 3, 4, 5]))             # 2
print(my_function([1, 2, 3, 4, 5, 6]))          # 3
print(my_function([1, 1, 1, 2, 2, 2]))          # 0
print(my_function([5, -3, 30, 20, 12, -2]))     # 140


