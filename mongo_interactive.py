import myconfig


class MongodbInteractive:
    def __init__(self):
        self.collections = myconfig.COLLECTIONS

    def mongodb_insert(self, data):
        """增"""
        info_dict = data
        return self.collections.insert(info_dict)

    def mongodb_delete(self, product_id, devicename):
        """删"""
        self.collections.delete_one({"product_id": product_id, "devicename": devicename})

    def mongodb_update(self, product_id, devicename, data):
        """改"""
        info_dict = data
        return self.collections.update({"product_id": product_id, "devicename": devicename}, {'$set': info_dict})

    def mongodb_query(self, product_id, devicename):
        """查"""
        query_data = self.collections.find_one({"product_id": product_id, "devicename": devicename}, {"_id": 0})
        return query_data
