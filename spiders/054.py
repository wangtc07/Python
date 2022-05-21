import urllib.request

url = 'https://www.google.com/'

# 模擬瀏覽器發送請求
response = urllib.request.urlopen(url)

# 一個類型，六個方法
# <class 'http.client.HTTPResponse'>
print(type(response))

# 按照一字節一字節讀取
# content = response.read()
# print(content)

# 返回多少個字節
# content1 = response.read(5)
# print(content1)

# 讀取一行
# content2 = response.readline()
# print(content2)

# 讀取多行
content3 = response.readlines()
print(content3)

# 返回狀態碼 200 正確
print(response.getcode())

# 返回 url 地址
print(response.geturl())

# 獲取狀態訊息
print(response.getheaders())

