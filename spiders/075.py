from bs4 import BeautifulSoup

soup = BeautifulSoup(open('075.html', encoding='UTF-8'), 'lxml')

# print(soup)

# 根據標籤名查找節點
print(soup.a)  # 第一個符合條件的數據
print(soup.a.attrs)  # 數據的屬性
print('\n')

# 函數
print(soup.find('a'))  # 第一個符合條件的數據
print(soup.find('a', title='llc'))  # 根據 title 的值，找到對應的標籤
print(soup.find('a', class_='n46'))
print('\n')

print(soup.find_all('a'))
print(soup.find_all(['a', 'span']))  # 獲取多個標籤
print(soup.find_all('li', limit=2))  # 找前幾個數據
print('\n')

print(soup.select('a'))  # 獲取多個標籤
print(soup.select('.n46'))  # 通過css選擇器獲取
print(soup.select('#n46'))
print(soup.select('li[id]'))
print(soup.select('li[id=miyu]'))
