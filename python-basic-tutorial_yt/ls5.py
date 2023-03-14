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


# タイプアノテーション・・強制力はほとんどない

def total_price_1item(unit_price: int, quantity: int = 1)-> int:
    total_price = unit_price * quantity
    return f'{total_price}円'

total_price = total_price_1item(130, 1)
print(total_price)


# datetimeモジュール

from datetime import date

t = date.today()
print(t)

d = date(2022, 12, 24)
print(d.weekday())

from datetime import time
t = time(12, 15, 30, 0)
print(t)

from datetime import datetime, timedelta

n = datetime.now()
print(n)

d1 = datetime(2020, 12, 25, 0, 0, 0)
d2 = datetime(2020, 11, 25, 0, 0, 0)
result = d1 - d2
print(result)
print(result.days) #30

d3 = d1 + timedelta(days=10)
print(d3)

from datetime import timezone

JST = timezone(timedelta(hours=+9))
result = datetime(2020, 1, 1, 12, 15, 30, tzinfo=JST)
print(result)

import jpholiday

holidays = jpholiday.year_holidays(2023)
print(holidays)