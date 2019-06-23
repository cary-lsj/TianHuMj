# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game_end.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import pai_pb2 as pai__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='game_end.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0egame_end.proto\x1a\tpai.proto\"\xac\x02\n\tGamerInfo\x12\x1f\n\x08gamerPai\x18\x01 \x02(\x0b\x32\r.GamerPaiPool\x12\x11\n\tnGameCoin\x18\x02 \x02(\x05\x12\x0b\n\x03\x62Hu\x18\x03 \x02(\x08\x12\r\n\x05\x62Ting\x18\x04 \x02(\x08\x12\x11\n\tnHuOPList\x18\x05 \x03(\x05\x12\x0b\n\x03nID\x18\x06 \x01(\x05\x12\r\n\x05\x62\x42oss\x18\x07 \x01(\x08\x12\x13\n\x05hupai\x18\x08 \x01(\x0b\x32\x04.Pai\x12\x0f\n\x07huCount\x18\t \x01(\x05\x12\x12\n\nmoBaoCount\x18\n \x01(\x05\x12\x11\n\tziMoCount\x18\x0b \x01(\x05\x12\x11\n\tgangCount\x18\x0c \x01(\x05\x12\x14\n\x0c\x64ianPaoCount\x18\r \x01(\x05\x12\x16\n\x0e\x64\x61nJuBestCount\x18\x0e \x01(\x05\x12\x12\n\ntotalScore\x18\x0f \x01(\x05\"_\n\rGameEndNotify\x12\x11\n\x03\x62\x61o\x18\x01 \x01(\x0b\x32\x04.Pai\x12\x1c\n\x08infoList\x18\x02 \x03(\x0b\x32\n.GamerInfo\x12\x0e\n\x06\x62Huang\x18\x03 \x01(\x08\x12\r\n\x05\x62Over\x18\x04 \x01(\x08')
  ,
  dependencies=[pai__pb2.DESCRIPTOR,])




_GAMERINFO = _descriptor.Descriptor(
  name='GamerInfo',
  full_name='GamerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gamerPai', full_name='GamerInfo.gamerPai', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nGameCoin', full_name='GamerInfo.nGameCoin', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bHu', full_name='GamerInfo.bHu', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bTing', full_name='GamerInfo.bTing', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nHuOPList', full_name='GamerInfo.nHuOPList', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nID', full_name='GamerInfo.nID', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bBoss', full_name='GamerInfo.bBoss', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hupai', full_name='GamerInfo.hupai', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='huCount', full_name='GamerInfo.huCount', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='moBaoCount', full_name='GamerInfo.moBaoCount', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ziMoCount', full_name='GamerInfo.ziMoCount', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gangCount', full_name='GamerInfo.gangCount', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dianPaoCount', full_name='GamerInfo.dianPaoCount', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='danJuBestCount', full_name='GamerInfo.danJuBestCount', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='totalScore', full_name='GamerInfo.totalScore', index=14,
      number=15, type=5, cpp_type=1, label=1,
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
  serialized_start=30,
  serialized_end=330,
)


_GAMEENDNOTIFY = _descriptor.Descriptor(
  name='GameEndNotify',
  full_name='GameEndNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bao', full_name='GameEndNotify.bao', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='infoList', full_name='GameEndNotify.infoList', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bHuang', full_name='GameEndNotify.bHuang', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bOver', full_name='GameEndNotify.bOver', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=332,
  serialized_end=427,
)

_GAMERINFO.fields_by_name['gamerPai'].message_type = pai__pb2._GAMERPAIPOOL
_GAMERINFO.fields_by_name['hupai'].message_type = pai__pb2._PAI
_GAMEENDNOTIFY.fields_by_name['bao'].message_type = pai__pb2._PAI
_GAMEENDNOTIFY.fields_by_name['infoList'].message_type = _GAMERINFO
DESCRIPTOR.message_types_by_name['GamerInfo'] = _GAMERINFO
DESCRIPTOR.message_types_by_name['GameEndNotify'] = _GAMEENDNOTIFY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GamerInfo = _reflection.GeneratedProtocolMessageType('GamerInfo', (_message.Message,), dict(
  DESCRIPTOR = _GAMERINFO,
  __module__ = 'game_end_pb2'
  # @@protoc_insertion_point(class_scope:GamerInfo)
  ))
_sym_db.RegisterMessage(GamerInfo)

GameEndNotify = _reflection.GeneratedProtocolMessageType('GameEndNotify', (_message.Message,), dict(
  DESCRIPTOR = _GAMEENDNOTIFY,
  __module__ = 'game_end_pb2'
  # @@protoc_insertion_point(class_scope:GameEndNotify)
  ))
_sym_db.RegisterMessage(GameEndNotify)


# @@protoc_insertion_point(module_scope)