# 2. Fix (optional for frontend candidates)
# Improve this function:
import functools

def my_function(data):
  ss, s, n = functools.reduce(lambda a, b: map(sum, zip(a,b)), [(x*x, x, 1) for x in data])
  return (ss - s*s/n) / n


# print(my_function([]))                        # error
# print(my_function([1]))                         # 0
# print(my_function([1, 2]))                      # 0
# print(my_function([1, 2, 3]))                   # 0
# print(my_function([1, 2, 3, 4]))                # 1
# print(my_function([1, 2, 3, 4, 5]))             # 2
# print(my_function([1, 2, 3, 4, 5, 6]))          # 3
# print(my_function([1, 1, 1, 2, 2, 2]))          # 0
# print(my_function([5, -3, 30, 20, 12, -2]))     # 140


# ******************************************************************************
# concepts to understand in function above:
# 1) multi line assignment
# Ex 1: 
a, b, c = 1, 2, 3
# print(a, b, c)            #=> (1, 2, 3)

# Ex 2: 
# a, b, c = 1, 2            #=> Error, need more than 2 values to unpack

# Ex 3: 
# a, b  , c = 1, 2, 3, 4    #=> Error, too many values to unpack

# Ex 4:
a, b, c = [ 1, 2, 3 ]    
# print(a, b, c)            #=> (1, 2, 3)


# ******************************************************************************
# 2) functools.reduce(fun, seq[, initializer])
# parameters:
#   fun = function / callback
#   seq = iteratable ex. array / list
#   initializer = optional paramater will be used as first param of function
# returns:
#   single result. first two elements in seq are passed into function and result
#   is saved.
#   then same function is applied to previous result and the element after the
#   second element. the result is saved. This process is repeated throughout
#   the array
# notes: 
#   - similar to JavaScript array.reduce()
#
# Ex 1: use reduce to compute sum of list
array = [ 1, 3, 5 ]
# print(functools.reduce(lambda a, b: a + b, array))    #=> 9


# ******************************************************************************
# 3) lambda arguments : expression
# - an anonymous function (i.e. not named)
# - takes in any number of arguments, but only has one expression
# - similar to callback functions, except they are anonymous (callbacks
#   can be named functions)
#
# Ex 1: double or tripple 
def coolFunction(n):                # returns lambda function
  return lambda a : a * n

myDoubler = coolFunction(2)
print(myDoubler(5))                 #=> 10
print(myDoubler(11))                #=> 22
print(coolFunction(3)(5))           #=> 15
print(coolFunction(3)(11))          #=> 33

# Ex 2:
print((lambda a, b : a + b)(1, 2))  #=> 3
print((lambda a, b : a + b)(2, 2))  #=> 4


# ******************************************************************************
# 4) map(fun, iter)
# parameters:
#   fun = function / callback
#   iter = iteratable ex. array / list
# returns:
#   a map object (iterator)
# notes
#   - similar to JS array.map(callback)
#
# Ex 1: double all numbers in array
nums = [ 1, 3, 5 ]
print(map(lambda a : a * 2, nums))    #=> [ 2, 6, 10 ]
print(nums)                           #=> [ 1, 3, 5 ]


# ******************************************************************************
# 5) sum(iter[, start])
# parameters:
#   iter = iterable. ex list / tuples of numbers
#   start = optional number to start sum with, if not provided, first element
#           of iterable is used
#
# Ex 1: sum all numbers in list
nums = [ 1, 3, 5 ]
print (sum(nums))                    #=> 9


# ******************************************************************************
# 6) zip( iter1, iter2, ... )
# returns a zip object (iterator of tuples)
#
# Ex 1:
a = (1, 2, 3)
b = (4, 5, 6)
x = zip(a, b)
print(x)        #=> [(1, 4), (2, 5), (3, 6)]

# Ex 2:
a = (1, 2)      # iter w/ less length determines length of each tuple
b = (3, 4, 5)   # iter w/ more elements than other iter is ignored
x = zip(a, b)
print(x)        #=> [(1, 3), (2, 4)]

