#院校信息表zhouju_schools  :
# 尝试更新院校对应的院校类型表的id,更新成功

import pymysql

ylei = []
db = pymysql.connect(host='localhost',user = 'root',password='123456',port=3306,db='zhouju2')
cursor = db.cursor()
table= 'zhouju_scholl_types'   #定义表名
sql = 'SELECT * FROM {table} WHERE id '.format(table=table)
cursor.execute(sql)
row = cursor.fetchone()
while row:              #每循环一次，指针偏移一条数据，简单高效
    # print(row)
    yl = {'name':row[2],'school_type':row[0]}
    ylei.append(yl)
    row = cursor.fetchone()

print(ylei)
# for l in ylei:
    # print(l['name'])
    # print(l['school_type'])

    # db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='zhouju2')
    # cursor = db.cursor()
    # sn = l['name']
    # sc = l['school_type']
    # keys = ','.join(l.keys())    #keys函数，取出键名，并用逗号拼接
    # # print(keys)
    # sql="UPDATE zhouju_schools SET school_type= '%s' WHERE name= '%s'" %(sc,sn)
    # print(sql)
    # cursor.execute(sql)
    # db.commit() #执行数据插入
    # db.close()