# coding:utf-8

import grpc
import single1_pb2 as pb2
import single1_pb2_grpc as pb2_grpc
import time

from concurrent import futures  # 创建线程数量


class World(pb2_grpc.WorldServicer):
    def HelloWorld(self, request, context):
        name = request.name
        age = request.age
        result = f'my name is {name}, i am {age} years old.'
        return pb2.HelloWorldReply(result=result)

    def TestClientRecvStream(self, request, context):
        index = 0
        while context.is_active():  # 服务端监听客户端是否处于活跃状态
            data = request.data

            # 如何主动关闭与客户端的长连接
            if data == 'close':
                 print('data is close, request will cancel.')
                 context.cancel()

            time.sleep(1)
            index += 1
            result = 'send %d %s' % (index, data)
            print(result)
            yield pb2.TestClientRecvStreamResponse(
                result = result
            )
            # return 

def run():
    grpc_server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=4)
    )
    pb2_grpc.add_WorldServicer_to_server(World(), grpc_server)
    grpc_server.add_insecure_port('127.0.0.1:5000')
    print('server will start at 127.0.0.1:5000')
    grpc_server.start()

    try:
        while 1:
            time.sleep(3600)
        
    except KeyboardInterrupt:
        grpc_server.stop(0)


if __name__ == '__main__':
    run()