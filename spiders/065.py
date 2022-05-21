import urllib.request

url = 'https://weibo.com/p/1005056879740511/info?mod=pedit'

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
  'cookie': 'XSRF-TOKEN=YvTV615vMmEgy0GF1fUE84mA; SSOLoginState=1648224108; _s_tentry=weibo.com; Apache=5131368164427.201.1648224115837; SINAGLOBAL=5131368164427.201.1648224115837; ULV=1648224115842:1:1:1:5131368164427.201.1648224115837:; TC-V-WEIBO-G0=35846f552801987f8c1e8f7cec0e2230; wvr=6; UOR=,,login.sina.com.cn; webim_unReadCount=%7B%22time%22%3A1651600340180%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A1%2C%22msgbox%22%3A0%7D; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhEKzoonmfQ5W6H8freRxqi5JpX5KMhUgL.FoqRS0.NSh5feK22dJLoIpjLxKML1-eL1-qLxK-LBKBL12qLxKqL1-eL1-qt; ALF=1683216220; SCF=ArWJrTSmKsKAKHUKbgjR2rZgAwEurMdxHzOjaN1r34kvxz-OujCGFcsK8J4Bkp4H6JRPU1CGuD2BjDTzoyFhbvY.; SUB=_2A25PdtOODeRhGeBG7FsW9C7Jyj2IHXVsAkJGrDV8PUNbmtAfLROjkW9NQee_9TIwCi7IhgdcBRPUZGvrLwWpPM1o; wb_view_log_6879740511=2560*14402; PC_TOKEN=410fdb1c12',
  # 判斷當前路徑是不是由上一個路徑進來的
  'referer': 'https://login.sina.com.cn/'
}

try:
  request = urllib.request.Request(url=url, headers=headers)

  response = urllib.request.urlopen(request)

  # 獲取響應內容
  content = response.read().decode('UTF-8')
  print(content)

  with open('weibo.html', 'w', encoding='UTF-8')as fp:
    fp.write(content)

except urllib.error.HTTPError:
  print('404 🙅')
except urllib.error.URLError:
  print('URL 錯誤 🙅‍')
