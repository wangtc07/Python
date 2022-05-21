import urllib.parse
import urllib.request
import json

# url = 'https://blog.csdn.net/sxsssss/article/details/1070040131'
  # urllib.error.HTTPError: HTTP Error 404: Not Found

url = 'https://blog.wangtc.com/'
# urllib.error.URLError:

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}

try:
  request = urllib.request.Request(url=url, headers=headers)

  response = urllib.request.urlopen(request)

  # 獲取響應內容
  content = response.read().decode('UTF-8')
  print(content)
except urllib.error.HTTPError:
  print('404 🙅')
except urllib.error.URLError:
  print('URL 錯誤 🙅‍')
