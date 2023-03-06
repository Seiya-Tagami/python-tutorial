# x = 'あいうえお'
# y = 'かきくけこ'
# print(x + y)

x = ['x', 'y']
y = ['a', 'b', 'c']
# y[2] = 'C'
# result = y[2]

#リストの結合
y.extend(x)

# リストの分割
result = y[1:4]
result_len = len(result)
print(y)
print(result)
print(result_len)

#辞書の扱い
a = {'りんご': 150, 'バナナ': 300, 'オレンジ': 100}
a['バナナ'] = 220
print(a)

