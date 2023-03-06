def average_calc(x, y):
    print('２つの数の平均を計算する処理です。')
    avg = (x + y) / 2
    diff = x - y
    return avg, diff

result1, result2 = average_calc(12, 32)
print(result1, result2)

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