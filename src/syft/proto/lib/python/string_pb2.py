# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/python/string.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/lib/python/string.proto",
    package="syft.lib.python",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=_b(
        '\n\x1dproto/lib/python/string.proto\x12\x0fsyft.lib.python\x1a%proto/core/common/common_object.proto"9\n\x06String\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\x12!\n\x02id\x18\x02 \x01(\x0b\x32\x15.syft.core.common.UIDb\x06proto3'
    ),
    dependencies=[
        proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,
    ],
)


_STRING = _descriptor.Descriptor(
    name="String",
    full_name="syft.lib.python.String",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="data",
            full_name="syft.lib.python.String.data",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="id",
            full_name="syft.lib.python.String.id",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=89,
    serialized_end=146,
)

_STRING.fields_by_name[
    "id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
DESCRIPTOR.message_types_by_name["String"] = _STRING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

String = _reflection.GeneratedProtocolMessageType(
    "String",
    (_message.Message,),
    dict(
        DESCRIPTOR=_STRING,
        __module__="proto.lib.python.string_pb2"
        # @@protoc_insertion_point(class_scope:syft.lib.python.String)
    ),
)
_sym_db.RegisterMessage(String)


# @@protoc_insertion_point(module_scope)
