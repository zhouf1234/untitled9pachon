# 在数据库开始建表,服务大厅分类表zhouju_server_category

import requests
import re
import pymysql
from lxml import etree

fwlei =[]
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
request = requests.get('http://www.open.com.cn/service/index.html',headers=header)
request.encoding='utf-8'
c = request.text
# print(c)
html = etree.HTML(c)

fwl = html.xpath('//div[@class="link clear"]//div//a/@title')
# print(fwl[:11])
for f1 in fwl[:11]:
    fwlei.append(f1)
# print(fwl[-3:])
for f2 in fwl[-3:]:
    fwlei.append(f2)

for f in fwlei:
    print(f)
    # db = pymysql.connect(host='localhost',user = 'root',password='123456',port=3306,db='zhouju2')
    # cursor = db.cursor()
    # # 上传数据的sql语句
    # sql = 'INSERT INTO zhouju_server_category(catename) values(%s)'
    # cursor.execute(sql,(f))
    # db.commit() #执行数据插入
    # db.close()