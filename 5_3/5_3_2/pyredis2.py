# coding=utf-8
from redis import StrictRedis, ConnectionPool

# redis存储
# 正常连接
redis = StrictRedis(password='admin123')
redis.set('name', 'Bob')
print(redis.get('name'))
# 键操作
# 判断一个键是否存在
print(redis.exists('name'))
# 删除一个键
print(redis.delete('name'))
# 判断键类型
print(redis.type('name'))
# 获取所有符合规则的键
print(redis.keys('n*'))
# 获取随机的一个键
print(redis.randomkey())
# 重命名键
print(redis.rename('name','nickname'))
# 获取当前数据库中键的数目
print(redis.dbsize())
# 设置键的过期时间，单位为秒
print(redis.expire('name',2))
# 获取键的过期时间，单位为秒，-1表示永久不过期
print(redis.ttl('name'))
# 将键移动到其他数据库，db:数据库代号
print(redis.move('name', 2))
# 删除当前选择数据库中的所有键
print(redis.flushdb())
# 删除所有数据库中的所有键
print(redis.flushall())