# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: create_dele_room.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import gameplay_pb2 as gameplay__pb2
import assets_pb2 as assets__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='create_dele_room.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x16\x63reate_dele_room.proto\x1a\x0egameplay.proto\x1a\x0c\x61ssets.proto\"j\n\x15\x43reateDeleRoomRequest\x12\x0f\n\x07nUserID\x18\x01 \x02(\x05\x12\x11\n\tsCardType\x18\x02 \x02(\t\x12\x1b\n\x08gamePlay\x18\x03 \x02(\x0b\x32\t.GamePlay\x12\x10\n\x08nPlayers\x18\x04 \x02(\x05\"\xa0\x01\n\x16\x43reateDeleRoomResponse\x12\x12\n\nnErrorCode\x18\x01 \x02(\x05\x12\x0f\n\x07sRoomID\x18\x02 \x01(\t\x12\x11\n\tsCardType\x18\x03 \x01(\t\x12\x1b\n\x08gamePlay\x18\x04 \x01(\x0b\x32\t.GamePlay\x12\x10\n\x08nPlayers\x18\x05 \x01(\x05\x12\x1f\n\tnewAssets\x18\x06 \x01(\x0b\x32\x0c.AssetUpdate')
  ,
  dependencies=[gameplay__pb2.DESCRIPTOR,assets__pb2.DESCRIPTOR,])




_CREATEDELEROOMREQUEST = _descriptor.Descriptor(
  name='CreateDeleRoomRequest',
  full_name='CreateDeleRoomRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nUserID', full_name='CreateDeleRoomRequest.nUserID', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sCardType', full_name='CreateDeleRoomRequest.sCardType', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gamePlay', full_name='CreateDeleRoomRequest.gamePlay', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nPlayers', full_name='CreateDeleRoomRequest.nPlayers', index=3,
      number=4, type=5, cpp_type=1, label=2,
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
  serialized_start=56,
  serialized_end=162,
)


_CREATEDELEROOMRESPONSE = _descriptor.Descriptor(
  name='CreateDeleRoomResponse',
  full_name='CreateDeleRoomResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nErrorCode', full_name='CreateDeleRoomResponse.nErrorCode', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sRoomID', full_name='CreateDeleRoomResponse.sRoomID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sCardType', full_name='CreateDeleRoomResponse.sCardType', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gamePlay', full_name='CreateDeleRoomResponse.gamePlay', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nPlayers', full_name='CreateDeleRoomResponse.nPlayers', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='newAssets', full_name='CreateDeleRoomResponse.newAssets', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=165,
  serialized_end=325,
)

_CREATEDELEROOMREQUEST.fields_by_name['gamePlay'].message_type = gameplay__pb2._GAMEPLAY
_CREATEDELEROOMRESPONSE.fields_by_name['gamePlay'].message_type = gameplay__pb2._GAMEPLAY
_CREATEDELEROOMRESPONSE.fields_by_name['newAssets'].message_type = assets__pb2._ASSETUPDATE
DESCRIPTOR.message_types_by_name['CreateDeleRoomRequest'] = _CREATEDELEROOMREQUEST
DESCRIPTOR.message_types_by_name['CreateDeleRoomResponse'] = _CREATEDELEROOMRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateDeleRoomRequest = _reflection.GeneratedProtocolMessageType('CreateDeleRoomRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEDELEROOMREQUEST,
  __module__ = 'create_dele_room_pb2'
  # @@protoc_insertion_point(class_scope:CreateDeleRoomRequest)
  ))
_sym_db.RegisterMessage(CreateDeleRoomRequest)

CreateDeleRoomResponse = _reflection.GeneratedProtocolMessageType('CreateDeleRoomResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATEDELEROOMRESPONSE,
  __module__ = 'create_dele_room_pb2'
  # @@protoc_insertion_point(class_scope:CreateDeleRoomResponse)
  ))
_sym_db.RegisterMessage(CreateDeleRoomResponse)


# @@protoc_insertion_point(module_scope)
