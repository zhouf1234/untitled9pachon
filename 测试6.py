import requests
import re
import pymysql
from lxml import etree

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
request = requests.get('http://www.open.com.cn/major/?b=7&page=1',headers=header)
request.encoding='utf-8'
c = request.text

ztui = []
zh = re.compile('<div.*?class="major-channel-list">.*?<ul>(.*?)</ul>.*?</div>',re.S)
zheng =re.findall(zh,c)
for t in zheng:
    zh2 = re.compile('<strong.*?class="title-com major-labels">(.*?)</strong>',re.S)
    t2 = re.findall(zh2,t)
    for t3 in t2:
        t4 = t3.strip()
        t5 = re.sub('<i.*?>|</i>','',t4)
        t6 = '1' if '特色专业' in t5 else '0'
        ztui.append(t6)

print(ztui)
print(len(ztui))