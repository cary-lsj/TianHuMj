# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exchange.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='exchange.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0e\x65xchange.proto\"P\n\x0f\x45xchangeRequest\x12\x0f\n\x07nUserID\x18\x01 \x02(\x05\x12\x1c\n\x05nType\x18\x02 \x02(\x0e\x32\r.EnumExchange\x12\x0e\n\x06nCount\x18\x03 \x01(\x05\"f\n\x10\x45xchangeResponse\x12\x12\n\nnErrorCode\x18\x01 \x02(\x05\x12\x1c\n\x05nType\x18\x02 \x02(\x0e\x32\r.EnumExchange\x12\x0f\n\x07nCountL\x18\x03 \x01(\x05\x12\x0f\n\x07nCountR\x18\x04 \x01(\x05*0\n\x0c\x45numExchange\x12\x10\n\x0c\x43RYSTAL2GOLD\x10\x00\x12\x0e\n\nGOLD2POWER\x10\x01')
)

_ENUMEXCHANGE = _descriptor.EnumDescriptor(
  name='EnumExchange',
  full_name='EnumExchange',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CRYSTAL2GOLD', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOLD2POWER', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=204,
  serialized_end=252,
)
_sym_db.RegisterEnumDescriptor(_ENUMEXCHANGE)

EnumExchange = enum_type_wrapper.EnumTypeWrapper(_ENUMEXCHANGE)
CRYSTAL2GOLD = 0
GOLD2POWER = 1



_EXCHANGEREQUEST = _descriptor.Descriptor(
  name='ExchangeRequest',
  full_name='ExchangeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nUserID', full_name='ExchangeRequest.nUserID', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nType', full_name='ExchangeRequest.nType', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nCount', full_name='ExchangeRequest.nCount', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=98,
)


_EXCHANGERESPONSE = _descriptor.Descriptor(
  name='ExchangeResponse',
  full_name='ExchangeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nErrorCode', full_name='ExchangeResponse.nErrorCode', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nType', full_name='ExchangeResponse.nType', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nCountL', full_name='ExchangeResponse.nCountL', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nCountR', full_name='ExchangeResponse.nCountR', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=202,
)

_EXCHANGEREQUEST.fields_by_name['nType'].enum_type = _ENUMEXCHANGE
_EXCHANGERESPONSE.fields_by_name['nType'].enum_type = _ENUMEXCHANGE
DESCRIPTOR.message_types_by_name['ExchangeRequest'] = _EXCHANGEREQUEST
DESCRIPTOR.message_types_by_name['ExchangeResponse'] = _EXCHANGERESPONSE
DESCRIPTOR.enum_types_by_name['EnumExchange'] = _ENUMEXCHANGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExchangeRequest = _reflection.GeneratedProtocolMessageType('ExchangeRequest', (_message.Message,), dict(
  DESCRIPTOR = _EXCHANGEREQUEST,
  __module__ = 'exchange_pb2'
  # @@protoc_insertion_point(class_scope:ExchangeRequest)
  ))
_sym_db.RegisterMessage(ExchangeRequest)

ExchangeResponse = _reflection.GeneratedProtocolMessageType('ExchangeResponse', (_message.Message,), dict(
  DESCRIPTOR = _EXCHANGERESPONSE,
  __module__ = 'exchange_pb2'
  # @@protoc_insertion_point(class_scope:ExchangeResponse)
  ))
_sym_db.RegisterMessage(ExchangeResponse)


# @@protoc_insertion_point(module_scope)