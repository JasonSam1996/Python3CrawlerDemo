# coding=utf-8
from redis import StrictRedis

redis = StrictRedis(password='admin123')
# 字符串操作
# 给数据库中键名为name的string赋予值value
print(redis.set('name', 'jason'))
# 返回数据库中键名为name的string的value
print(redis.get('name'))
# 给数据库中键名name的string赋予值value并返回上一次的value
print(redis.getset('name', 'sam'))
# 返回多个键对应的value组成的列表
print(redis.mget(['name', 'nickname']))
# 如果不存在这个键值对，则更新value，否则不变
print(redis.setnx('newname', 'Tom'))
