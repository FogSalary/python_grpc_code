# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: single2.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rsingle2.proto\x12\x04test\"*\n\rHelloWorldReq\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x05\"!\n\x0fHelloWorldReply\x12\x0e\n\x06result\x18\x01 \x01(\t\"\xc1\x01\n\x10HelloTestRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x03\x12\x0c\n\x04\x64\x61te\x18\x03 \x03(\t\x12\x32\n\x06number\x18\x04 \x03(\x0b\x32\".test.HelloTestRequest.NumberEntry\x1aP\n\x0bNumberEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x30\n\x05value\x18\x02 \x01(\x0b\x32!.test.HelloTestRequestNumberValue:\x02\x38\x01\"K\n\x1bHelloTestRequestNumberValue\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x05\x12\x11\n\tis_active\x18\x03 \x01(\x08\"\x13\n\x11HelloTestResponse\"+\n\x1bTestClientRecvStreamRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\".\n\x1cTestClientRecvStreamResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"+\n\x1bTestClientSendStreamRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\".\n\x1cTestClientSendStreamResponse\x12\x0e\n\x06result\x18\x01 \x01(\t2\xcd\x02\n\x05World\x12:\n\nHelloWorld\x12\x13.test.HelloWorldReq\x1a\x15.test.HelloWorldReply\"\x00\x12\x42\n\tHelloTest\x12\x16.test.HelloTestRequest\x1a\x17.test.HelloTestResponse\"\x00(\x01\x30\x01\x12\x61\n\x14TestClientRecvStream\x12!.test.TestClientRecvStreamRequest\x1a\".test.TestClientRecvStreamResponse\"\x00\x30\x01\x12\x61\n\x14TestClientSendStream\x12!.test.TestClientSendStreamRequest\x1a\".test.TestClientSendStreamResponse\"\x00(\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'single2_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_HELLOTESTREQUEST_NUMBERENTRY']._loaded_options = None
  _globals['_HELLOTESTREQUEST_NUMBERENTRY']._serialized_options = b'8\001'
  _globals['_HELLOWORLDREQ']._serialized_start=23
  _globals['_HELLOWORLDREQ']._serialized_end=65
  _globals['_HELLOWORLDREPLY']._serialized_start=67
  _globals['_HELLOWORLDREPLY']._serialized_end=100
  _globals['_HELLOTESTREQUEST']._serialized_start=103
  _globals['_HELLOTESTREQUEST']._serialized_end=296
  _globals['_HELLOTESTREQUEST_NUMBERENTRY']._serialized_start=216
  _globals['_HELLOTESTREQUEST_NUMBERENTRY']._serialized_end=296
  _globals['_HELLOTESTREQUESTNUMBERVALUE']._serialized_start=298
  _globals['_HELLOTESTREQUESTNUMBERVALUE']._serialized_end=373
  _globals['_HELLOTESTRESPONSE']._serialized_start=375
  _globals['_HELLOTESTRESPONSE']._serialized_end=394
  _globals['_TESTCLIENTRECVSTREAMREQUEST']._serialized_start=396
  _globals['_TESTCLIENTRECVSTREAMREQUEST']._serialized_end=439
  _globals['_TESTCLIENTRECVSTREAMRESPONSE']._serialized_start=441
  _globals['_TESTCLIENTRECVSTREAMRESPONSE']._serialized_end=487
  _globals['_TESTCLIENTSENDSTREAMREQUEST']._serialized_start=489
  _globals['_TESTCLIENTSENDSTREAMREQUEST']._serialized_end=532
  _globals['_TESTCLIENTSENDSTREAMRESPONSE']._serialized_start=534
  _globals['_TESTCLIENTSENDSTREAMRESPONSE']._serialized_end=580
  _globals['_WORLD']._serialized_start=583
  _globals['_WORLD']._serialized_end=916
# @@protoc_insertion_point(module_scope)
