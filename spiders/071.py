import urllib.request
from lxml import etree

url = 'https://www.google.com/'

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('UTF-8')

# 解析響應的數據
tree = etree.HTML(content)

# 獲取想要的數據
result = tree.xpath('//input[@class="gNO89b"]/@value')

print(result[0])