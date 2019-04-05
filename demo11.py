#院校信息表zhouju_schools  :
# 尝试更新院校对应的院校特征id如 [1,2] ,本次已经更新成功

import pymysql

zz = []
db = pymysql.connect(host='localhost',user = 'root',password='123456',port=3306,db='zhouju2')
cursor = db.cursor()
table= 'zhouju_shool_features'   #定义表名
sql = 'SELECT * FROM {table} WHERE id '.format(table=table)
cursor.execute(sql)
row = cursor.fetchone()
while row:              #每循环一次，指针偏移一条数据，简单高效
    # print(row)
    y = {'name': row[2], 'ind': row[0]}
    zz.append(y)
    row = cursor.fetchone()

# print(zz)
# print(type(zz))

list_dict={}
for d in zz:
    #print(d)
    if d["name"] not in list_dict:
        list_dict[d["name"]] = d
        list_dict[d["name"]]["school_feature"]=[d["ind"],]
        list_dict[d["name"]].pop("ind")
    else:
        list_dict[d["name"]]["school_feature"].append(d["ind"])
ret = list(list_dict.values())
# print(ret)

# for t in ret:
#     # print(t['name'])
#     # print(t['school_feature'])
#
#     db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='zhouju2')
#     cursor = db.cursor()
#     tn = t['name']
#     tc = t['school_feature']
#     sql="UPDATE zhouju_schools SET school_feature= '%s' WHERE name= '%s'" %(tc,tn)
#     print(sql)
#     cursor.execute(sql)
#     db.commit() #执行数据插入
#     db.close()