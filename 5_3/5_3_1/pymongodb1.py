import pymongo

# mongodb连接
clent = pymongo.MongoClient(host='localhost', port=27017)
# mongodb二种连接方法
# clent = pymongo.MongoClient('mongodb://localhost:27017')
# 指定数据库
db = clent.test
# db = clent['test']
# 指定集合
collection = db.students
# collection = db[students]
# 插入数据
student = {
    'id': '20170101',
    'name': 'jason',
    'age': 20,
    'gender': 'male'
}
result = collection.insert(student)
print(result)
# 插入多条数据
student2 = {
    'id':'20170202',
    'name':'sam',
    'age':20,
    'gender':'male'
}
student1 = {
    'id': '20170101',
    'name': 'jason',
    'age': 20,
    'gender': 'male'
}
student3 = {
    'id': '20170101',
    'name': 'jason',
    'age': 20,
    'gender': 'male'
}
result2 = collection.insert([student1,student2])
print(result2)
result3 = collection.insert_one(student3)
print(result3)
print(result3.inserted_id)