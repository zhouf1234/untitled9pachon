import pymysql

ls = []
db = pymysql.connect(host='localhost',user = 'root',password='123456',port=3306,db='zhouju2')
cursor = db.cursor()
table= 'zhouju_scholl_types'   #定义表名
sql = 'SELECT * FROM {table} WHERE id '.format(table=table)     #查询表所有id
cursor.execute(sql)
row = cursor.fetchone()
while row:              #每循环一次，指针偏移一条数据，简单高效
    print(row)
    ls.append(row[0])
    row = cursor.fetchone()
print(ls)

