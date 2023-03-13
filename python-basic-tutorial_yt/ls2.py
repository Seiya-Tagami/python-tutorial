# if文　bool値について
x = 10
y= 9
if x == 10:
    print('これは10です')
elif x == 9:
    print('これは9です')
else:
    print('これは10ではありません')

print(x >= 10 or y >= 9)
print(x >= 10 and not y >= 10)


# 三項演算子
age = 18
result = '成人' if age >= 20 else '子供' if age >= 1 else '赤ちゃん'
print(result)


# セイウチ演算子・代入式
x = list(range(3))
if(n:=len(x)) >= 10:
    print('listが長すぎます')

print(f'n:{n}')

import re

s='合計金額は1200円です'
if(m:=re.search(r'[0-9]+円', s)):
    print(m.group())


# for文
for t in range(10):
    print('Pythonプログラミング Vtuber サプー')

x_list = [10, 22, 70, -2]
for val in x_list:
    x_twice = val * 2
    print(x_twice)

x_dict = {'りんご': 150, 'バナナ': 300, 'オレンジ': 100}
for k, v in x_dict.items():
    print(k, v)

# リスト内包表記
names = ['斎藤', '山田', '田中']
Names = [i + 'さん' for i in names]
print(Names)

arr = [i for i in range(11) if i % 2 == 0]
print(arr)

arr = ['き' if i%2==1 else i for i in range(11)]
print(arr)