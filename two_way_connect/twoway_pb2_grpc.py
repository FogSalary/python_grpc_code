# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import twoway_pb2 as twoway__pb2

GRPC_GENERATED_VERSION = '1.65.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.66.0'
SCHEDULED_RELEASE_DATE = 'August 6, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in twoway_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class WorldStub(object):
    """import ""

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.HelloWorld = channel.unary_unary(
                '/test.World/HelloWorld',
                request_serializer=twoway__pb2.HelloWorldReq.SerializeToString,
                response_deserializer=twoway__pb2.HelloWorldReply.FromString,
                _registered_method=True)
        self.HelloTest = channel.stream_stream(
                '/test.World/HelloTest',
                request_serializer=twoway__pb2.HelloTestRequest.SerializeToString,
                response_deserializer=twoway__pb2.HelloTestResponse.FromString,
                _registered_method=True)
        self.TestClientRecvStream = channel.unary_stream(
                '/test.World/TestClientRecvStream',
                request_serializer=twoway__pb2.TestClientRecvStreamRequest.SerializeToString,
                response_deserializer=twoway__pb2.TestClientRecvStreamResponse.FromString,
                _registered_method=True)
        self.TestClientSendStream = channel.stream_unary(
                '/test.World/TestClientSendStream',
                request_serializer=twoway__pb2.TestClientSendStreamRequest.SerializeToString,
                response_deserializer=twoway__pb2.TestClientSendStreamResponse.FromString,
                _registered_method=True)
        self.TestTwoWayStream = channel.stream_stream(
                '/test.World/TestTwoWayStream',
                request_serializer=twoway__pb2.TestTwoWayStreamRequest.SerializeToString,
                response_deserializer=twoway__pb2.TestTwoWayStreamResponse.FromString,
                _registered_method=True)


class WorldServicer(object):
    """import ""

    """

    def HelloWorld(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HelloTest(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestClientRecvStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestClientSendStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestTwoWayStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WorldServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'HelloWorld': grpc.unary_unary_rpc_method_handler(
                    servicer.HelloWorld,
                    request_deserializer=twoway__pb2.HelloWorldReq.FromString,
                    response_serializer=twoway__pb2.HelloWorldReply.SerializeToString,
            ),
            'HelloTest': grpc.stream_stream_rpc_method_handler(
                    servicer.HelloTest,
                    request_deserializer=twoway__pb2.HelloTestRequest.FromString,
                    response_serializer=twoway__pb2.HelloTestResponse.SerializeToString,
            ),
            'TestClientRecvStream': grpc.unary_stream_rpc_method_handler(
                    servicer.TestClientRecvStream,
                    request_deserializer=twoway__pb2.TestClientRecvStreamRequest.FromString,
                    response_serializer=twoway__pb2.TestClientRecvStreamResponse.SerializeToString,
            ),
            'TestClientSendStream': grpc.stream_unary_rpc_method_handler(
                    servicer.TestClientSendStream,
                    request_deserializer=twoway__pb2.TestClientSendStreamRequest.FromString,
                    response_serializer=twoway__pb2.TestClientSendStreamResponse.SerializeToString,
            ),
            'TestTwoWayStream': grpc.stream_stream_rpc_method_handler(
                    servicer.TestTwoWayStream,
                    request_deserializer=twoway__pb2.TestTwoWayStreamRequest.FromString,
                    response_serializer=twoway__pb2.TestTwoWayStreamResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'test.World', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('test.World', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class World(object):
    """import ""

    """

    @staticmethod
    def HelloWorld(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/test.World/HelloWorld',
            twoway__pb2.HelloWorldReq.SerializeToString,
            twoway__pb2.HelloWorldReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def HelloTest(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/test.World/HelloTest',
            twoway__pb2.HelloTestRequest.SerializeToString,
            twoway__pb2.HelloTestResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def TestClientRecvStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/test.World/TestClientRecvStream',
            twoway__pb2.TestClientRecvStreamRequest.SerializeToString,
            twoway__pb2.TestClientRecvStreamResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def TestClientSendStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(
            request_iterator,
            target,
            '/test.World/TestClientSendStream',
            twoway__pb2.TestClientSendStreamRequest.SerializeToString,
            twoway__pb2.TestClientSendStreamResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def TestTwoWayStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/test.World/TestTwoWayStream',
            twoway__pb2.TestTwoWayStreamRequest.SerializeToString,
            twoway__pb2.TestTwoWayStreamResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
