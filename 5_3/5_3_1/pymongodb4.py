import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)

db = client.test

collection = db.students

# 计数
count = collection.find().count()
print(count)
count = collection.find({'age':20}).count()
print(count)