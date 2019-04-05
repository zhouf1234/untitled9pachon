import os

filepath = './01'
if not os.path.exists(filepath):    #如果文件夹不存在就创建
    os.mkdir(filepath)

p2 =filepath + '/%s.txt'%1
print(p2)
with open(p2,'w',encoding = 'gbk') as f:
    f.write('你好吗')
