#学习中心的高校授权查询的东北师范大学的信息表zhouju_centers     此次只是东北师范大学
#http://www.open.com.cn/service/collegeauthsearch.html?school_code=10200&school_name=%E4%B8%9C%E5%8C%97%E5%B8%88%E8%8C%83%E5%A4%A7%E5%AD%A6&province_code=&page=1

import requests
import re
import pymysql
import urllib.parse

kw = '东北师范大学'              #此次关键字是东北师范大学，东北师范大学总共21页
keyword = urllib.parse.urlencode({"school_name":kw})
for i in range(1,22):
    url ='http://www.open.com.cn/service/collegeauthsearch.html?school_code=10200&' +str(keyword) +'&province_code=&page='+str(i)
    # print(url)
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    request = requests.get(url,headers=header)
    request.encoding='utf-8'
    c = request.text
    # print(c)
    # html = etree.HTML(c)

    #所有学习中心信息
    dbn = re.compile('<div.*?class="lists-box">.*?<table>.*?<tbody>(.*?)</tbody>',re.S)
    dbname = re.findall(dbn,c)
    for dbna in dbname:
        dbna2 = re.compile('<tr>(.*?)</tr>',re.S)
        dbna3 = re.findall(dbna2,dbna)
        for n in dbna3:
            n2 = re.compile('<td.*?>(.*?)</td>',re.S)
            n3 = re.findall(n2,n)

            #所有学习中心名称
            n4 = re.sub('\d+|\[|\]','',n3[1])
            nn4 = re.sub('奥鹏','舟炬',n4)
            nnn4 = nn4.strip()
            print(nnn4)
            #所有编号
            n5 = re.sub('.*?\[|\]|[A-Z]','',n3[1])
            # print(n5)
            #所有地址
            n6 = n3[3].strip()
            # 所有电话
            n7 = n3[2].strip()

            # db = pymysql.connect(host='localhost',user = 'root',password='123456',port=3306,db='zhouju2')
            # cursor = db.cursor()
            # # 上传数据的sql语句
            # sql = 'INSERT INTO zhouju_centers(name, num, address, phone) values(%s,%s,%s,%s)'
            # cursor.execute(sql,(nnn4,n5,n6,n7))
            # db.commit() #执行数据插入
            # db.close()