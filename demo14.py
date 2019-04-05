#专业信息表zhouju_majors，实际取的是专业小类名称对应的院校信息，分页面如http://www.open.com.cn/major/19414.html
# 因为总共50页，上千条的数据，建议去大类的url取数据，16个大类，一个大类一个大类的取，即一个url一个url分别取
# demo12数据太多，分出此文件来取分页面的图片并保存
#此次只取小类图片，有重复的图片连接要去重，此次分别保存在了16个文件夹里

import requests
import re
import pymysql
import os
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


yximage = []   #图片连接列表，要做去重处理
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

        html3 = etree.HTML(c3)

        #去每个专业类下的院校的分页面url取内容，如http://www.open.com.cn/major/19414.html
        zyurl = html3.xpath('//div[@class="major-channel-list"]//ul//li//dl[1]//dt/a/@href')
        for yu in zyurl:
            yu2 = 'http://www.open.com.cn'+yu
            header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
            req = requests.get(yu2, headers=header)
            req.encoding = 'utf-8'
            c4 = req.text

            #大类下每所专业院校的图片，此次只取一张，因为其他的7张都是重复的，到时候直接取随意一个院校的就可
            html4 = etree.HTML(c4)
            zyimage = html4.xpath('//div[@class="major-detail clear"]//div//div//div//div[2]//img[1]/@src')
            # print(zyimage)
            for z in zyimage:
                z2 = 'http://www.open.com.cn'+z
                yximage.append(z2)

yximage2 = set(yximage)     #去重处理后要变回列表
yximage3 = list(yximage2)
# print(yximage3)
# print(type(yximage3))

for j in range(len(yximage3)):         #遍历所有图片url，并保存到本地路径，放在文件夹里，已成功
    # print("%s" % (yximage3[j]))
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

    request = requests.get(yximage3[j],headers=header)

    filepath = './16'
    if not os.path.exists(filepath):  # 如果文件夹不存在就创建
        os.mkdir(filepath)
    p2 = filepath + '/%s.jpg' % j
    # print(p2)
    # with open(p2, "wb")as f:
    #     f.write(request.content)


#最后16个url页面中分页面的剩余的相同的6张图片取一下保存,此次已成功保存
header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
reqs = requests.get('http://www.open.com.cn/major/19414.html', headers=header)
reqs.encoding = 'utf-8'
c5 = reqs.text

#大类下专业院校的图片，其他的7张,取一次就可，保存在data3
html4 = etree.HTML(c5)
zyimage2 = html4.xpath('//div[@class="major-detail clear"]//div//div//div//div[2]//img/@src')
# print(zyimage)
for zz in range(len(zyimage2[1:])):
    zz2 = 'http://www.open.com.cn'+(zyimage2[1:])[zz]
    # print(zz2)
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

    req2 = requests.get(zz2,headers=header)

    filepath = './data3'
    if not os.path.exists(filepath):  # 如果文件夹不存在就创建
        os.mkdir(filepath)
    p2 = filepath + '/%s.jpg' % zz
    print(p2)
    # with open(p2, "wb")as f:
    #     f.write(req2.content)



