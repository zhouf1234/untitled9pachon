#院校信息表zhouju_schools
import requests
import re
import pymysql
from lxml import etree


# # http://www.open.com.cn/major/index.html?page=1

yuans = [] #35所院校
yimg = []   #35个院校图片连接
yword = []  #35个院校描述
yxun = []   #35条校训
yhui = []   #35个校徽图片连接
ybxuz = []  #35个报名须知，元组类型，里面是35个列表，包含p标签的
ybimage = [] #35个毕业证模板图片连接
yximage = []    #35个学位证模板图片连接
yj = []     #35个0和1表示是否是985
yr = []     #35个0和1表示是否是211
ydou = []   #35个0和1表示是否是双一流
ls = []     #35个对应的院校类型表的id
yrp = []    #35个累计报读人数

for i in range(1,3):    #总共两页
    # print(i)
    url = 'http://www.open.com.cn/school/index.html?page=' + str(i)
    # print(url)
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    request = requests.get(url, headers=header)
    request.encoding = 'utf-8'
    c = request.text
    # print(len(c))

    html = etree.HTML(c)
    yuan = html.xpath('//div[@class="clear list-item"]//dl//dt//a//img/@title')
    # print(yuan)       #所有院校名
    for j in yuan:
        if j not in yuans:
            yuans.append(j)

    #校训
    xu = html.xpath('//div[@class="clear list-item"]//dl//dd//h2/a/text()')
    for x in xu:
        x2 = str(x)
        x3 = x2.strip()
        x4 = re.sub('.*?--','',x3)
        yxun.append(x4)

    #校徽图片地址
    xhui = html.xpath('//div[@class="clear list-item"]//dl//dt//a/img/@data-original')
    # print(xhui)
    for h in xhui:
        h2 = 'http://www.open.com.cn'+h
        yhui.append(h2)

    # 是否985，是否211，是否双一流
    sf = re.compile('<div.*?class="clear list-item">.*?<dl>.*?<dd>.*?<p.*?>(.*?)</p>.*?</dd>.*?</dl>.*?</div>', re.S)
    shifou = re.findall(sf, c)
    for shf in shifou:
        # print(i)
        sh = re.compile('<span>(.*?)</span>', re.S)
        zheng2 = re.findall(sh, shf)
        # print(zheng2[2:])
        s = '1'
        f = '0'
        j = s if '985' in zheng2[2:] else f
        yj.append(j)
        r = s if '211' in zheng2[2:] else f
        yr.append(r)
        dou = s if '双一流' in zheng2[2:] else f
        ydou.append(dou)

    #累计报读人数
    read = html.xpath('//div[@class="clear list-item"]//dl//dd//p[@class="levels"]/text()')
    # print(read)
    for rp in read:
        rp2 = str(rp)
        rp3 = re.sub('.*?累计报读：','',rp2)
        yrp.append(rp3)


    #分页里
    yuanurl = html.xpath('//div[@class="clear list-item"]//dl//dd//h2/a/@href')
    # print(yuanurl)      #院校信息分页面所有url,去分页面取内容
    for yurl in yuanurl:
        yurl2 = 'http://www.open.com.cn'+yurl
        # print(yurl2)
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        requ = requests.get(yurl2, headers=header)
        requ.encoding = 'utf-8'
        c2 = requ.text
        # print(len(c2))

        html2 = etree.HTML(c2)
        # 院校首页图连接
        im = re.compile('<div.*?class="top_bg".*?style="background:url\((.*?)\).*?',re.S)
        yuanimage = re.findall(im,c2)
        # print(yuanimage)
        for ima in yuanimage:
            ima2 = re.sub("'",'',ima)
            ima3 = 'http://www.open.com.cn'+ima2
            # print(ima3)
            yimg.append(ima3)

        #院校描述
        word = html2.xpath('//div[@class="top_bg"]//div[@class="w1200"]//p[2]/text()')
        # print(word)
        for w in word:
            yword.append(w)

        #报名须知，要求是带p标签
        xr = re.compile('<div.*?class="xuzhi">(.*?)\s+\<\!.*?</div>',re.S)
        xr2 = re.findall(xr,c2)
        xz5 = []
        for xz in xr2:
            xz2 = re.sub('<h3>|.*?</h3>','',xz)
            xz3 = re.sub('奥鹏','舟炬',xz2)
            xz4 = re.sub('www.open.com.cn','www.zhoujuedu.com',xz3)
            xz5.append(xz4)
        # print(xz5)
        ybxuz.append(xz5)


        #毕业证图片连接地址
        bimage = html2.xpath('//div[@class="w1165 clear"]//div//ul//li[1]//div[@class="img-box"]/img/@src')
        # print(bimage)
        for b in bimage:
            b2 = 'http://www.open.com.cn'+b
            ybimage.append(b2)

        #学位证图片连接地址
        ximage = html2.xpath('//div[@class="w1165 clear"]//div//ul//li[2]//div[@class="img-box"]/img/@src')
        # print(ximage)
        for xw in ximage:
            xw2 = 'http://www.open.com.cn'+xw
            yximage.append(xw2)

# 去其他表查询需要的数据
#院校对应的院校类型表的id，查到的id没有和院校对应上，根据院校名字更新数据试试，此次未上传，看demo10，11


# 报名须知的元组处理
ybxz = []
for bm in ybxuz:
    for b in bm:
        ybxz.append(b)

# 准备上传数据
# 全部做成列表的话，还是用字典方式传入数据库吧
listionary = list(zip(yuans,yimg,yword,yxun,yhui,ybxz,ybimage,yximage,yj,yr,ydou,yrp))
for i in listionary:
    # print(i)
    yx = {'name':i[0],'banner':i[1],'description':i[2],'motto':i[3],'emblem':i[4],'enrol_notes':i[5],'diploma_images':i[6],'degree_imges':i[7],'is985':i[8],'is211':i[9],'isdouble':i[10],'count':i[11]}
    print(yx)

    # db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='zhouju2')
    # cursor = db.cursor()
    # table= 'zhouju_schools'   #定义表名
    # keys = ','.join(yx.keys())    #keys函数，取出键名，并用逗号拼接
    # # print(keys)
    # values = ','.join(['%s'] * len(yx)) #获取data长度，逗号拼接
    # # print(values)
    # sql='INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)
    #
    # if cursor.execute(sql,tuple(yx.values())):
    #     print('successful')
    #     db.commit() #执行数据插入
    # db.close()









