# coding:utf-8

import grpc
import hello_world_pb2 as pb2
import hello_world_pb2_grpc as pb2_grpc


def run():
    conn = grpc.insecure_channel('127.0.0.1:5000')
    client = pb2_grpc.WorldStub(channel=conn)
    resposne = client.HelloWorld(pb2.HelloWorldReq(
        name="victor",
        age = 33
    ))
    print(resposne.result)


if __name__ == '__main__':
    run()
