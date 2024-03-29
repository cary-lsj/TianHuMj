# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: buy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import assets_pb2 as assets__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='buy.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\tbuy.proto\x1a\x0c\x61ssets.proto\"#\n\x04Good\x12\x0b\n\x03nID\x18\x01 \x02(\x05\x12\x0e\n\x06nCount\x18\x02 \x01(\x05\"3\n\nBuyRequest\x12\x0f\n\x07nUserID\x18\x01 \x02(\x05\x12\x14\n\x05goods\x18\x02 \x03(\x0b\x32\x05.Good\"B\n\x0b\x42uyResponse\x12\x12\n\nnErrorCode\x18\x01 \x02(\x05\x12\x1f\n\tnewAssets\x18\x02 \x01(\x0b\x32\x0c.AssetUpdate\"8\n\x0f\x41ppleBuyRequest\x12\x0f\n\x07nUserID\x18\x01 \x02(\x05\x12\x14\n\x05goods\x18\x02 \x03(\x0b\x32\x05.Good\"G\n\x10\x41ppleBuyResponse\x12\x12\n\nnErrorCode\x18\x01 \x02(\x05\x12\x1f\n\tnewAssets\x18\x02 \x02(\x0b\x32\x0c.AssetUpdate')
  ,
  dependencies=[assets__pb2.DESCRIPTOR,])




_GOOD = _descriptor.Descriptor(
  name='Good',
  full_name='Good',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nID', full_name='Good.nID', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nCount', full_name='Good.nCount', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=27,
  serialized_end=62,
)


_BUYREQUEST = _descriptor.Descriptor(
  name='BuyRequest',
  full_name='BuyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nUserID', full_name='BuyRequest.nUserID', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='goods', full_name='BuyRequest.goods', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=64,
  serialized_end=115,
)


_BUYRESPONSE = _descriptor.Descriptor(
  name='BuyResponse',
  full_name='BuyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nErrorCode', full_name='BuyResponse.nErrorCode', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='newAssets', full_name='BuyResponse.newAssets', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=117,
  serialized_end=183,
)


_APPLEBUYREQUEST = _descriptor.Descriptor(
  name='AppleBuyRequest',
  full_name='AppleBuyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nUserID', full_name='AppleBuyRequest.nUserID', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='goods', full_name='AppleBuyRequest.goods', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=185,
  serialized_end=241,
)


_APPLEBUYRESPONSE = _descriptor.Descriptor(
  name='AppleBuyResponse',
  full_name='AppleBuyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nErrorCode', full_name='AppleBuyResponse.nErrorCode', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='newAssets', full_name='AppleBuyResponse.newAssets', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=243,
  serialized_end=314,
)

_BUYREQUEST.fields_by_name['goods'].message_type = _GOOD
_BUYRESPONSE.fields_by_name['newAssets'].message_type = assets__pb2._ASSETUPDATE
_APPLEBUYREQUEST.fields_by_name['goods'].message_type = _GOOD
_APPLEBUYRESPONSE.fields_by_name['newAssets'].message_type = assets__pb2._ASSETUPDATE
DESCRIPTOR.message_types_by_name['Good'] = _GOOD
DESCRIPTOR.message_types_by_name['BuyRequest'] = _BUYREQUEST
DESCRIPTOR.message_types_by_name['BuyResponse'] = _BUYRESPONSE
DESCRIPTOR.message_types_by_name['AppleBuyRequest'] = _APPLEBUYREQUEST
DESCRIPTOR.message_types_by_name['AppleBuyResponse'] = _APPLEBUYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Good = _reflection.GeneratedProtocolMessageType('Good', (_message.Message,), dict(
  DESCRIPTOR = _GOOD,
  __module__ = 'buy_pb2'
  # @@protoc_insertion_point(class_scope:Good)
  ))
_sym_db.RegisterMessage(Good)

BuyRequest = _reflection.GeneratedProtocolMessageType('BuyRequest', (_message.Message,), dict(
  DESCRIPTOR = _BUYREQUEST,
  __module__ = 'buy_pb2'
  # @@protoc_insertion_point(class_scope:BuyRequest)
  ))
_sym_db.RegisterMessage(BuyRequest)

BuyResponse = _reflection.GeneratedProtocolMessageType('BuyResponse', (_message.Message,), dict(
  DESCRIPTOR = _BUYRESPONSE,
  __module__ = 'buy_pb2'
  # @@protoc_insertion_point(class_scope:BuyResponse)
  ))
_sym_db.RegisterMessage(BuyResponse)

AppleBuyRequest = _reflection.GeneratedProtocolMessageType('AppleBuyRequest', (_message.Message,), dict(
  DESCRIPTOR = _APPLEBUYREQUEST,
  __module__ = 'buy_pb2'
  # @@protoc_insertion_point(class_scope:AppleBuyRequest)
  ))
_sym_db.RegisterMessage(AppleBuyRequest)

AppleBuyResponse = _reflection.GeneratedProtocolMessageType('AppleBuyResponse', (_message.Message,), dict(
  DESCRIPTOR = _APPLEBUYRESPONSE,
  __module__ = 'buy_pb2'
  # @@protoc_insertion_point(class_scope:AppleBuyResponse)
  ))
_sym_db.RegisterMessage(AppleBuyResponse)


# @@protoc_insertion_point(module_scope)
