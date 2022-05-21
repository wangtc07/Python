import urllib.request
from lxml import etree


# 下載前10頁的圖片
# https://sc.chinaz.com/tupian/huadetupian.html
# https://sc.chinaz.com/tupian/huadetupian_2.html

# 請求對象的訂製
def createRequeat(page):
  if (page == 1):
    url = 'https://sc.chinaz.com/tupian/huadetupian.html'
  else:
    url = 'https://sc.chinaz.com/tupian/huadetupian_' + str(page) + '.html'

  headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
  }

  request = urllib.request.Request(url=url, headers=headers)
  return request


def getContent(request):
  response = urllib.request.urlopen(request)
  content = response.read().decode('UTF-8')
  return content


def download(content):
  # 下載圖片
  # urllib.request.urlretrieve('圖片地址', '文件的名字')
  tree = etree.HTML(content)
  # 圖片一班會進行懶加載 src -> src2
  src = tree.xpath('//div[@id="container"]//div/a/img/@src2')

  name = tree.xpath('//div[@id="container"]//div/a/img/@alt')

  for i in range(len(src)):
    link = 'https:' + src[i]
    imgName = "./072/" + name[i] + ".jpg"
    print(link, imgName)

    urllib.request.urlretrieve(link, imgName)
  pass


if __name__ == '__main__':
  startPage = int(input('start page'))
  endPage = int(input('end page'))

  for page in range(startPage, endPage + 1):
    request = createRequeat(page)
    content = getContent(request)
    download(content)
