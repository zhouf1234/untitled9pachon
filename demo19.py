#院校招生简章表zhouju_school_intro

import requests
import re
import pymysql
from lxml import etree

yuans = [] #35所院校
yuanl = []  #35个院校专业类型

yuanjs = []     #35个院校介绍
yuanzs = []     #35个招生对象介绍
yuanbm = []     #35个报名办法
yuanrx = []     #35个入学方式
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
    # # 所有院校名
    # yuan = html.xpath('//div[@class="clear list-item"]//dl//dt//a//img/@title')
    # for j in yuan:
    #     if j not in yuans:
    #         yuans.append(j)
    #
    # #院校类型
    # yl = html.xpath('//div[@class="clear list-item"]//dl//dd//p[1]/span[2]/text()')
    # for l in yl:
    #     yuanl.append(l)

    #获取院校招生简章url,并拼接,进入分页面取内容
    zsurl = html.xpath('//div[@class="clear list-item"]//dl//dd//p[3]/a[1]/@href')
    for url in zsurl:
        url2 = 'http://www.open.com.cn'+url
        # print(url2)
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        reques = requests.get(url2, headers=header)
        reques.encoding = 'utf-8'
        c2 = reques.text

        html2 = etree.HTML(c2)

        #院校介绍，要求带p标签
        yp = re.compile('<h2.*?id=aw_school_intro_title_0>(.*?)</h2>', re.S)
        yp2 = re.findall(yp, c2)
        for p in yp2:
            if '院校介绍' not in p:
                yj2 = re.compile('<h2.*?id=aw_school_intro_title_1>.*?</h2>(.*?)<strong>', re.S)
                yjs2 = re.findall(yj2, c2)
                yjs3 = ','.join(yjs2)
                yjs4 = re.sub('奥鹏','舟炬',yjs3)
                yuanjs.append(yjs4)
                # print(type(yjs3))
            else:
                yj = re.compile('<h2.*?id=aw_school_intro_title_0>.*?</h2>(.*?)<h.*?>', re.S)
                yjs = re.findall(yj, c2)
                yjss = ','.join(yjs)
                yjsss = re.sub('奥鹏','舟炬',yjss)
                yuanjs.append(yjsss)
                # print(type(yjss))

        #招生对象，要求带p标签
        yd = re.compile('<h2.*?id=aw_school_intro_title_2>(.*?)</h2>', re.S)
        yd2 = re.findall(yd, c2)
        for d in yd2:
            if '招生对象' not in d:
                yx2 = re.compile('<h2.*?id=aw_school_intro_title_3>.*?</h2>(.*?)<h.*?>', re.S)
                yjx2 = re.findall(yx2, c2)
                yjx3 = ','.join(yjx2)
                yuanzs.append(yjx3)

            else:
                yx = re.compile('<h2.*?id=aw_school_intro_title_2>.*?</h2>(.*?)<h.*?>', re.S)
                yjx = re.findall(yx, c2)
                yjxx = ','.join(yjx)
                yuanzs.append(yjxx)

        #报名办法
        yb = re.compile('<h2.*?id=aw_school_intro_title_3>(.*?)</h2>', re.S)
        yb2 = re.findall(yb, c2)
        # print(yp2)
        for b in yb2:
            if '报名办法' in b:
                ybj = re.compile('<h2.*?id=aw_school_intro_title_3>.*?</h2>(.*?)<h.*?>', re.S)
                ybs = re.findall(ybj, c2)
                for ys in ybs:
                    yjsssb = re.sub('奥鹏', '舟炬', ys)
                    yjss1 = re.sub('http://www.open.com.cn', 'http://www.zhoujuedu.com', yjsssb)
                    yjss2 = re.sub('&nbsp;|<span.*?>|</span>|<strong>|</strong>|<a>|</a>|<br/>', '', yjss1)
                    yjss3 = re.compile('<p.*?>(.*?)</p>', re.S)
                    yjss4 = re.findall(yjss3, yjss2)
                    yjss5 = ','.join(yjss4)
                    yuanbm.append(yjss5)
            elif '入学资格' in b:
                ybj2 = re.compile('<h2.*?id=aw_school_intro_title_3>.*?</h2>(.*?)<h.*?>', re.S)
                ybs2 = re.findall(ybj2, c2)
                for ys in ybs2:
                    yjsssb2 = re.sub('奥鹏', '舟炬', ys)
                    yjss12 = re.sub('http://www.open.com.cn', 'http://www.zhoujuedu.com', yjsssb2)
                    yjss22 = re.sub('&nbsp;|<span.*?>|</span>|<strong>|</strong>|<a>|</a>|<br/>', '', yjss12)
                    yjss32 = re.compile('<p.*?>(.*?)</p>', re.S)
                    yjss42 = re.findall(yjss32, yjss22)
                    yjss52 = ','.join(yjss42)
                    yuanbm.append(yjss52)
            elif '报名办法' or '入学资格' not in b:
                s = []
                yj2 = re.compile('<h2.*?id=aw_school_intro_title_4>.*?</h2>(.*?)<h.*?>', re.S)
                yjs2 = re.findall(yj2, c2)  # 获取所有p标签
                for ys2 in yjs2:
                    yjs0 = re.sub('奥鹏', '舟炬', ys2)
                    yjs6 = re.sub('<br/>', '', yjs0)
                    yjs4 = re.compile('<p.*?>(.*?)</p>', re.S)
                    yjs5 = re.findall(yjs4, yjs6)  # 获取所有p标签的内容，并拼接为字符串
                    yjs3 = ','.join(yjs5)
                    s.append(yjs3)
                yjj2 = re.compile('<h2.*?id=aw_school_intro_title_5>.*?</h2>(.*?)<h.*?>', re.S)
                yjjs2 = re.findall(yjj2, c2)  # 获取所有p标签
                for ysj2 in yjjs2:
                    yjs01 = re.sub('奥鹏', '舟炬', ysj2)
                    yjs61 = re.sub('<br/>', '', yjs01)
                    yjs41 = re.compile('<p.*?>(.*?)</p>', re.S)
                    yjs51 = re.findall(yjs41, yjs61)  # 获取所有p标签的内容，并拼接为字符串
                    yjs31 = ','.join(yjs51)
                    s.append(yjs31)
                s2 = ','.join(s)
                yuanbm.append(s2)

        #入学方式
        yr = re.compile('<h2.*?id=aw_school_intro_title_4>(.*?)</h2>', re.S)
        yr2 = re.findall(yr, c2)
        # print(yr2)
        for r in yr2:
            if '入学方式' not in r:
                yr2 = re.compile('<h2.*?id=aw_school_intro_title_6>.*?</h2>(.*?)<h.*?>', re.S)
                yjr2 = re.findall(yr2, c2)
                for yr2 in yjr2:
                    yjr6 = re.sub('<br/>|&nbsp;|<strong>|</strong>', '', yr2)
                    yjr4 = re.compile('<p.*?>(.*?)</p>', re.S)
                    yjr5 = re.findall(yjr4, yjr6)  # 获取所有p标签的内容，并拼接为字符串
                    yjr3 = ','.join(yjr5)
                    yuanrx.append(yjr3)
            else:
                yrr = re.compile('<h2.*?id=aw_school_intro_title_4>.*?</h2>(.*?)<h.*?>', re.S)
                yjr = re.findall(yrr, c2)
                for ys in yjr:
                    yjsssr2 = re.sub('奥鹏', '舟炬', ys)
                    yjssr2 = re.sub('http://www.open.com.cn', 'http://www.zhoujuedu.com', yjsssr2)
                    yjsrr2 = re.sub('&nbsp;|<span.*?>|</span>|<strong>|</strong>|<a>|</a>|<br/>', '', yjssr2)
                    yjrrr2 = re.compile('<p.*?>(.*?)</p>', re.S)
                    yjrr42 = re.findall(yjrrr2, yjsrr2)
                    yjrr52 = ','.join(yjrr42)
                    yuanrx.append(yjrr52)

        #入学资格审核


