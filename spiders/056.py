import urllib.request

url = 'https://www.google.com/'

# url 的組成
# 協議 http, https
# 主機/域名 www.google.com
# port號 http: 80 , https: 443
# 路徑
# 參數
# 錨點 #

# UA
# user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36
headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}
# 請求對象的訂製
# 關鍵字傳參
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

# 獲取響應內容
content = response.read().decode('UTF-8')

print(content)
