import urllib.parse
import urllib.request
import json

url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)
print(request)

response = urllib.request.urlopen(request)
# POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type str.

# 獲取響應內容
content = response.read().decode('UTF-8')
print(content)

print(type(content))
# <class 'str'>

# str -> json
obj = json.loads(content)
print(obj)

fp = open('move.json', 'w', encoding='UTF-8')
fp.write(content)
