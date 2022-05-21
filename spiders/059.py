import urllib.parse
import urllib.request
import json

# urlencode
# 多參數的時候

url = 'https://fanyi.baidu.com/sug'
headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
}

data = {
  'kw': 'japan',
}

# post 請求必須進行編碼
data = urllib.parse.urlencode(data).encode('UTF-8')

request = urllib.request.Request(url=url, data=data, headers=headers)
print(request)

response = urllib.request.urlopen(request)
# POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type str.

# 獲取響應內容
content = response.read().decode('UTF-8')

print(content)
# {"errno":0,"data":[{"k":"Japan","v":"n. \u65e5\u672c"},
# {"k":"japan","v":"n. \u9ed1\u8272\u4eae\u6f06\uff0c\u65e5\u672c\u4eae\u6f06; \uff08\u65e5\u672c\u5f0f\uff09\u6f06\u5668 vt. \u5728\uff08\u5c24\u6307\u6728\u5236\u54c1\u6216\u91d1\u5c5e\u5236\u54c1\uff09\u4e0a\u6d82\u9ed1\u8272\u4eae\u6f06"},{"k":"JAPAN","v":"abbr. Japanese advanced processing architecture ne"},{"k":"Japanese","v":"n. \u65e5\u8bed; \u65e5\u672c\u4eba\uff0c\u65e5\u672c\u56fd\u6c11 adj. \u65e5\u8bed\u7684; \u65e5\u672c\u7684\uff0c\u65e5\u672c\u4eba\u7684"},
# {"k":"japanica","v":"[\u533b]\u65e5\u672c\u5c71\u8336\uff0c\u65e5\u672c\uff1f\uff1f"}]}

print(type(content))
# <class 'str'>

# str -> json
obj = json.loads(content)
print(obj)
