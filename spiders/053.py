# 導入 urllib
import urllib.request

# 定義 url
url = 'https://www.google.com/'

# 模擬瀏覽器發送請求
response = urllib.request.urlopen(url)

# 獲取響應中的 頁面源碼
content = response.read()

# 將 2進制 -> 字符串 decode('編碼格式') charset="UTF-8"
content = content.decode('UTF-8')

# 打印
print(content)




