import random
from mongo_interactive import MongodbInteractive


random_str = ''.join(random.sample(['a', 'b', 'c', 'd', 'e', 'f', '1', '2', '3'], 5))
# 请求数据
product_id = str(random.randint(1000, 2000))
devicename = random_str
print(product_id)
print(devicename)


obj = MongodbInteractive()
ret = obj.mongodb_query(product_id, devicename)
print(ret)
if ret:
    print('true')
else:
    print('none')