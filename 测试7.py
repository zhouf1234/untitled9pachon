import requests
import os
# header = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
# request = requests.get('http://www.open.com.cn/product/img/news/20181120/15426846215bf37fcdb9534.jpg',headers=header)
#
# #'favicon.ico'：要保存的文件名，
# with open('0.png',"wb")as f:
#     f.write(request.content)

jjj =['http://www.open.com.cn/product/img/product/intro/21.png',
      'http://www.open.com.cn/product/img/product/intro/39.png',
      'http://www.open.com.cn/product/img/product/intro/139.png',
      'http://www.open.com.cn/product/img/product/intro/38.png',
      'http://www.open.com.cn/product/img/product/intro/36.png',
      'http://www.open.com.cn/product/img/product/intro/74.png']

for j in range(len(jjj)):
    print(jjj[j])
    header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    request = requests.get(jjj[j],headers=header)

    filepath = './01'
    if not os.path.exists(filepath):  # 如果文件夹不存在就创建
        os.mkdir(filepath)
    p2 = filepath + '/%s.jpg' % j
    # print(p2)
    # with open(p2, "wb")as f:
    #     f.write(request.content)
