#-*-conding:utf-8-*-
#模拟题表zhouju_aquestions（本次只北京语言大学，国际经济与贸易专业，专升本层次），未关联外键，上传时显示外键约束失败1452
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from lxml import etree
import requests
import re
import pymysql
import time

if __name__ == "__main__":
    # chrome_options = Options()
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--headless')
    # abspath = os.path.abspath(r"D:\chromedriver_win32\chromedriver.exe")
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2767.400"
    }
    dr = webdriver.Chrome()
    dr.get('http://www.open.com.cn/service/examdownload.html')
    # drop = dr.find_element_by_id('school').find_element_by_tag_name("option")[2].click()
    Select(dr.find_element_by_id("school")).select_by_index(1)
    time.sleep(3)
    Select(dr.find_element_by_id("major")).select_by_value("4333")
    time.sleep(3)
    Select(dr.find_element_by_id("level")).select_by_visible_text("专升本")
    time.sleep(3)
    dr.find_element_by_id("submit").click()
    time.sleep(3)
    html = dr.page_source
    html1 = etree.HTML(html)
    requd1f = html1.xpath('//td[@class="mock-name"]//text()')
    print(requd1f)
    requd1f2 = html1.xpath('//td[@class="mock-opt"]//@href')
    print(requd1f2)
    url = []
    for i in requd1f2:
        ie = 'http://www.open.com.cn'+i
        url.append(ie)
    print(url)
    requd1f3 = html1.xpath('//option[@value="10032"]//text()')
    requd1f3[0] = requd1f3[0].replace(' ', '')
    print(requd1f3)
    requd1f4 = html1.xpath('//option[@value="4333"]//text()')
    requd1f4[0] = requd1f4[0].replace(' ', '')
    print(requd1f4)
    requd1f5 = html1.xpath('//option[@value="942"]//text()')
    requd1f5[0] = requd1f5[0].replace(' ', '')
    print(requd1f5)
    db = pymysql.connect(host="localhost", user="root", password='123456', port=3306, db='zhouju2')
    cursor = db.cursor()
    sql = "SELECT id FROM zhouju_schools WHERE name='%s'" % (requd1f3[0])
    db.ping(reconnect=True)
    cursor.execute(sql)
    major_id = cursor.fetchone()
    major_id = major_id[0]
    sql2 = "SELECT id FROM zhouju_majors WHERE school='%s'" % (major_id)
    cursor.execute(sql2)
    major_id2 = cursor.fetchone()
    major_id2 = major_id2[0]
    print(major_id)
    print(major_id2)
    levels = {
        '高起专': 0,
        '高起本': 1,
        '专升本': 2
    }
    num_id = 1
    for i in range(0,len(url)):
        cursor = db.cursor()
        sql = 'INSERT INTO zhouju_aquestions(id,name,filename,sccholl_id,major_cate_id,leval,addtime,is_status) values(%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql,(num_id,requd1f[i],url[i],major_id,major_id2,levels[requd1f5[0]],None,1))
        db.commit()
        num_id += 1
    db.close()


