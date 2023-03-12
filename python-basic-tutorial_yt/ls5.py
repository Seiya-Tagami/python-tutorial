# map関数
x = [0, -20, 9.1, 7]

def twice(num):
    return num * 2

# result = list(map(twice, x))
# result = list(map(lambda num : num * 2, x))
result = list(map(abs, x))
print(result)

# filter関数
x = [30, -20, 9, 7]

def is_multiple_3(num):
    return num % 3 == 0

# r = list(filter(is_multiple_3, x))
r = list(filter(lambda n:n%3 == 0, x))
print(r)

# reduce関数
from functools import reduce

x = [4, 10, 3, 2]

def multiply(a, b):
    return a * b

result = reduce(multiply, x)
print(result) #240