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
