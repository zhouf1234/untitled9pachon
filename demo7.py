# 院校特征表zhouju_shool_features
import requests
import re
import pymysql
from lxml import etree

page = 2    #共两页
url = 'http://www.open.com.cn/school/index.html?page='+str(page)
# print(url)
# http://www.open.com.cn/school/index.html?page=1
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
request = requests.get(url,headers=header)
request.encoding='utf-8'
c = request.text
# print(c)

html = etree.HTML(c)
te = html.xpath('//td[@class="area-ele aw_tag"]/a/text()')
print(te)       #八大特征

# 院校名
yuan = html.xpath('//div[@class="clear list-item"]//dl//dt//a//img/@title')
# print(yuan)

# 院校特征
zh = re.compile('<div.*?class="clear list-item">.*?<dl>.*?<dd>.*?<p.*?>(.*?)</p>.*?</dd>.*?</dl>.*?</div>',re.S)
zheng =re.findall(zh,c)
# print(zheng)
zheng3 = []
for i in zheng:
    # print(i)
    zh2 = re.compile('<span>(.*?)</span>',re.S)
    zheng2 = re.findall(zh2,i)
    # print(zheng2)
    zheng3.append(zheng2)
# print(len(zheng3))

dictionary = list(zip(zheng3, yuan))     #特征和学校名合并为列表
# print(dictionary)
for i in dictionary:
    # print(i[0][2:])
    for j in i[0][2:]:
        # print(j)
        if j in te[7]:
            tez = {'feature_name':te[7],'notes':i[1]}
            print(tez)
            # db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='zhouju2')
            # cursor = db.cursor()
            # table= 'zhouju_shool_features'   #定义表名
            # keys = ','.join(tez.keys())    #keys函数，取出键名，并用逗号拼接
            # # print(keys)
            # values = ','.join(['%s'] * len(tez)) #获取data长度，逗号拼接
            # # print(values)
            # sql='INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)
            #
            # if cursor.execute(sql,tuple(tez.values())):
            #     print('successful')
            #     db.commit() #执行数据插入
            # db.close()

