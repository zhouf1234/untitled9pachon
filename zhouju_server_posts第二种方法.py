#-*-coding:utf-8-*-
# 服务大厅文章
import requests
import io
import sys
import re
from pyquery import PyQuery as pq
import pymysql
import time
import json




id_count = 1
def load_url(url):
    # 分类链接列表，里面还包含分类名
    port_link_list = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
    }
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码
    html = requests.get(url,headers=headers)
    # 匹配文章模块
    port = re.search('报考服务.*?权威查询',html.text,re.S)
    port2 = re.search('常见下载.*?</dd>',html.text,re.S)
    doc = pq(port.group(0))
    doc1 = pq(port2.group(0))
    # 分类链接
    port_link = doc('a')
    port_links = doc1('a')
    for i in port_link.items():
        port_link_list.append(['http://www.open.com.cn' + i.attr('href'),i.text()])
    for s in port_links.items():
        if 'help' in s.attr('href'):
            port_link_list.append(['http://www.open.com.cn' + s.attr('href'),s.text()])
    # print(port_link_list)
    return(port_link_list)


def get_port(port_link):
    global id_count
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
    }
    # 遍历链接
    for i in port_link:
        title_list = []
        title_link = []
        # 来源
        more = []
        # 时间
        more1 = []
        index_html = requests.get(i[0],headers=headers)
        # 正则匹配页数
        page = re.search('pagination.*?共(.*?)页',index_html.text,re.S).group(1)
        # 分页访问
        for pages in range(1,int(page) + 1):
            url = i[0] + '?page=' + str(pages)
            port_html = requests.get(url,headers=headers)
            doc = pq(port_html.text)
            titles = doc.find('dl')
            title = doc.find('h4 a')
            # 文章名字
            title_list += title.text().replace('奥鹏','舟炬').split(' ')
            # 文章链接
            for links in title.items():
                if not 'http' in links.attr('href'):
                    title_link.append('http://www.open.com.cn' + links.attr('href'))
                else:
                    title_link.append(links.attr('href'))
            # 文章来源
            more += re.findall('来源：(.*?)</span>',port_html.text,re.S)
            more1 += re.findall('时间：(.*?)</span>',port_html.text,re.S)
        count = 0
        print(title_link)
        for auth in title_link:
            print(auth)
            auth_html = requests.get(auth,headers=headers)
            doc = pq(auth_html.text)
            # 阅读人数
            views = doc('.icon-eye').parent().remove('i').text()
            if not views:
                views = None
            print('阅读人数',views)
            # 正文内容
            content = doc('.server-content').children()
            if not content:
                content = None
            else:
                content = str(content).replace('奥鹏','舟炬')
            # 标签
            tags = doc('.fl span').text()
            tags = tags.split(' ')
            # 来源链接
            l_link = doc('.fr').text().replace('来源：','').replace('open.com.cn','zhoujuedu.com').rstrip('/')
            if not l_link:
                l_link = 'http://www.zhoujuedu.com'

            morex = more[count]
            if morex == '':
                morex = '舟炬教育'
            db = pymysql.connect(host="localhost", user="root", password='123123', port=3306, db='zhouju')
            cursor = db.cursor()
            sql = 'SELECT id FROM zhouju_server_categorys WHERE catename= "%s"' %i[1]
            cursor.execute(sql)
            # 查询父id
            cateid = cursor.fetchone()[0]
            # print('父iD',cateid)
            sql1 = 'INSERT INTO zhouju_server_posts(id,post_title,source,source_link,post_content,edit_time,views,cateid,keywords,is_status) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            try:
                cursor.execute(sql1,(id_count,title_list[count],str(morex).replace('奥鹏','舟炬'),l_link,content,time.mktime(time.strptime(str(more1[count]).rstrip(' '), '%Y-%m-%d')),views,cateid,json.dumps(tags),1))
                db.commit()
            except:
                db.rollback()
                print('ERROR')
            db.close()
            id_count += 1
            count += 1



def main():
    url = 'http://www.open.com.cn/help/148.html'
    port_link = load_url(url)
    get_port(port_link)


if __name__ == '__main__':
    main()