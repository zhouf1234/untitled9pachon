import pymysql

# 连接入mysql数据库

# 创建数据库zhouju
# # 声明一个mysql连接对象db
# db = pymysql.connect(host='localhost',user = 'root',password='123456',port=3306)
# #获取操作游标
# cursor = db.cursor()
# # mysql语句，获取当前mysql版本
# cursor.execute('SELECT VERSION()')
# # 获取第一条数据
# data = cursor.fetchone()
# print('database version:',data)
# # 创建名为spiders的数据库
# cursor.execute('CREATE DATABASE zhouju DEFAULT CHARACTER SET utf8')
# # 关闭数据库
# db.close()


# 一：    （demo2-14）
# 无外键关联的表
# 在数据库开始建表，城市表zhouju_cityreg        ,都没有设置自增长。。。无语了，重新建库了，都设置自增长id吧
# 在数据库开始建表,院校类型表zhouju_scholl_types
# 在数据库开始建表,院校特征表zhouju_shool_features
# 在数据库开始建表,文章表zhouju_posts
# 在数据库开始建表，专业大分类表zhouju_major_cates

# 有外键关联的表
#在数据库开始建表，院校信息表zhouju_schools   #外键关联了院校类型表，特征表，文章表，城市表
# 在数据库开始建表，专业信息表zhouju_majors  #关联专业分类表，院校信息表,并下载小类里面的指定图片

# 二：(demo15)
# 无外键关联的表
#在数据库开始建表，学习中心的高校授权查询的东北师范大学的信息表zhouju_centers

#三：(demo16-18)
# 无外键关联的表
# 在数据库开始建表,服务大厅分类表zhouju_server_category
# 在数据库开始建表,服务大厅分类文章表zhouju_server_posts

#四：都未关联外键
#附件表zhouju_attachments
#模拟题表zhouju_aquestions
#友情连接表zhouju_links

#五：
#有外键关联的表
# 在数据库开始建表,院校招生简章表zhouju_school_intro         #关联院校信息表。。。。等