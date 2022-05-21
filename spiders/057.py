import urllib.request
import urllib.parse

# url = 'https://www.google.com/search?q=松尾美佑'
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 14-17: ordinal not in range(128)

# url = 'https://www.google.com/search?q=%E6%9D%BE%E5%B0%BE%E7%BE%8E%E4%BD%91'

url = 'https://www.google.com/search?q='

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}

# 將 中文 變成 unicode 編碼格式
name = urllib.parse.quote('松尾美佑')
# %E6%9D%BE%E5%B0%BE%E7%BE%8E%E4%BD%91

url = url + name

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

# 獲取響應內容
content = response.read().decode('UTF-8')

print(content)
