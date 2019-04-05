# 在数据库开始建表,服务大厅分类文章表zhouju_server_posts
#通过服务大厅的类，需要的只有14类，找到当前类页面url的所有分页面的url，去分页面取内容，传数据也一个个类传吧

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

fwt = []        #当前服务类下所有文章标题，以下所有数据条数都必须一致
fwly = []       #当前服务类下所有文章来源
fwwz = []       #当前服务类下所有文章内容,文章内容已经处理过了，多段内容拼接为字符串即可，本次为列表
fbt = []        #当前服务类下所有文章编辑时间
frp = []         #当前服务类下所有文章阅读人数

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
                #所有标题
                ftitle = html4.xpath('//div[@class="new-title"]/h2/text()')
                for t in ftitle:
                    t2 = re.sub('奥鹏','舟炬',t)
                    fwt.append(t2.strip())

                #文章来源
                flaiy = html4.xpath('//div[@class="new-title"]/span[3]/text()')
                for l in flaiy:
                    l2 = re.sub('奥鹏','舟炬',l)
                    fwly.append(l2)

                #文章内容
                fwrite = html4.xpath('//div[@class="server-content"]//p//text()')
                w3 = []
                for w in fwrite:
                    w2 = re.sub('奥鹏','舟炬',w)
                    w3.append(w2.strip())
                w4 = ','.join(w3)   #w3得到的内容是列表，w2是字符串，列表内容用逗号拼接为字符串即可了
                fwwz.append(w4)

                #编辑时间
                fwtime = html4.xpath('//div[@class="new-title"]/span[2]/text()')
                fbt.append(fwtime[1].strip())

                #阅读人数
                fread = html4.xpath('//div[@class="new-title"]/span[1]/text()')
                for r in fread:
                    frp.append(r.strip())

                #关键字,恐怕要用更新数据的方法来传，再写一个demo18吧


# 准备上传数据
# 全部做成列表的话，还是用字典方式传入数据库吧
listionary = list(zip(fwt,fwly,fwwz,fbt,frp))
# print(listionary)
for i in listionary:
    # print(i)
    yf = {'cateid':str(list_index+1),'post_title':i[0],'source':i[1],'source_line':'http://www.zhoujuedu.com','post_content':i[2],'edit_time':i[3],'views':i[4]}
    print(yf)

    # db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='zhouju2')
    # cursor = db.cursor()
    # table= 'zhouju_server_posts'   #定义表名
    # keys = ','.join(yf.keys())    #keys函数，取出键名，并用逗号拼接
    # # print(keys)
    # values = ','.join(['%s'] * len(yf)) #获取data长度，逗号拼接
    # # print(values)
    # sql='INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)
    #
    # if cursor.execute(sql,tuple(yf.values())):
    #     print('successful')
    #     db.commit() #执行数据插入
    # db.close()
