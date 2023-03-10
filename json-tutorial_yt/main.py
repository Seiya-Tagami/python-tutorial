# 送信
import json
obj = {'user': 'サプー', 'hobby':['読書', 'プログラミング']}
json_text = json.dumps(obj, ensure_ascii=False)
print(json_text)

# 読み込み
text = '{"id":123, "is_student": true}'
obj2 = json.loads(text)
print(obj2)