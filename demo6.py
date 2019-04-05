# 院校类型表zhouju_scholl_types
import requests
import re
import pymysql
from lxml import etree

page = 1    #共两页
url = 'http://www.open.com.cn/school/index.html?page='+str(page)
# print(url)
# http://www.open.com.cn/school/index.html?page=1
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
request = requests.get(url,headers=header)
request.encoding='utf-8'
c = request.text
# print(c)

html = etree.HTML(c)
lei = html.xpath('//td[@class="area-ele aw_type"]//p/a/text()')
print(lei)      #八大类型列表

# 分类院校名
yuan = html.xpath('//div[@class="clear list-item"]//dl//dt//a//img/@title')
# print(yuan)

#类别说明，类别
shuo2 = html.xpath('//div[@class="clear list-item"]//dl//dd//p[1]/span[2]/text()')
# print(shuo2)

dictionary = list(zip(shuo2, yuan))     #类别和学校名合并为列表
# print(dictionary)
for i in dictionary:
    # print(i)
    if i[0] in lei[7]:
        leig = {'type_name': lei[7], 'notes':i[1]} #如果院校类型在列表中的第一索引，则第二索引作为字典值
        # print(leig)

        # db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='zhouju2')
        # cursor = db.cursor()
        # table= 'zhouju_scholl_types'   #定义表名
        # keys = ','.join(leig.keys())    #keys函数，取出键名，并用逗号拼接
        # # print(keys)
        # values = ','.join(['%s'] * len(leig)) #获取data长度，逗号拼接
        # # print(values)
        # sql='INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)
        #
        # if cursor.execute(sql,tuple(leig.values())):
        #     print('successful')
        #     db.commit() #执行数据插入
        # db.close()



















