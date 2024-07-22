# coding:utf-8

import grpc
import twoway_pb2 as pb2
import twoway_pb2_grpc as pb2_grpc
import time

from concurrent import futures  # 创建线程数量


class World(pb2_grpc.WorldServicer):
    def HelloWorld(self, request, context):
        name = request.name
        age = request.age

        # 返回错误码与错误信息
        # if conditions:
        # context.set_details('haha bug')
        # # context.set_details(json.dumps{'code': sub_code, 'msg': 'xxxx'})  # 40301 missing 4030 arg error
        # context.set_code(grpc.StatusCode.DATA_LOSS)
        # raise context

        # 从服务端往客户端传输添加 headers 方法
        # context.set_trailing_metadata(((),(),()))
        context.set_trailing_metadata((('name', 'victor'),('key', 'value')))

        # 服务器端接受客户端 headers
        headers = context.invocation_metadata()
        print(headers)
        print(headers[0].key, headers[0].value)

        result = f'my name is {name}, i am {age} years old.'
        # 压缩方式一
        context.set_compression(grpc.Compression.Gzip)  # dir(grpc.Compression) Deflate
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

    def TestClientSendStream(self, request_iterator, context):
        index = 0
        for request in request_iterator:
            print(request.data, ":", index)
            if index == 10:
                break
            index += 1

        return pb2.TestClientSendStreamResponse(result = 'ok')

    def TestTwoWayStream(self, request_iterator, context):
        index = 0
        for request in request_iterator:
            # 从客户端获取流
            data = request.data
            if index == 3:
                context.cancel()
            index += 1
            result = 'service send client %s' % data
            yield pb2.TestTwoWayStreamResponse(result = result)

def run():
    # grpc_server = grpc.server(
    #     futures.ThreadPoolExecutor(max_workers=4)
    # )
    # 方法二 让所有服务都可压缩
    # grpc_server = grpc.server(
    #     futures.ThreadPoolExecutor(max_workers=4),
    #     compression=grpc.Compression.Gzip
    # )

    # 增加传输流量
    grpc_server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=4),
        compression=grpc.Compression.Gzip,
        options=[
            ("grpc.max_send_message_length", 50 * 1024 * 1024),
            ("grpc.max_receive_message_length", 50 * 1024 * 1024)
            ]
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