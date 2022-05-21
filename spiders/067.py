import urllib.request

# 代理
url = 'https://www.whatismyip.com.tw/tw/'

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

proxies = {
  'http': 'http://20.47.108.204'
}

# 獲取 handler 對象
handler = urllib.request.ProxyHandler(proxies=proxies)

# 獲取 opener 對象
opener = urllib.request.build_opener(handler)

# 調用 open 方法
response = opener.open(request)

content = response.read().decode('UTF-8')
print(content)

with open('067.html', 'w', encoding='UTF-8')as fp:
  fp.write(content)
