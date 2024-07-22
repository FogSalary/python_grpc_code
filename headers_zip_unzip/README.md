
[Python-GRPC](https://www.bilibili.com/video/BV1Bk4y167r8/?spm_id_from=333.788&vd_source=6164de2a185f949293fb3064a50fdb40)


python-grpc 课程
- grpc-python01 引言
- grpc-python02 了解 rpc 与 grpc 以及创建一个简单的 grpc-python
- grpc-python03 常用 protobuf 数据类型和 pb 文件
- grpc-python04 单向流之服务器端向客户端传输
- grpc-python05 客户端流请求-以及新专题预告
- grpc-python06 双向流与强制和友好断开与超时机制
- grpc-python07 错误码与服务端客户端发送与接受错误信息
- grpc-python08 headers 与压缩与传输最大值
- grpc-python09 service 拦截器与寻求淘宝开店教程
- grpc-python10 多进程启动 grpcpython 服务
- grpc-python11 grpc-web 与 envoy 上篇与慕课 2020 年 python 全栈开发入门课程推荐
- grpc-python12 最终章-如何做 restful 以及女儿友情参与
- grpc-python13 不依赖 proto 动态请求 grpc 服务器端


微服务
GRPC-GO


```
pip install grpcio
pip install protobuf
pip install grpcio-tools
```


什么是 rpc ？什么是 grpc？
<a href=""><div align=center><img src=".\images\learn_grpc01.png" alt="demo" border="0" width="600"/></div></a>

<a href=""><div align=center><img src=".\images\learn_grpc02.png" alt="demo" border="0" width="600"/></div></a>

<a href=""><div align=center><img src=".\images\learn_grpc03.png" alt="demo" border="0" width="600"/></div></a>

<a href=""><div align=center><img src=".\images\learn_grpc04.png" alt="demo" border="0" width="600"/></div></a>


编写好 proto 文件后，需要使用 tools 将其转换为 python 文件
```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. hello_world.proto
```


## grpc-python03 常用 protobuf 数据类型和 pb 文件
Protobuf 数据类型定义
Python pb 文件

<a href=""><div align=center><img src=".\images\learn_grpc05.png" alt="demo" border="0" width="600"/></div></a>

<a href=""><div align=center><img src=".\images\learn_grpc06.png" alt="demo" border="0" width="600"/></div></a>

**_pb2.py 文件介绍**
每一个 message 对应的信息存储，比如我们的 request 与 response 在这里被定义 extension


**_pb2_grpc.py 文件介绍**
- 用来存储每一个服务的 server 与客户端以及注册 server 的工具
- 客户端名为：service_name + Stub
- 服务器名为：service_name + Serivcer
- 注册服务为：add_服务端名_to_server

```

```


## grpc-python04 单向流之服务器端向客户端传输

传输方式
1. unary 单程
2. stream 流
   1. 双向传输，客户端请求服务器端（流），服务器端返回给客户端（流）
   2. 单向传输，服务器端接收到客户端（流），服务器端返回给客户端（非流）；客户端保持跟服务器的长连接
   3. 单向传输，服务器端接收到客户端（非流），服务器端send给客户端（流）；服务器端和客户端保持长连接


流会不断给另一方发送消息，而非流则不会；
单向流实际也是双方建立了一个长链接，只是某一方主动向另一方一直发起流的数据；



## grpc-python05 客户端流请求-以及新专题预告

客户端不断地向服务器端发送信息，服务器端则不断地接受，达到一定状态时则断开请求并返回最后一次的结果；

## grpc-python06 双向流与强制和友好断开与超时机制
单向流的两种传输方式：
1. 客户端接收流的方式，服务器端如何给客户端发起流；
2. 客户端主动发起流，服务端接收流的方式


双向流传输方式：


## grpc-python07 错误码与服务端客户端发送与接受错误信息

GRPC 状态码与返回接收的用法

服务端如何返回状态码，客户端如何接收状态码；

成功的 Code 码
- code: 0 -> ok

失败的 Code 码
<a href=""><div align=center><img src=".\images\learn_grpc07.png" alt="demo" border="0" width="800"/></div></a>

<a href=""><div align=center><img src=".\images\learn_grpc08.png" alt="demo" border="0" width="800"/></div></a>



## grpc-python08 headers 与压缩与传输最大值

- 客户端与服务端相互传输与接收 headers key value  （metadata）
- 客户端与服务端传输数据与接收数据 进行压缩与解压缩


## grpc-python09 service 拦截器与寻求淘宝开店教程


## grpc-python10 多进程启动 grpcpython 服务


## grpc-python11 grpc-web 与 envoy 上篇与慕课 2020 年 python 全栈开发入门课程推荐


## grpc-python12 最终章-如何做 restful 以及女儿友情参与


## grpc-python13 不依赖 proto 动态请求 grpc 服务器端