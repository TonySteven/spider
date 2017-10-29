# coding=utf-8

import requests
from PIL import Image
from io import BytesIO


##Make a Request


# r = requests.get('https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=185801639,3443553077&fm=173&s=98D061840A0826575AFB948C03001089&w=218&h=146&img.JPEG')
# r = requests.put("http://httpbin.org/put")
# r = requests.put("http://httpbin.org/delete")
#
# r = requests.put("http://httpbin.org/get")
#
# r = requests.put("http://httpbin.org/get")

# with open('baidu.png', 'wb') as f:
#     f.write(r.content)

##Passing Parameters In URLs



# payload = {'key1': 'value1', 'key2': 'value2'}
#
# r = requests.get('http://httpbin.org/get',params=payload)
#
# print(r.url)

## Response Content
# r = requests.get('https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo_top_ca79a146.png')

## Binary Response Content
# i = Image.open(BytesIO(r.content))

## JSON Response Content
# r = requests.get('https://api.github.com/events')
#
# print(r.json())

## Raw Response Content
# r = requests.get('https://api.github.com/events', stream=True)
#
# r.raw
#
# print(r.raw.read(10))

## Custom Headers
url = 'https://www.baidu.com'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36 QQBrowser/4.2.4843.400'}

r = requests.get(url, headers=headers)

print(r)









