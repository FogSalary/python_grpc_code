# coding:utf-8

import grpc
import twoway_pb2 as pb2
import twoway_pb2_grpc as pb2_grpc
import time
import random


def test():
    # 如何让客户端主动与服务器端断开链接
    index = 0
    while 1:
        time.sleep(1)
        data = str(random.random())
        if index == 5:
            break
        print(index)
        index += 1
        yield pb2.TestClientSendStreamRequest(data= data)

def run():
    conn = grpc.insecure_channel('127.0.0.1:5000')
    client = pb2_grpc.WorldStub(channel=conn)
    # resposne = client.HelloWorld(pb2.HelloWorldReq(
    #     name="victor",
    #     age = 33
    # ))
    # response = client.TestClientRecvStream(pb2.TestClientRecvStreamRequest(
    #     data = "victor"
    # ))

    # for item in response:
    #     print(item.result)

    # response = client.TestClientSendStream(test())

    # print(response.result)

    response = client.TestTwoWayStream(test())
    # 超时机制
    # response = client.TestTwoWayStream(test(), timeout=10)
    for res in response:
        print(res.result)





if __name__ == '__main__':
    run()
