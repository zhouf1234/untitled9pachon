import pymysql
#院校特征，恐怕得用更新数据的方法了


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
print(ret)



