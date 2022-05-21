import urllib.request

# 使用 handler 訪問百度

url = 'https://www.baidu.com'

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

# 獲取 handler 對象
handler = urllib.request.HTTPSHandler()

# 獲取 opener 對象
opener = urllib.request.build_opener(handler)

# 調用 open 方法
response = opener.open(request)

content = response.read().decode('UTF-8')
print(content)
