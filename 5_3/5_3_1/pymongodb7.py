import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students
# 更新数据
# condition = {'name': 'jason'}
# student = collection.find_one(condition)
# student['age'] = 25
# result = collection.update(condition, student)
# print(result)
# # 另外，我们也可以使用$set操作符对数据进行更新
# result = collection.update(condition, {'$set': student})
# print(result)
# 这样可以只更新student字典内存在的字段。如果原先还有其他字段，则不会更新，也不会删除。
# 而个不用$set的话，则会把之前的数据全部用student字典替换；如果原本存在其他字段，则会被删除
# 另外update官方不推荐

# condition = {'name': 'sam'}
# student = collection.find_one(condition)
# student['age'] = 18
# result = collection.update_one(condition, {'$set': student})
# print(result)
# print(result.matched_count, result.modified_count)
# update_many
condition = {'age': {'$gte': 20}}
result = collection.update_many(condition, {'$inc': {'age': 1}})
print(result)
print(result.matched_count, result.modified_count)
