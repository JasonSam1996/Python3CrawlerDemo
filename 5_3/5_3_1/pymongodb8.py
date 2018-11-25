import pymongo

client = pymongo.MongoClient(host='localhost',port=27017)
db = client.test
collection = db.students
# 删除数据
result = collection.delete_one({'name':'jason'})
print(result)
print(result.deleted_count)
result = collection.delete_many({'name':'jason'})
print(result.deleted_count)