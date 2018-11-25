import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)

db = client.test

collection = db.students

# 排序 ASC指定升序，DESC降序
results = collection.find().sort('name', pymongo.ASCENDING)
print([result['name'] for result in results])
