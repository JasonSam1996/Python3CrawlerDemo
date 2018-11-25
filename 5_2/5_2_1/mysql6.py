import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='jason123',
                     port=3306,
                     db='spiders')
cursor = db.cursor()
# 查询数据
sql = 'SELECT * FROM students WHERE age >= 20'
# try:
#     cursor.execute(sql)
#     print('Count:', cursor.rowcount)
#     # 获取第一条数据,返回结果是元组形式
#     one = cursor.fetchone()
#     print('One:', one)
#     # 得到结果的所有数据，因为上次取值之后，指针偏移到吓一跳数据，所有返回的是取第一条值后面的所有数据
#     results = cursor.fetchall()
#     print('Results:', results)
#     print('Results Type', type(results))
#     for row in results:
#         print(row)
# except:
#     print('Error')
# 此外，我们还可以用while循环加fetchone()方法来获取所有数据，而不是用fetchall()全部一起获取出来
try:
    cursor.execute(sql)
    print('Count',cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:',row)
        row = cursor.fetchone()
except:
    print('Error')
