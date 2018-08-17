import time
from urllib.error import URLError
import gevent
from urllib import request
import http.client
import requests
import json
import random

from gevent import monkey
# 补丁
monkey.patch_all()


url = 'http://127.0.0.1:8000/'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'
}


def run():
    # 请求数据
    random_str = ''.join(random.sample(['a', 'b', 'c', '1', '2', '3'], 3))
    product_id = str(random.randint(1000, 1010))
    devicename = random_str
    request_data = {'product_id': product_id, 'devicename': devicename}
    req_data = json.dumps(request_data)
    data = req_data.encode(encoding='utf-8')

    try:
        # s1:request请求
        # req = request.Request(url=url, data=data, headers=headers, method="POST")
        # response = request.urlopen(req)
        # resp = response.read()
        # print("服务器返回值为:\n", resp.decode('utf-8'))

        # s2:httpclient请求
        httpclient = http.client.HTTPConnection(host='127.0.0.1', port=8000)
        # httpclient = http.client.HTTPConnection(host='120.78.163.250', port=8000)
        httpclient.request("POST", '/', data, headers)
        response = httpclient.getresponse()
        print(response.read().decode())

        # s3:requests请求
        # resp = requests.post(url=url, data=data, headers=headers)
        # print("状态:\n", resp)
        # print("请求头:\n", resp.headers)
        # print("服务器返回值为:\n", resp.content.decode())
    except URLError as e:
        print('请求', e)
    except Exception as e:
        print('请求错误：', e)


if __name__ == '__main__':
    begin_time = time.time()

    run_gevent_list = []
    for i in range(200):
        print('------%d--Test------' % i)
        run_gevent_list.append(gevent.spawn(run))
    gevent.joinall(run_gevent_list)

    end = time.time()
    print('测试时间（累计）:', end-begin_time)
