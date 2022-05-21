import urllib.request

# 下載網頁
# urlPage = 'https://www.nogizaka46.com/s/n46/diary/detail/65326?ima=0105'

# url 下載的路徑 , filename文件的名字
# urllib.request.urlretrieve(urlPage, 'kubo.html')

# 下載圖片
# urlImg = 'https://www.nogizaka46.com/files/46/diary/n46/MEMBER/0000_11.jpeg'
# urllib.request.urlretrieve(url=urlImg, filename='kubo.jpg')

# 下載影片
urlVideo = 'https://s3-ap-northeast-1.amazonaws.com/smartvideo-prd/nogizaka46/3m-6WfKSRGeeouCiQGe1lQ/1650431175.mp4'
urllib.request.urlretrieve(urlVideo, 'sakura.mp4')

