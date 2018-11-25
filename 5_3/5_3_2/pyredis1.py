# coding=utf-8
from redis import StrictRedis, ConnectionPool

# redis存储
# 正常连接
# redis = StrictRedis(password='admin123')
# 使用ConnectionPool连接
# pool = ConnectionPool(host='localhost', port=6379, db=0, password='admin123')
# redis = StrictRedis(connection_pool=pool)
# 使用URL方式连接
url = 'redis://:admin123@localhost:6379/0'
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)
redis.set('name', 'Bob')
print(redis.get('name'))
