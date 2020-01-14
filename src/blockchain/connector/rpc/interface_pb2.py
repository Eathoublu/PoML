# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: interface.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='interface.proto',
    package='',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=_b(
        '\n\x0finterface.proto\"\'\n\x05\x42\x61tch\x12\x10\n\x08\x62\x61tch_id\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\"1\n\x10Training_request\x12\x0c\n\x04\x66uel\x18\x01 \x03(\t\x12\x0f\n\x07\x66urnace\x18\x02 \x03(\t\"3\n\x1d\x46\x65tch_training_result_request\x12\x12\n\ntrainingId\x18\x01 \x01(\t\"\x85\x01\n\x06Result\x12 \n\x04\x63ode\x18\x01 \x01(\x0e\x32\x12.Result.StatusCode\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"D\n\nStatusCode\x12\x0b\n\x07SUCCESS\x10\x00\x12\x13\n\x0fINVALID_REQUEST\x10\x01\x12\x14\n\x10\x43ONSENSUS_FAILED\x10\x02\x32\x93\x01\n\tConsensus\x12\x1f\n\x0cUpload_batch\x12\x06.Batch\x1a\x07.Result\x12#\n\x05Train\x12\x11.Training_request\x1a\x07.Result\x12@\n\x15\x46\x65tch_training_result\x12\x1e.Fetch_training_result_request\x1a\x07.Resultb\x06proto3')
)

_RESULT_STATUSCODE = _descriptor.EnumDescriptor(
    name='StatusCode',
    full_name='Result.StatusCode',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='SUCCESS', index=0, number=0,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='INVALID_REQUEST', index=1, number=1,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CONSENSUS_FAILED', index=2, number=2,
            serialized_options=None,
            type=None),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=230,
    serialized_end=298,
)
_sym_db.RegisterEnumDescriptor(_RESULT_STATUSCODE)

_BATCH = _descriptor.Descriptor(
    name='Batch',
    full_name='Batch',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='batch_id', full_name='Batch.batch_id', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='data', full_name='Batch.data', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=19,
    serialized_end=58,
)

_TRAINING_REQUEST = _descriptor.Descriptor(
    name='Training_request',
    full_name='Training_request',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='fuel', full_name='Training_request.fuel', index=0,
            number=1, type=9, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='furnace', full_name='Training_request.furnace', index=1,
            number=2, type=9, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=60,
    serialized_end=109,
)

_FETCH_TRAINING_RESULT_REQUEST = _descriptor.Descriptor(
    name='Fetch_training_result_request',
    full_name='Fetch_training_result_request',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='trainingId', full_name='Fetch_training_result_request.trainingId', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=111,
    serialized_end=162,
)

_RESULT = _descriptor.Descriptor(
    name='Result',
    full_name='Result',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='code', full_name='Result.code', index=0,
            number=1, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='description', full_name='Result.description', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
        _RESULT_STATUSCODE,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=165,
    serialized_end=298,
)

_RESULT.fields_by_name['code'].enum_type = _RESULT_STATUSCODE
_RESULT_STATUSCODE.containing_type = _RESULT
DESCRIPTOR.message_types_by_name['Batch'] = _BATCH
DESCRIPTOR.message_types_by_name['Training_request'] = _TRAINING_REQUEST
DESCRIPTOR.message_types_by_name['Fetch_training_result_request'] = _FETCH_TRAINING_RESULT_REQUEST
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Batch = _reflection.GeneratedProtocolMessageType('Batch', (_message.Message,), {
    'DESCRIPTOR': _BATCH,
    '__module__': 'interface_pb2'
    # @@protoc_insertion_point(class_scope:Batch)
})
_sym_db.RegisterMessage(Batch)

Training_request = _reflection.GeneratedProtocolMessageType('Training_request', (_message.Message,), {
    'DESCRIPTOR': _TRAINING_REQUEST,
    '__module__': 'interface_pb2'
    # @@protoc_insertion_point(class_scope:Training_request)
})
_sym_db.RegisterMessage(Training_request)

Fetch_training_result_request = _reflection.GeneratedProtocolMessageType('Fetch_training_result_request',
                                                                         (_message.Message,), {
                                                                             'DESCRIPTOR': _FETCH_TRAINING_RESULT_REQUEST,
                                                                             '__module__': 'interface_pb2'
                                                                             # @@protoc_insertion_point(class_scope:Fetch_training_result_request)
                                                                         })
_sym_db.RegisterMessage(Fetch_training_result_request)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {
    'DESCRIPTOR': _RESULT,
    '__module__': 'interface_pb2'
    # @@protoc_insertion_point(class_scope:Result)
})
_sym_db.RegisterMessage(Result)

_CONSENSUS = _descriptor.ServiceDescriptor(
    name='Consensus',
    full_name='Consensus',
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=301,
    serialized_end=448,
    methods=[
        _descriptor.MethodDescriptor(
            name='Upload_batch',
            full_name='Consensus.Upload_batch',
            index=0,
            containing_service=None,
            input_type=_BATCH,
            output_type=_RESULT,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name='Train',
            full_name='Consensus.Train',
            index=1,
            containing_service=None,
            input_type=_TRAINING_REQUEST,
            output_type=_RESULT,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name='Fetch_training_result',
            full_name='Consensus.Fetch_training_result',
            index=2,
            containing_service=None,
            input_type=_FETCH_TRAINING_RESULT_REQUEST,
            output_type=_RESULT,
            serialized_options=None,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_CONSENSUS)

DESCRIPTOR.services_by_name['Consensus'] = _CONSENSUS

# @@protoc_insertion_point(module_scope)