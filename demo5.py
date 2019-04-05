# zhouju_posts，获取封面图片连接连接，共15页，299个，然后更新数据库的方法传入连接，此次已成功

# http://www.open.com.cn/news/index.html?page=1    如第一页
import requests
from lxml import etree
import re
import pymysql

pimage = []     #封面图片连接连接列表
for page in range(1,16):    #全部15页
    url = 'http://www.open.com.cn/news/index.html?page='
    url = url+str(page)
    # print(url)      #url拼接，共15页
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    request = requests.get(url,headers=header)
    request.encoding='utf-8'
    c = request.text
    # print(len(c))
    html = etree.HTML(c)

    # # 文章封面图片url,共计299个url
    urphoto = html.xpath('//div[@class="center-content"]//div[@class="news-box"]//a//dl//dt//span/img/@data-original')
    # print(urphoto)
    for p in urphoto:
        p1 = 'http://www.open.com.cn'+p
        pimage.append(p1)

    #获取并拼接了图片连接，可以遍历保存,此次没有要求保存
    # for j in range(len(urphoto)):         #拼接图片url，并保存到本地，此次已经运行成功过
    #     print("s[%d]=%s" % (j, 'http://www.open.com.cn'+urphoto[j]))
    #     header = {
    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    #
    #     request = requests.get('http://www.open.com.cn'+urphoto[j],headers=header)
    #     p2 = '%s.jpg'%j
    #     # print(p2)
    #     with open(p2, "wb")as f:
    #         f.write(request.content)

#更新数据库和准备工作
list = [ i for i in range(1,300)]

dictlp = dict(zip(list,pimage))     #此次已经更新数据库成功
# for key in dictlp:
#     # print(key)
#     # print(dictlp[key])
#
#     db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='zhouju2')
#     cursor = db.cursor()
#     sn = key
#     sc = dictlp[key]
#     sql="UPDATE zhouju_posts SET post_image= '%s' WHERE id= '%s'" %(sc,sn)
#     print(sql)
#     cursor.execute(sql)
#     db.commit() #执行数据插入
#     db.close()