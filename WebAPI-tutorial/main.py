# 郵便番号検索API

import requests

res = requests.get('https://zipcloud.ibsnet.co.jp/api/search', params={'zipcode':'xxxxxxx'})

res_json = res.json()
results = res_json['results'][0]
address = results['address1'] + results['address2'] + results['address3'] + results['zipcode']
print(res.status_code)
print(address)