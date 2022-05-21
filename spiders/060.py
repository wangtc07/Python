import urllib.parse
import urllib.request
import json

# urlencode
# 多參數的時候

url = 'https://translate.google.com.tw/_/TranslateWebserverUi/data/batchexecute?rpcids=AVdN8&source-path=%2F&f.sid=4432242214293821683&bl=boq_translate-webserver_20220501.18_p0&hl=zh-TW&soc-app=1&soc-platform=1&soc-device=1&_reqid=1684325&rt=c'
headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
  'cookie': '_ga=GA1.4.398103432.1646382878; 1P_JAR=2022-04-24-14; SID=JwjokBP3pc1A5uCcAN79PRBwhj8NcI7WCE8zh--OxmmvrERtHmtxxS8NoIPcBqCkQIMtcw.; __Secure-1PSID=JwjokBP3pc1A5uCcAN79PRBwhj8NcI7WCE8zh--OxmmvrERtqDZVBZ01xAAAwJMo1iJCfg.; __Secure-3PSID=JwjokBP3pc1A5uCcAN79PRBwhj8NcI7WCE8zh--OxmmvrERt2rijAa3Pnqc8eiD55iSyXw.; HSID=AVkSfon6DtLUDvAbM; SSID=A0IR4WxdqMSUaOBmh; APISID=sbUvJ5k1UtvfI_cK/AmY5QKyLV8Pe6F_kO; SAPISID=RkDNt7U_Y_E25Of7/AEyiTD5twUNU-fxeA; __Secure-1PAPISID=RkDNt7U_Y_E25Of7/AEyiTD5twUNU-fxeA; __Secure-3PAPISID=RkDNt7U_Y_E25Of7/AEyiTD5twUNU-fxeA; _gid=GA1.4.1399451948.1651591466; OTZ=6488124_24_24__24_; NID=511=vdviwfjWcUcd3V080xo4-j5e-eVZTmNB15J9-Emv1TrycUqeXrUsCrdsiM8E9fhZqwOI7TWXYBhNftv6ui8Q53q5YAAB_G4-CFkbjctYSCFesH4aDWxUa4JDgn407pFXEjxgCXMFTAMX4smIgx_BEWQzdw16zwSBx1vH2OZIIHoN5lIxPK9I-C2QYxSSvcKTebq-lsP0b1R-MNGVz-PGzzDDIAmwrUU7WpydT4QZ4hpmLiR9qasMAbubju9X3nfjxUplUCBBlX9IZTj32TMPDHjtubPA_2kAoHHi0vA3iwj1x47rhqv8_9NidqMrcENH1toYQeV1ZiV12vNXsNdZ6j98HgLEu2QgkYYLdynzcaOoRm6fSqKlfZV0-PLr16iMrEclU6Unck1t-yzPqUFSZBVsJ38'
}


data = {
  'f.req': '[[["AVdN8","[\"uk\",\"en\",\"zh-TW\"]",null,"generic"]]]',
  'at': 'AD08yZk2dmXds6DweYFKtx9vEfdt:1651591523729'
}

# post 請求必須進行編碼
data = urllib.parse.urlencode(data).encode('UTF-8')

request = urllib.request.Request(url=url, data=data, headers=headers)
print(request)

response = urllib.request.urlopen(request)
# POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type str.

# 獲取響應內容
content = response.read().decode('UTF-8')
print(content)

print(type(content))
# <class 'str'>

# str -> json
obj = json.loads(content)
print(obj)