import json
import logging
import requests
from ws4py.client.threadedclient import WebSocketClient
logging.basicConfig(level=logging.INFO)
loger = logging.getLogger(__name__)
loger.setLevel(logging.INFO)
"""根据jemter 的连接方式尝试"""


def get_sid(req,host):
    re = requests.get('{}{}'.format(req,host))
    s = str(re.content)
    print(s)
    re_str = s[17:-1]
    dict_str = json.loads(re_str)
    return dict_str.get('sid')

def conn_socket(req,host):
    ws = create_connection('{}{}&sid={}'.format(req,host,get_sid('http://',host)))
    if ws.sock is not None:
        loger.info('连接成功')
    return ws


def conn_socket_ws4py():
    pass

class Clientsocket(WebSocketClient):
    def received_message(self, message):
        print(message)

    def opened(self):
        self.send('111')
        loger.info('发送成功1111')

    def closed(self, code, reason=None):
        loger.info('连接关闭，code{} ，原因 {} '.format(code,reason))




"""问题：连接成功后会断开"""
if __name__ == '__main__':
    # host = 'tst-redcentermahjong-stg90.1768.com/socket.io/?EIO=3&transport=polling&t=1443084886884-0'
    # a = requests.get('http://{}&sid={}'.format(host,get_sid('http://',host)))
    # print(a.text)
    # ws = conn_socket('ws://',host)
    # ws1 = Clientsocket('ws://tst-redcentermahjong-stg90.1768.com/socket.io/?EIO=3&transport=polling&t=1443084886884-0&sid={}'.format(get_sid('http://',host))
    #                   )
    ws1 = Clientsocket(
        'ws://127.0.0.1:8000')
    try:
        ws1.connect()
    except Exception as e:
        print(e)
    ws1.run_forever()


    # print(ws1.key)
    # print(ws1.host)
    #握手信息
    #loger.info('握手信息 ==={}==== '.format(ws1.handshake_request))

    #print(ws1.handshake_request)


    # try:
    #     ws1.connect()
    # except Exception as e:
    #     print(e)
    # ws1.run_forever()

    # except Exception as e:
    #     loger.info('{},连接失败'.format(e))
    # websocket.enableTrace(True)
    # ws = websocket.WebSocketApp('ws://tst-redcentermahjong-stg90.1768.com/socket.io/?EIO=3&transport=polling&t=1443084886884-0&sid={}'.format(get_sid(host))
    #                             )
    # ws.run_forever(ping_interval=5,ping_timeout=1)









