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


# 例外処理

x = 1
y = 0

try:
    result = x / y
except ZeroDivisionError as e:
    print('ゼロで割ることはできません。')
    print(e)
except NameError as e:
    print('変数が定義されていません')
    print(e)
else:
    print(result)
    print('正常に終了しました')
finally:
    print('割り算が終了しました。')