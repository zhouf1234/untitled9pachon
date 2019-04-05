import requests
import re
import pymysql
from lxml import etree

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
reques = requests.get('http://www.open.com.cn/encrollregulation-3333.html', headers=header)
reques.encoding = 'utf-8'
c2 = reques.text
# print(c2)
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
                print(yjss5)
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
                print(yjss52)
        elif '报名办法' or '入学资格' not in b:
            s = []
            yj2 = re.compile('<h2.*?id=aw_school_intro_title_4>.*?</h2>(.*?)<h.*?>', re.S)
            yjs2 = re.findall(yj2, c2)  # 获取所有p标签
            for ys2 in yjs2:
                yjs0 = re.sub('奥鹏','舟炬',ys2)
                yjs6 = re.sub('<br/>', '', yjs0)
                yjs4 = re.compile('<p.*?>(.*?)</p>', re.S)
                yjs5 = re.findall(yjs4, yjs6)  # 获取所有p标签的内容，并拼接为字符串
                yjs3 = ','.join(yjs5)
                s.append(yjs3)
            yjj2 = re.compile('<h2.*?id=aw_school_intro_title_5>.*?</h2>(.*?)<h.*?>', re.S)
            yjjs2 = re.findall(yjj2, c2)  # 获取所有p标签
            for ysj2 in yjjs2:
                yjs01 = re.sub('奥鹏','舟炬',ysj2)
                yjs61 = re.sub('<br/>', '', yjs01)
                yjs41 = re.compile('<p.*?>(.*?)</p>', re.S)
                yjs51 = re.findall(yjs41, yjs61)  # 获取所有p标签的内容，并拼接为字符串
                yjs31 = ','.join(yjs51)
                s.append(yjs31)
            s2 = ','.join(s)
            print(s2)
