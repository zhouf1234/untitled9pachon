# 爬取热门省市和所有省市
import requests
from lxml import etree
import re
from pyquery import PyQuery as pq
import pymysql

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
request = requests.get('http://www.open.com.cn/base/findCityList',headers=header)
request.encoding='utf-8'
c = request.text
# print(c)

html = etree.HTML(c)
# res = html.xpath('//table//tr//text()')
# print(res)
# # for i in res:
# #     print(i)

res = html.xpath('//body')
for r in res:
    # zimu = r.xpath("//td[@class='name']/text()")
    # print(zimu)         #首字母
    # for i in zimu:
    #     print(i)

    hot = r.xpath("//table[@class='aw_table_hot    ']//tr//i/text()")
    print(hot)  #所有热门省市

    city = r.xpath("//i/text()")
    # print(city)    #所有省市

    # for d in range(1,369):  #插入id,写了自增长就不用
    #     print(d)
    #     db = pymysql.connect(host='localhost',user = 'root',password='123456',port=3306,db='zhouju')
    #     cursor = db.cursor()
    #     # 上传数据的sql语句
    #     sql = 'INSERT INTO zhouju_cityreg(id) values(%s)'
    #     try:
    #         cursor.execute(sql,(d))
    #         db.commit() #执行数据插入
    #     except:
    #         db.rollback()
    #     db.close()


    # news_city = []
    # for id in city:
    #     if id not in news_city:
    #         news_city.append(id)
    # # print(len(news_city))
    # for cityname in news_city:
    #     ci = str(cityname)
    #     # print(ci)   #插不进去，。。。，一个字段一个字段的话
    # # print(cityname)
    # for i in news_city:
    #     res = '1' if i in hot else '0'
    #     # print(type(res))
    #     dic = {'is_hot':res}    #一个字段一个字段更新的话，有问题的，因为设置了主键自增长，除非一开始就全部插入进去







