# import pymysql
#
# # 打开数据库连接
# db = pymysql.connect(host="10.77.100.9",port=3308,user="shuang",password="shuang@123",database="ipdb")
#
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# # SQL 插入语句
# # sql = """INSERT INTO indexapp_ipdata(position,extension, ip)VALUES ('1', '1','10.77.78.1');"""
# sql = "show databases;"
# try:
#     # 执行sql语句
#     cursor.execute(sql)
#     # 提交到数据库执行
#     db.commit()
# except:
#     # 如果发生错误则回滚
#     db.rollback()
#
# # 关闭数据库连接
# db.close()

import mysql.connector

mydb = mysql.connector.connect(
    host="10.77.100.9",
    port=3308,
    user="root",
    passwd="Shuang@123",
    db='ipdb'
)

mycursor = mydb.cursor()
sql = "INSERT INTO indexapp_ipdata(position,extension,ip) VALUES (%s, %s,%s)"
#sql = "INSERT INTO indexapp_ipdata(position,extension,ip) VALUES (%s,%s,%s)"

val = ("1", "1","1.1.1.1")
# mycursor.execute()
try:
    # 执行sql语句
    mycursor.execute(sql,val)
    # 提交到数据库执行
    mydb.commit()
    print(mycursor.rowcount, "记录插入成功。")
except:
    # 如果发生错误则回滚
    print(mycursor.rowcount)
    mydb.rollback()