# Ex 3:
a = (1, 2)
b = (3, 4)   
c = (5, 6)
x = zip(a, b, c)
print(x)        #=> [ (1, 3, 5), (2, 4, 6) ]


# ******************************************************************************
# 7) for _ in __
#    _ = element (can name this anything)
#    __ = iterable (ex. list)
#
# Ex 1: loop through list
pantry = [ "mango", "apple" ]
for ele in pantry:
  print(ele)

# Ex 2: List Comprehension
# [ expression for _ in __ ]
# returns iterable
nums = [ 1, 2, 3 ]
print([ num * 2 for num in nums ])   #=> [ 2, 4, 6 ]


# ******************************************************************************
# 8) Tuples
# - immutable
# - hashable (use it as a key)
# https://www.tutorialspoint.com/python/python_tuples.htm
#
# Ex 1:
x = (1, 2, 3)





# ******************************************************************************
# 2. Fix (optional for frontend candidates)
# Improve this function:
from functools import reduce

# Ex. data == [ 1, 2, 3 ]
def my_function(data):

  # original code:
  # ss, s, n = reduce(lambda a, b: map(sum, zip(a,b)), [(x*x, x, 1) for x in data])
  # print(ss, s, n)                               #=> 14, 6, 3

  # the right part of the reducing function (i.e. the sequence) is the input 
  #   data transformed into the following:
  # transformed = [(x*x, x, 1) for x in data]     # O(N) TIME, N = input data length
  transformed = [[x*x, x, 1] for x in data]     # O(N) TIME, N = input data length
  # print(transformed)                          #=> [ (1, 1, 1), (4, 2, 1), (9, 3, 1) ]

  # the left part of the reducing function performs basic addition
  # [ (1, 1, 1), (4, 2, 1), (9, 3, 1) ]          => [ 14, 6, 3 ]
  # 
  #   (1, 1, 1)
  #   (4, 2, 1)
  # + (9, 3, 1)
  # -----------
  #   14, 6, 3

  result = reduce(lambda a, b: [ (a[0] + b[0]), (a[1] + b[1]), (a[2] + b[2]) ], transformed)
  # print(result)                                   #=> [14, 6, 3]

  total = transformed[0]
  # total = [1, 1, 1]

  # loop through transformed
  idx = 1
  while idx < len(transformed):
    total[0] += transformed[idx][0]
    total[1] += transformed[idx][1]
    total[2] += transformed[idx][2]
    idx += 1
  # print(total)      #=> [14, 6, 3]

  ss, s, n = total

  # print(s * s / n)                              #=> 6 * 6/3 => 12
  # print(ss - s*s/n)                             #=> 14 - 12 => 2
  # print((ss - s*s/n) / n)                       $=> 2/3     => 0

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


myData = [ 1, 2, 3 ]
transformed = [ (x*x, x, 1) for x in myData ]     # O(N) TIME, N = list length
# print(transformed)                      #=> [ (1, 1, 1), (4, 2, 1), (9, 3, 1) ]


# lambda a, b: map(sum, zip(a, b))
# takes in two iterables, returns iterable
def myLambda(a, b):
  zipResult = zip(a, b)                   # O(3) => O(1) TIME, bec, limited to length of a or b
  # print(zipResult)                      #=> [ (1, 4), (1, 2), (1, 1) ]

  # x = map(sum, zip(a, b))               # O(3) => O(1) TIME
  x = map(sum, zipResult)                 # sum numbers in each tuple in zip result
  # x == [ 5, 3, 2 ]

  return x

# print(zip((1, 1, 1), (4, 2, 1)))        #=> [ (1, 4), (1, 2), (1, 1)]
# print(myLambda((1, 1, 1), (4, 2, 1)))   #=> [ 5, 3, 2 ]
# print(myLambda([5, 3, 2], (9, 3, 1)))   #=> [ 14, 6, 3 ]

