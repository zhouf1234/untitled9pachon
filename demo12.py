#专业信息表zhouju_majors，实际取的是专业小类名称对应的院校信息
# 因为总共50页，上千条的数据，建议去大类的url取数据，16个大类，一个大类一个大类的取，即一个url一个url分别取

import requests
import re
import pymysql
from lxml import etree

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
request = requests.get('http://www.open.com.cn/major/index.html',headers=header)
request.encoding='utf-8'
c = request.text
# print(c)
html = etree.HTML(c)
#如 http://www.open.com.cn/major/?b=7
# 主页获取所有大类分页面的url
zhuanur = html.xpath('//div[@class="select-box"]//tr[1]//td[3]//div/a/@href')
# print(zhuanur)
#一个个url分别去取，上千条数据太大了
bigurlf = []
for u in zhuanur:
    ur = 'http://www.open.com.cn'+u
    bigurlf.append(ur)
# print(bigurlf[0])

bigurl = bigurlf[15]     #共16个大类url
header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
reque = requests.get(bigurl, headers=header)
reque.encoding = 'utf-8'
c2 = reque.text

#当前分页面有多少页
#http://www.open.com.cn/major/?b=7&page=1   进行url拼接
html2 = etree.HTML(c2)
pages = html2.xpath('//div[@class="major-content clear"]//div//div[3]//input/@data-max')
# print(pages)

zxiao = []  #当前大类下所有专业小类名称，最后需要和dxiao列表进行判断和字典拼接，传入表格的是此小类名称,按dxiao吧先
zyxm = []    #当前大类下所有专业小类的院校，和dxiao的条数一致，用于匹配school表id

dxiao = []  #当前大类下所有院校的专业小类名称，决定传入表的数据有多少条
zjs = []    #当前大类下所有院校的专业简述，和dxiao的条数一致
zl = '1'    #所有院校的所属分类id，和dxiao的条数一致,现在是一个大类一个大类在传数据，直接传完一类手填即可
zcc = []     #当前大类下所有院校的专业层次，和dxiao的条数一致
# zyx = []           #当前类名所属院校id,关联school表,直接加一条学院名字段吧，太难拼接了，更新数据方法传
ztj = []    #当前大类下所有院校的是否推荐，和dxiao的条数一致
zxt = []    #当前大类下所有院校的学制，和dxiao的条数一致
zbp = []    #当前大类下所有院校的报读人数，和dxiao的条数一致
zk = []     #当前大类下所有院校的是否录取快，和dxiao的条数一致
zts = []    #当前大类下所有院校的是否特色专业，和dxiao的条数一致
zxjs = []   #当前大类下所有院校专业介绍，和dxiao的条数一致
for i in pages:
    i2 = int(i)
    for p in range(1,i2+1):
        burl = bigurl + '&page=' +str(p)
        # print(burl)
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        requ = requests.get(burl, headers=header)
        requ.encoding = 'utf-8'
        c3 = requ.text

        #大类下所有小类名称
        html3 = etree.HTML(c3)
        zhsma = html3.xpath('//div[@class="select-box"]//tr[2]//td[3]//div/a/text()')
        for z in zhsma:
            if z not in zxiao:
                zxiao.append(z)

        #大类下每所院校的专业小类名称
        dx = html3.xpath('//div[@class="major-channel-list"]//ul//li//p/@title')
        for px in dx:
            dxiao.append(px)

        #大类下每所院校的专业小类简述
        zjian = html3.xpath('//div[@class="major-channel-list"]//ul//li//dl//dd[1]/text()')
        for z in zjian:
            zjs.append(z)

        #大类下每所院校的层次，0高起专，1高起本，2专升本
        zceng = html3.xpath('//div[@class="major-channel-list"]//ul//li//dl//dd[2]//p//strong[2]//span[1]//i/text()')
        # print(zceng)
        for zc in zceng:
            gqz = '0'
            gqb = '1'
            zsb = '2'
            if zc == '高起专':
                zcc.append(gqz)
            elif zc == '高起本':
                zcc.append(gqb)
            elif zc == '专升本':
                zcc.append(zsb)

        # 大类下每所院校的学制，即学习时间
        zxtime = html3.xpath('//div[@class="major-channel-list"]//ul//li//dl//dd[2]//p//strong[2]//span[2]//i/text()')
        for zt in zxtime:
            zxt.append(zt)

        # 大类下每所院校的报读人数
        zbpeo = html3.xpath('//div[@class="major-channel-list"]//ul//li//dl//dd[2]//p//strong[2]//span[3]//i/text()')
        for zp in zbpeo:
            zbp.append(zp)

        # 大类下每所专业院校的是否推荐，是否录取快，是否特色专业
        zh = re.compile('<div.*?class="major-channel-list">.*?<ul>(.*?)</ul>.*?</div>', re.S)
        zheng = re.findall(zh, c3)
        for t in zheng:
            zh2 = re.compile('<strong.*?class="title-com major-labels">(.*?)</strong>', re.S)
            t2 = re.findall(zh2, t)
            for t3 in t2:
                t4 = t3.strip()
                t5 = re.sub('<i.*?>|</i>', '', t4)

                t6 = '1' if '院校推荐' in t5 else '0'
                ztj.append(t6)
                k = '1' if '录取快' in t5 else '0'
                zk.append(k)
                ts = '1' if '特色专业' in t5 else '0'
                zts.append(ts)

        #所属院校名称
        yx = html3.xpath('//div[@class="major-channel-list"]//ul//li//dl[1]//dd[2]//strong[1]//span[1]/text()')
        for yx2 in yx:
            zyxm.append(yx2.strip())


        #去每个专业类下的院校的分页面url取内容，如http://www.open.com.cn/major/19414.html
        zyurl = html3.xpath('//div[@class="major-channel-list"]//ul//li//dl[1]//dt/a/@href')
        for yu in zyurl:
            yu2 = 'http://www.open.com.cn'+yu
            header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
            req = requests.get(yu2, headers=header)
            req.encoding = 'utf-8'
            c4 = req.text

            #大类下每所专业院校的专业介绍
            html4 = etree.HTML(c4)
            zyjs = html4.xpath('//div[@class="major-detail clear"]//div//div//div//div[2]//text()')
            # print(zyjs)   #有空格元素在列表里
            mytest = [i for i in zyjs if i != ' ']  #去除列表所有空格元素
            # print(mytest)
            for zy in mytest:
                # print(zy)
                zxjs.append(zy)



#准备上传数据，做成字典上传吧
listionary = list(zip(dxiao,zjs,zcc,ztj,zxt,zbp,zk,zts,zxjs,zyxm))
for i in listionary:
    # print(i)
    yz = {'major_category':'16','major_name':i[0],'major_desciption':i[1],'level':i[2],'isrecommend':i[3],'times':i[4],'count':i[5],'isfast':i[6],'isspecial':i[7],'detail':i[8],'schoolsssss':i[9]}
    print(yz)

    # db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='zhouju2')
    # cursor = db.cursor()
    # table= 'zhouju_majors'   #定义表名
    # keys = ','.join(yz.keys())    #keys函数，取出键名，并用逗号拼接
    # # print(keys)
    # values = ','.join(['%s'] * len(yz)) #获取data长度，逗号拼接
    # # print(values)
    # sql='INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)
    #
    # if cursor.execute(sql,tuple(yz.values())):
    #     print('successful')
    #     db.commit() #执行数据插入
    # db.close()


