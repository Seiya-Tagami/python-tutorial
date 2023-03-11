def average_calc(x, y):
    print('２つの数の平均を計算する処理です。')
    avg = (x + y) / 2
    diff = x - y
    return avg, diff

result1, result2 = average_calc(12, 32)
print(result1, result2)

# メモ化・・使うケースは余り多くはないが、再帰を使ったアルゴリズム・動的計画法でメモ化が役に立つことがある
from functools import cache

@cache
def func1(num):
    print(f'関数が呼ばれました。引数${num}')
    return (num + 10) / 3

r1 = func1(110)
r2 = func1(113)
r3 = func1(110) # 同じ引数で再度呼び出された場合は保存しておいた過去のデータを返す
print([r1, r2, r3])

# example フィボナッチ数列
# fib_list = []

# fib_listを使わなくとも、メモ化してしまえば保存した値で計算可能
@cache
def fibonacci(i):
    if i == 0 or i == 1:
        return i
    else:
        return fibonacci(i - 1) +fibonacci(i - 2)

r = fibonacci(34)
print(r)
# for n in range(35):
#     fib_num = fibonacci(n, fib_list)
#     fib_list.append(fib_num)

# print(fib_list[-1])
# print(fib_list)

# クラス
class Student:
    # イニシャライザー
    def __init__(self, arg_name):
        self.name = arg_name

    def print_text(self):
        print(self.name)

student1 = Student('サプー1')
student1.print_text()

student2 = Student('サプー2')
student2.print_text()