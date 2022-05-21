import json
import jsonpath

obj = json.load(open('073.json', 'r', encoding='UTF-8'))

# 所有書的作者
book_author = jsonpath.jsonpath(obj, '$.store.book[*].author')
print(book_author)

# 所有的作者
author = jsonpath.jsonpath(obj, '$..author')
print(author)

# store 下的所有元素
all = jsonpath.jsonpath(obj, '$.store')
print(all)

# store 下的所有錢
price = jsonpath.jsonpath(obj, '$.store..price')
print(price)

# 第三個書
book3 = jsonpath.jsonpath(obj, '$..book[2]')
print(book3)

# 最後一本書
last_book = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')
print(last_book)

# 前兩本書
book = jsonpath.jsonpath(obj, '$..book[0,1]')
print(book)
book = jsonpath.jsonpath(obj, '$..book[:2]')
print(book)

# 過濾所有有包含 isbn 鍵的書
isbn_book = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')
print(isbn_book)

# 哪本書超過 10 元
expensive_book = jsonpath.jsonpath(obj, '$..book[?(@.price>10)]')
print(expensive_book)