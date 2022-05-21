import urllib.parse
import urllib.request
import json


def create_request(page):
  baseUrl = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&'

  data = {
    "start": (page - 1) * 20,
    'limit': 20
  }

  url = baseUrl + urllib.parse.urlencode(data);

  print(url)

  headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
  }

  request = urllib.request.Request(url=url, headers=headers)

  return request


def get_content(request):
  response = urllib.request.urlopen(request)
  content = response.read().decode('UTF-8')
  return content


# 程序的入口
def download(content, page):
  with open('douben_' + str(page) + '.json', 'w', encoding='UTF-8') as fp:
    fp.write(content)


if __name__ == '__main__':
  startPage = int(input("start page"))
  endPage = int(input('end page'))

  for page in range(startPage, endPage + 1):
    request = create_request(page)
    # 獲取響應數據
    content = get_content(request)
    # 下載
    download(content, page)

