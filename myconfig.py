#!/usr/bin/env python3
from pymongo import MongoClient


# Tornado app配置
settings = {
    # 'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
    # 'static_path': os.path.join(os.path.dirname(__file__), 'statics'),
    'debug': True,
}

MONGOCLIENT = MongoClient("mongodb://user:password@120.78.163.250:27017/")
# 数据库
DB = MONGOCLIENT["dsservice_test_db"]
# 设备影子集合
COLLECTIONS = DB["ds_test_col"]

