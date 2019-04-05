#友情连接表zhouju_links,已经上传
import requests
import re
import pymysql

# db = pymysql.connect(host='localhost',user='root',password='123456',port=3306,db='zhouju2')
# cursor=db.cursor()
list = ['id','link_title','url','is_status']
ldian = dict.fromkeys(list)
hear = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
lian = requests.get('http://www.open.com.cn/',headers=hear).text
lian1 = re.search('友情链接.*?</dd>',lian,re.S)
lian2=str(lian1.group())
wen = re.findall('<a.*?>(.*?)</a>',lian2,re.S)
lurl = re.findall('href="(.*?)"',lian2,re.S)
for i in range(0,len(wen)):
    ldian['id']=i+1
    ldian['link_title']=wen[i]
    ldian['url']=lurl[i]
    ldian['is_status']=1
    table='zhouju_links'
    keys = ','.join(ldian.keys())
    val = ','.join(['%s']*len(ldian))
#     sql = 'insert into {table}({keys}) values ({val})'.format(table=table,keys=keys,val=val)
#     try:
#         cursor.execute(sql,tuple(ldian.values()))
#         db.commit()
#     except:
#         db.rollback()
# db.close()


