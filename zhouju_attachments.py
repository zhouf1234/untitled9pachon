#-*-conding:utf-8-*-
# 附件表zhouju_attachments，学习中心的课件播放器下载页面
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
import requests
import re
import pymysql
import time

def StopItera(dr,header,url2b):
   dr.get(url2b)
   html = dr.page_source
   html2 = etree.HTML(html)
   sqld = html2.xpath('//div[@class="news-box"]//a//@href')
   url_1 = []
   #name
   tname = []
   time1 = []
   turl2 = []
   ttxt = []
   for i in sqld:
        ie = 'http://www.open.com.cn'+i
        dr.get(ie)
        html2 = dr.page_source
        html3 = etree.HTML(html2)
        sqld = html3.xpath('//div[@class="new-title"]//h2//text()')
        if '奥鹏' in sqld[0]:
            sqld[0]='舟炬考试客户端'
        tname.append(sqld[0])
        sqld2 = html3.xpath('//div[@class="new-title"]//span//text()')

        sqld2[4] = sqld2[4].replace(' ', '')

        time1.append(sqld2[4])
        sqld3 = html3.xpath('//div[@class="server-content"]//a//@href')
        turl2.append(sqld3)
        sqld4 = html3.xpath('//div[@class="server-content"]//a//text()')
        ttxt.append(sqld4)

        # time.mktime(time.strptime(sqld2[4], '%Y-%m-%d'))
   print(tname)
   print(time1)

   turl2[0][0] = turl2[0][0]+'提取码: 584p'
   for i in range(0,len(turl2[1])):
       turl2[1][i] = turl2[1][i]+ttxt[1][i]
       if 'http' not in turl2[1][i]:
           turl2[1][i] = 'http://www.open.com.cn'+turl2[1][i]
   turl2[2][0] = 'http://www.open.com.cn'+turl2[2][0]
   turl2[3][0] = 'http://www.open.com.cn' + turl2[3][0]
   print(turl2)
   db = pymysql.connect(host="localhost", user="root", password='123456', port=3306, db='zhouju2')

   num_id = 1
   for i in range(0, len(tname)):
       cursor = db.cursor()
       sql = 'INSERT INTO zhouju_attachments(id,name,addtime,filename,is_status) values(%s,%s,%s,%s,%s)'

       cursor.execute(sql,(num_id,tname[i],time.mktime(time.strptime(time1[i],'%Y-%m-%d')),','.join(turl2[i]),1))
       db.commit()
       num_id += 1
   db.close()



if __name__ == "__main__":
    # chrome_options = Options()
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--headless')
    # abspath = os.path.abspath(r"D:\chromedriver_win32\chromedriver.exe")
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2767.400"
    }
    dr = webdriver.Chrome()
    url2b = 'http://www.open.com.cn/help/105.html'
    StopItera(dr,header,url2b)

