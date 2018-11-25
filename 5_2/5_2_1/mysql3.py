import pymysql

# spiders表插入数据
id = '20120001'
name = 'jason'
age = 20
db = pymysql.connect(host='localhost', user='root', password='jason123', port=3306, db='spiders')
cursor = db.cursor()
# sql = 'INSERT INTO students(id,name,age) values(%s,%s,%s)'
# try:
#     cursor.execute(sql, (id, name, age))
#     db.commit()
# except:
#     db.rollback()
# db.close()
data = {
    'id': '20120003',
    'name': 'Tom',
    'age': 22
}
table = 'students'
# 输出 ID，name，age
key = ','.join(data.keys())
# 有几个字段构造几个%s
values = ','.join(['%s'] * len(data))
sql = 'INSERT INTO {table}({key}) VALUES ({values})'.format(table=table, key=key, values=values)
try:
    if cursor.execute(sql, tuple(data.values())):
        print("Successful")
        db.commit()
except:
    print("Failed")
    db.rollback()
db.close()
