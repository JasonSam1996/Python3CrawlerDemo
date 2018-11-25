import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient(host='localhost', port=27017)

db = client.test

collection = db.students

# 查询
# 查询单条
result = collection.find_one({'name': 'jason'})
result2 = collection.find_one({'_id': ObjectId('5bf0041480c7f50eae0b6e4b')})
# 查询多条，大于20
result3 = collection.find({'age': {'$gt': 20}})
print(type(result))
print(result)
print(type(result2))
print(result2)
print(type(result3))
print(result3)
for result in result3:
    print(result)
# 正则匹配
result4 = collection.find({'name': {'$regex': 's.*'}})
print(result4)
