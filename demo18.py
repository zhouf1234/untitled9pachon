# 在数据库开始建表,服务大厅分类文章表zhouju_server_posts,更新数据的方法传关键字,更新成功

import requests
import re
import pymysql
from lxml import etree

fwurl =[]   #14类的所有url,通过这个去找分页面url，再找内容
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
request = requests.get('http://www.open.com.cn/service/index.html',headers=header)
request.encoding='utf-8'
c = request.text
# print(c)
html = etree.HTML(c)
fwl = html.xpath('//div[@class="link clear"]//div//a/@href')
# print(fwl[:11])         #进行拼接url
for f1 in fwl[:11]:
    fwurl.append('http://www.open.com.cn'+f1)
# print(fwl[-3:])
for f2 in fwl[-3:]:
    fwurl.append('http://www.open.com.cn'+f2)

list_index = 13
fwlu = fwurl[list_index]       #14类服务，一个一个找，一个个上传，内容较多
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
reques = requests.get(fwlu,headers=header)
reques.encoding='utf-8'
c2 = reques.text

#获取当前url页数  #页面如http://www.open.com.cn/help/166.html?page=1
html2 = etree.HTML(c2)
flpage = html2.xpath('//div[@class="pagination"]//input/@data-max')


wg = []
for p in flpage:
    p2 = int(p)
    for pa in range(1,p2+1):
        ffurl = fwlu+'?page='+str(pa)
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        reque = requests.get(ffurl, headers=header)
        reque.encoding = 'utf-8'
        c3 = reque.text

        html3 = etree.HTML(c3)
        #去每页的每个分页面取内容，如http://www.open.com.cn/help/show-7170.html
        fffurl = html3.xpath('//div[@class="news-box"]//dl//dt//h4/a/@href')
        for fu in fffurl:
            if fu.startswith('/') == True:
                fu2 = 'http://www.open.com.cn'+fu
                header = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
                requ = requests.get(fu2, headers=header)
                requ.encoding = 'utf-8'
                c4 = requ.text

                html4 = etree.HTML(c4)

                #关键字,恐怕要用更新数据的方法来传
                fg = html4.xpath('//div[@class="tag"]//text()')     #得到n个列表
                # print(type(fg[3:]))
                w4 = ','.join(fg[3:])   #得到的关键字列表拼接成字符串，在去替换掉不需要的字符
                # print(w4)
                w6 =re.sub(' |\n|来源|\：|http://www.open.com.cn/|http://www.iopen.com.cn/|http://www.open.com.cn','',w4)
                # print(w6)
                wg.append(w6.replace(',', ' '))  #所有逗号替换为空格
# print(wg)
print(len(wg))

lis = [i for i in range(486,487)]

listionary = dict(zip(lis,wg))
for i in listionary:
    print(i)
    # print(listionary[i])

    # db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='zhouju2')
    # cursor = db.cursor()
    # sn = i
    # sc = listionary[i]
    # sql="UPDATE zhouju_server_posts SET keywords= '%s' WHERE id= '%s'" %(sc,sn)
    # print(sql)
    # cursor.execute(sql)
    # db.commit() #执行数据插入
    # db.close()




