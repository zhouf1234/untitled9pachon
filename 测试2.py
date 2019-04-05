# 院校特征表zhouju_shool_features   第二种方法，不用一页一页上传了

import requests
import re
import pymysql
from lxml import etree

# # http://www.open.com.cn/major/index.html?page=1

tes = [] # 八大特征
yuans = [] #35所院校
tezs = []  #所有院校特征
for i in range(1,3):    #总共两页
    # print(i)
    url = 'http://www.open.com.cn/school/index.html?page=' + str(i)
    print(url)
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    request = requests.get(url, headers=header)
    request.encoding = 'utf-8'
    c = request.text
    # print(len(c))

    html = etree.HTML(c)
    te = html.xpath('//td[@class="area-ele aw_tag"]/a/text()')
    # print(te)  # 八大特征
    for i in te:
        if i not in tes:
            tes.append(i)
    yuan = html.xpath('//div[@class="clear list-item"]//dl//dt//a//img/@title')
    # print(yuan)
    for j in yuan:
        if j not in yuans:
            yuans.append(j)

    zh = re.compile('<div.*?class="clear list-item">.*?<dl>.*?<dd>.*?<p.*?>(.*?)</p>.*?</dd>.*?</dl>.*?</div>', re.S)
    zheng = re.findall(zh, c)
    # print(zheng)
    for i in zheng:
        # print(i)
        zh2 = re.compile('<span>(.*?)</span>', re.S)
        zheng2 = re.findall(zh2, i)
        # print(zheng2)
        tezs.append(zheng2)

# print(tes)
# print(yuans)
# print(tezs)
dictionary = list(zip(tezs, yuans))     #特征和学校名合并为列表
# print(dictionary)
for i in dictionary:
    # print(i[0][2:])
    for j in i[0][2:]:
        # print(j)
        if j in tes[0]:
            tez = {'feature_name':tes[0],'notes':i[1]}
            print(tez)  #两页的特征和学校都出来了，一个特征一个特征上传mysql数据库即可