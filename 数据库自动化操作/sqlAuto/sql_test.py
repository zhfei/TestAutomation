#!~/Documents/pythonFiles/venv python
# -*- coding:utf-8 -*-

import MySQLdb


connect = MySQLdb.connect(
    host='192.168.1.103',
    port=3306,
    user='root',
    passwd='zhoufei@123456',
    db='course',
    charset='GBK'
)

# 通过数据库连接，拿到数据库游标
cursor = connect.cursor()

# 1.查询测试
cursor.execute('select * from table_1')

row = cursor.fetchone()
print(row)

# rows = cursor.fetchall()

# for i in range(cursor.rowcount):
#     row = cursor.fetchone()
#     print(row)

print("-"*20)

manyRow = cursor.fetchmany(3)
print(manyRow)


# 2.插入测试

cursor.execute("INSERT INTO table_1(`name`, sex, fenshu, age) VALUES('lilei2', '男', 66, 21)")
connect.commit()


# 3.批量插入
for i in range(100):
    a = i+2
    cursor.execute("INSERT INTO table_1(`name`, sex, fenshu, age) VALUES('lilei%d', '男', 66, 21)" % a)

connect.commit()
connect.close()