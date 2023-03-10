# x = 'あいうえお'
# y = 'かきくけこ'
# print(x + y)

x = ['y', 'x']
y = ['a', 'b', 'c']
# y[2] = 'C'
# result = y[2]

#リストの結合
y.extend(x)

# 破壊的メソッド　→消費リソースが非破壊的メソッドより少ない
x.append('z')
print(x)

x.sort() #紛らわしいソート処理　
print(x)

#非破壊的メソッド　→非破壊的メソッドは安全でおすすめ
user = "山本さん"
newUser = user.replace('さん', '様')
print(newUser)

hoge = sorted(x) #紛らわしいソート処理。
print(hoge)

# リストの分割
result = y[1:4]
result_len = len(result)
print(result)
print(result_len)

#辞書の扱い
a = {'りんご': 150, 'バナナ': 300, 'オレンジ': 100}
a['バナナ'] = 220
print(a)
