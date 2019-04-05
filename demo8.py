# 专业分类表zhouju_major_cates

import requests
import re
import pymysql
from lxml import etree

page = 1    #第一页就行
url = 'http://www.open.com.cn/major/index.html?page='+str(page)
# print(url)
# http://www.open.com.cn/major/index.html?page=1
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
request = requests.get(url,headers=header)
request.encoding='utf-8'
c = request.text
# print(c)

html = etree.HTML(c)
zhuan = html.xpath('//div[@class="select-box"]//tr[1]//td[3]//div/a/text()')
print(zhuan)    #所有专业大类,此次已经上传了
# for z in zhuan:
#     print(z)
#     db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='zhouju2')
#     cursor = db.cursor()
#     # 上传数据的sql语句
#     sql = 'INSERT INTO zhouju_major_cates(catename) values(%s)'
#     cursor.execute(sql,(z))
#     db.commit() #执行数据插入
#     db.close()


#如 http://www.open.com.cn/major/?b=7
# 专业小类分页面的url
zhuanur = html.xpath('//div[@class="select-box"]//tr[1]//td[3]//div/a/@href')
# print(zhuanur)
zs = []
for u in zhuanur:
    ur = 'http://www.open.com.cn'+u
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    reque = requests.get(ur, headers=header)
    reque.encoding = 'utf-8'
    c2 = reque.text


    html2 = etree.HTML(c2)
    # zhbig = html2.xpath('//div[@class="select-box"]//tr[1]//td[3]//div/span/text()')
    # print(zhbig) #list类型，获取到的专业大类名,暂时没用到这个

    zhsma = html2.xpath('//div[@class="select-box"]//tr[2]//td[3]//div/a/text()')
    # print(type(zhsma))    #所有专业小类,list类型
    zs.append(zhsma)
# print(zs)
for s in zs[15]:
    # print(s)
    sc = {'catename':s,'pid':'16'}  #按大类下小类上传的，16次
    print(sc)
    # db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='zhouju2')
    # cursor = db.cursor()
    # table= 'zhouju_major_cates'   #定义表名
    # keys = ','.join(sc.keys())    #keys函数，取出键名，并用逗号拼接
    # # print(keys)
    # values = ','.join(['%s'] * len(sc)) #获取data长度，逗号拼接
    # # print(values)
    # sql='INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)
    #
    # if cursor.execute(sql,tuple(sc.values())):
    #     print('successful')
    #     db.commit() #执行数据插入
    # db.close()


