import urllib.parse
import urllib.request

# urlencode
# 多參數的時候

# https://www.google.com/search?q=松尾美佑&nogizaka=四期生

data = {
  'q': '松尾美佑',
  'nogizaka': '四期生'
}

a = urllib.parse.urlencode(data)
print(a)

url = 'https://www.google.com/search?' + a
print(url)

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}
# 請求對象的訂製
# 關鍵字傳參
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('UTF-8')

print(content)
