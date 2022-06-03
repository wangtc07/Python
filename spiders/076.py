from bs4 import BeautifulSoup
import urllib.request

url = 'https://www.starbucks.com.cn/menu/'

response = urllib.request.urlopen(url)

content = response.read().decode('UTF -8')

# //ul[@class="grid padded-3 product"]//h3/text()
soup = BeautifulSoup(content, 'lxml')
# ul[class="grid padded-3 product"] h3
list = soup.select('ul[class="grid padded-3 product"] strong')
print(list)
