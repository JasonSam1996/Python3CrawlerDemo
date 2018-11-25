import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students
# 偏移，在某些情况下，我们可能想只取某几个元素，这时可以利用skip()方法偏移几个位置，另外，还可以用limit()方法指定要取得结果个数
results = collection.find().sort('name', pymongo.ASCENDING).skip(5).limit(6)
print([result['name'] for result in results])
# 值得注意的是，在数据库量非常庞大的时候，如千万、亿级别，
# 最好不要使用大的偏移量来查询数据，因为这样很可能导致内存溢出
# 可以通过objectID来查询
