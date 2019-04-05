# zhouju_posts文章表

# http://www.open.com.cn/news/index.html?page=1    先第一页试试看吧,一页页上传的
import requests
from lxml import etree
import re
import pymysql

page = 15        #每页20条
url = 'http://www.open.com.cn/news/index.html?page='
url = url+str(page)
# print(url)      #第一页url拼接
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
request = requests.get(url,headers=header)
request.encoding='utf-8'
c = request.text
# print(c)
html = etree.HTML(c)

# 文章封面图片url
urphoto = html.xpath('//div[@class="center-content"]//div[@class="news-box"]//a//dl//dt//span/img/@data-original')
# print(urphoto)
for p in urphoto:
    p2 = 'http://www.open.com.cn'+p
    # print(p2)

# 分页面连接
ur = html.xpath('//div[@class="center-content"]//div[@class="news-box"]//a/@href')
# print(ur)   #得到所有的url
# http://www.open.com.cn/news/8992.html   分页的网址
for u in ur:
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    request = requests.get('http://www.open.com.cn'+u, headers=header)
    request.encoding = 'utf-8'
    c2 = request.text

    html2 = etree.HTML(c2)

    #文章标题获取
    title = html2.xpath('//div[@class="new-title"]//h2/text()')
    # print(title)
    for i in title:
        i2 = str(i)
        i3 = re.sub('奥鹏','舟炬',i2)
        print(i3)

    #封面图片在最上面

    #文章来源
    laiy = html2.xpath('//div[@class="new-title"]/span[3]/text()')
    # print(laiy)
    for la in laiy:
        la2 = str(la)
        la3 = re.sub('奥鹏','舟炬',la2)
        print(la3)


    #文章来源url连接
    laiyuan = html2.xpath('//div[@class="tag"]//samp[@class="fr"]/text()')
    # print(laiyuan)
    for lai in laiyuan:
        print(lai)

    #文章内容
    wen = html2.xpath('//div[@class="server-content"]//p//text()')
    # print(wen)
    for w in wen:
        w2 = str(w)
        w3 = re.sub('奥鹏','舟炬',w2)
        print(w3)

    #文章编辑时间
    times =html2.xpath('//div[@class="new-title"]/span[2]/text()')
    # print(times)
    for t in times:
        t2=str(t)
        print(t2)     #去不掉空格符

    #阅读人数
    read = html2.xpath('//div[@class="new-title"]/span[1]/text()')
    # print(read)
    for r in read:
        print(r)

        # db = pymysql.connect(host='localhost',user = 'root',password='123456',port=3306,db='zhouju2')
        # cursor = db.cursor()
        # # 上传数据的sql语句
        # sql = 'INSERT INTO zhouju_posts(post_title,source,source_link,post_content,edit_time,views) values(%s,%s,%s,%s,%s,%s)'
        # cursor.execute(sql,(i3,la3,lai,w3,t2,r))
        # db.commit() #执行数据插入
        # db.close()




