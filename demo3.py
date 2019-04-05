import requests
import re
import pymysql

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
request = requests.get('http://www.open.com.cn/base/findCityList',headers=header)
request.encoding='utf-8'
c = request.text
print(c)

# pa = re.compile('<td class="name">(.*?)</td>')
# re = re.findall(pa,c)
# print(re)   #首字母

# pat1 = re.compile('<table class="aw_table_hot">.*?')
# ress = re.findall(pat1,c)
# print(ress)

pat=re.compile('<i.*?>(.*?)</i>')
res = re.findall(pat,c)         #所有城市
# print(res)


news_city = []
for id in res:
    if id not in news_city:
        news_city.append(id)
# print(len(news_city))
# for cityname in news_city:
#     print(type(cityname))
    # db = pymysql.connect(host='localhost',user = 'root',password='123456',port=3306,db='zhouju2')
    # cursor = db.cursor()
    #     # 上传数据的sql语句
    # sql = 'INSERT INTO zhouju_cityreg(cityname) values(%s)'
    # cursor.execute(sql,(cityname))
    # db.commit() #执行数据插入
    # db.close()
