import pymysql

# 关系型数据库存储
# MySQL的存储
db = pymysql.connect(host='localhost', user='root', password='jason123', port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print("DataBase Version:", data)
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
db.close()
