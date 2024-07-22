# coding:utf-8

import grpc
import single1_pb2 as pb2
import single1_pb2_grpc as pb2_grpc


def run():
    conn = grpc.insecure_channel('127.0.0.1:5000')
    client = pb2_grpc.WorldStub(channel=conn)
    # resposne = client.HelloWorld(pb2.HelloWorldReq(
    #     name="victor",
    #     age = 33
    # ))
    response = client.TestClientRecvStream(pb2.TestClientRecvStreamRequest(
        data = "victor"
    ))

    for item in response:
        print(item.result)


if __name__ == '__main__':
    run()
