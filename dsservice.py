import json
import time
import tornado.web
import myconfig
from tornado.ioloop import IOLoop
from tornado import gen
import tornado.options
from mongo_interactive import MongodbInteractive
tornado.options.parse_command_line()


class DeviceShadowService(tornado.web.RequestHandler):
    """与mongodb交互，对状态数据进行操作"""
    @gen.coroutine
    def get(self):
        """连接GET请求"""
        product_id = self.get_argument('product_id')
        devicename = self.get_argument('devicename')

        obj = MongodbInteractive()
        # 查找数据
        query_data = obj.mongodb_query(product_id, devicename)
        print(query_data)

    @gen.coroutine
    def post(self):
        """连接POST请求"""
        # 请求数据
        req_data = self.request.body
        data_dict = json.loads(req_data)
        product_id = data_dict["product_id"]
        devicename = data_dict["devicename"]
        self.post_data_process(product_id, devicename)

    @gen.coroutine
    def post_data_process(self, product_id, devicename):
        obj = MongodbInteractive()
        # 查找
        ret = obj.mongodb_query(product_id, devicename)
        if ret:
            # 更新
            update_data = {'product_id': product_id, 'devicename': devicename, 'state': {"color": 'green'}, 'id': 22}
            ret = obj.mongodb_update(product_id, devicename, update_data)
            print('--update----', ret['n'])
            self.write('--update---OK--')
        else:
            # 插入数据
            data = {'product_id': product_id, 'devicename': devicename, 'state': {"color": 'red'}, 'id': 11}
            obj.mongodb_insert(data)
            self.write('--insert--OK--')


def make_app():
    return tornado.web.Application([
            (r"/", DeviceShadowService)
        ], **myconfig.settings)


def start(port):
    app = make_app()
    app.listen(port=port)
    IOLoop.current().start()


if __name__ == '__main__':
    start(8000)
