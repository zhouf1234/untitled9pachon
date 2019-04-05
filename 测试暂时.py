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

yz = re.compile('<h3>(.*?)</h3>',re.S)
yz2 = re.findall(yz,c2)
print(yz2)
# for z in yz2:

# for r in yr2:
#     if '入学方式' not in r:
#         yr2 = re.compile('<h2.*?id=aw_school_intro_title_6>.*?</h2>(.*?)<h.*?>', re.S)
#         yjr2 = re.findall(yr2, c2)
#         for yr2 in yjr2:
#             yjr6 = re.sub('<br/>|&nbsp;|<strong>|</strong>', '', yr2)
#             yjr4 = re.compile('<p.*?>(.*?)</p>', re.S)
#             yjr5 = re.findall(yjr4, yjr6)  # 获取所有p标签的内容，并拼接为字符串
#             yjr3 = ','.join(yjr5)
#             print(yjr3)
#     else:
#         yrr = re.compile('<h2.*?id=aw_school_intro_title_4>.*?</h2>(.*?)<h.*?>', re.S)
#         yjr = re.findall(yrr, c2)
#         for ys in yjr:
#             yjsssr2 = re.sub('奥鹏', '舟炬', ys)
#             yjssr2 = re.sub('http://www.open.com.cn', 'http://www.zhoujuedu.com', yjsssr2)
#             yjsrr2 = re.sub('&nbsp;|<span.*?>|</span>|<strong>|</strong>|<a>|</a>|<br/>', '', yjssr2)
#             yjrrr2 = re.compile('<p.*?>(.*?)</p>', re.S)
#             yjrr42 = re.findall(yjrrr2, yjsrr2)
#             yjrr52 = ','.join(yjrr42)
#             print(yjrr52)








