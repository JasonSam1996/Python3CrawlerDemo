import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='jason123',
                     port=3306,
                     db='spiders')
cursor = db.cursor()
# 更新数据
# sql = 'UPDATE students SET age = %s WHERE name = %s'
# try:
#     cursor.execute(sql, (25, 'jason'))
#     db.commit()
# except:
#     db.rollback()
# db.close()
# 去重，如果数据存在，则更新数据，如果数据不存在，则插入数据
data = {
    'id': '20120001',
    'name': 'jason',
    'age': 20
}
table = 'students'
key = ','.join(data.keys())
values = ','.join(['%s'] * len(data))
# ON DUPLICATE KEY UPDATE 这行代码的意思是如果主键已经存在，就执行更新操作
sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE ' \
      ''.format(table=table, keys=key, values=values)
update = ','.join([" {key} = %s".format(key=key) for key in data])
sql += update
try:
    if cursor.execute(sql, tuple(data.values()) * 2):
        print("Successful")
        db.commit()
except:
    print("Failed")
    db.rollback()
db.close()
