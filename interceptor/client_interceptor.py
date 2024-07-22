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
    try:
        # resposne = client.HelloWorld(pb2.HelloWorldReq(
        # 客户端接收来自服务端的 headers
        # response, call = client.HelloWorld.with_call(pb2.HelloWorldReq(
        #     name="victor",
        #     age = 33
        # ))
        # 客户端发送 headers 信息给服务器端
        # response, call = client.HelloWorld.with_call(pb2.HelloWorldReq(
        #     name="victor",
        #     age = 33
        # ), metadata=(('client_key', 'client_value'),))
        # 压缩方法
        response, call = client.HelloWorld.with_call(pb2.HelloWorldReq(
            name="victor",
            age = 33
        # ), compression=grpc.Compression.Gzip, metadata=(('client_key', 'client_value'),))
        ), compression=grpc.Compression.Gzip, metadata=(('name', 'victor'),))

        print(response.result)
        headers = call.trailing_metadata()
        print(headers[0][0])
        print(headers[0][1])
        print(dir(headers[0]))
        print(headers[0].key, headers[0].value)
        print(call.trailing_metadata())

        # help(client.HelloWorld.with_call)
    except Exception as e:
        # print(dir(e))
        print(e.code())
        print(e.details())
        print(e.code().name, e.code().value)
    # response = client.TestClientRecvStream(pb2.TestClientRecvStreamRequest(
    #     data = "victor"
    # ))

    # for item in response:
    #     print(item.result)

    # response = client.TestClientSendStream(test())

    # print(response.result)

    # response = client.TestTwoWayStream(test())
    # # 超时机制
    # # response = client.TestTwoWayStream(test(), timeout=10)
    # for res in response:
    #     print(res.result)





if __name__ == '__main__':
    run()
