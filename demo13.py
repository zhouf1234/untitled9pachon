#专业信息表zhouju_majors，更新数据方法学校id
import pymysql

# 去school表查数据，取id，拼接字典，既然建立了学校名的字段，那就考虑用更新数据的方法吧
zs = []
db = pymysql.connect(host='localhost',user = 'root',password='123456',port=3306,db='zhouju2')
cursor = db.cursor()
table= 'zhouju_schools'   #定义表名
sql = 'SELECT * FROM {table} WHERE id '.format(table=table)     #查询表所有id,获取所有信息，只能查id了
cursor.execute(sql)
row = cursor.fetchone()
while row:              #每循环一次，指针偏移一条数据，简单高效
    row2 = {'schoolsssss':row[1],'school':row[0]}
    zs.append(row2)
    row = cursor.fetchone()

print(zs)
# for s in zs:
#     # print(s['schoolsssss'])
#     # print(s['school'])
#     db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='zhouju2')
#     cursor = db.cursor()
#     sn = s['schoolsssss']
#     sc = s['school']
#     sql="UPDATE zhouju_majors SET school= '%s' WHERE schoolsssss= '%s'" %(sc,sn)
#     print(sql)
#     cursor.execute(sql)
#     db.commit() #执行数据插入
#     db.close()