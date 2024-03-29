# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pai.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pai.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\tpai.proto\"$\n\x03Pai\x12\r\n\x05nType\x18\x01 \x02(\x05\x12\x0e\n\x06nValue\x18\x02 \x02(\x05\"J\n\x06\x43hiPai\x12\r\n\x05nType\x18\x01 \x02(\x05\x12\x0f\n\x07nValue1\x18\x02 \x02(\x05\x12\x0f\n\x07nValue2\x18\x03 \x02(\x05\x12\x0f\n\x07nValue3\x18\x04 \x02(\x05\"(\n\x07PengPai\x12\r\n\x05nType\x18\x01 \x02(\x05\x12\x0e\n\x06nValue\x18\x02 \x02(\x05\"<\n\x07GangPai\x12\r\n\x05nType\x18\x01 \x02(\x05\x12\x0e\n\x06nValue\x18\x02 \x02(\x05\x12\x12\n\nnGangState\x18\x03 \x02(\x05\"l\n\x08OrderPai\x12\x11\n\x03pai\x18\x01 \x01(\x0b\x32\x04.Pai\x12\x17\n\x06\x63hipai\x18\x02 \x01(\x0b\x32\x07.ChiPai\x12\x19\n\x07pengpai\x18\x03 \x01(\x0b\x32\x08.PengPai\x12\x19\n\x07gangpai\x18\x04 \x01(\x0b\x32\x08.GangPai\"(\n\x07PaiPool\x12\r\n\x05nType\x18\x01 \x02(\x05\x12\x0e\n\x06nValue\x18\x02 \x03(\x05\",\n\x08\x43\x61nHuPai\x12\x11\n\x03pai\x18\x01 \x02(\x0b\x32\x04.Pai\x12\r\n\x05\x63ount\x18\x02 \x02(\x05\":\n\x0c\x43\x61nHuPaiPool\x12\x11\n\x03pai\x18\x01 \x02(\x0b\x32\x04.Pai\x12\x17\n\x04pool\x18\x02 \x03(\x0b\x32\t.CanHuPai\"\xdc\x01\n\x0cGamerPaiPool\x12\x0b\n\x03nID\x18\x01 \x02(\x05\x12\x16\n\x04pool\x18\x02 \x03(\x0b\x32\x08.PaiPool\x12\x19\n\x07\x63hiPool\x18\x03 \x03(\x0b\x32\x08.PaiPool\x12\x1a\n\x08pengPool\x18\x04 \x03(\x0b\x32\x08.PaiPool\x12\x1b\n\tmGangPool\x18\x05 \x03(\x0b\x32\x08.PaiPool\x12\x1b\n\taGangPool\x18\x06 \x03(\x0b\x32\x08.PaiPool\x12\x19\n\x07putPool\x18\x07 \x03(\x0b\x32\x08.PaiPool\x12\x1b\n\x08orderPai\x18\x08 \x03(\x0b\x32\t.OrderPai')
)




_PAI = _descriptor.Descriptor(
  name='Pai',
  full_name='Pai',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nType', full_name='Pai.nType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nValue', full_name='Pai.nValue', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=13,
  serialized_end=49,
)


_CHIPAI = _descriptor.Descriptor(
  name='ChiPai',
  full_name='ChiPai',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nType', full_name='ChiPai.nType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nValue1', full_name='ChiPai.nValue1', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nValue2', full_name='ChiPai.nValue2', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nValue3', full_name='ChiPai.nValue3', index=3,
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
  serialized_start=51,
  serialized_end=125,
)


_PENGPAI = _descriptor.Descriptor(
  name='PengPai',
  full_name='PengPai',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nType', full_name='PengPai.nType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nValue', full_name='PengPai.nValue', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=127,
  serialized_end=167,
)


_GANGPAI = _descriptor.Descriptor(
  name='GangPai',
  full_name='GangPai',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nType', full_name='GangPai.nType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nValue', full_name='GangPai.nValue', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nGangState', full_name='GangPai.nGangState', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  serialized_start=169,
  serialized_end=229,
)


_ORDERPAI = _descriptor.Descriptor(
  name='OrderPai',
  full_name='OrderPai',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pai', full_name='OrderPai.pai', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chipai', full_name='OrderPai.chipai', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pengpai', full_name='OrderPai.pengpai', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gangpai', full_name='OrderPai.gangpai', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=231,
  serialized_end=339,
)


_PAIPOOL = _descriptor.Descriptor(
  name='PaiPool',
  full_name='PaiPool',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nType', full_name='PaiPool.nType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nValue', full_name='PaiPool.nValue', index=1,
      number=2, type=5, cpp_type=1, label=3,
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
  serialized_start=341,
  serialized_end=381,
)


_CANHUPAI = _descriptor.Descriptor(
  name='CanHuPai',
  full_name='CanHuPai',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pai', full_name='CanHuPai.pai', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='CanHuPai.count', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=383,
  serialized_end=427,
)


_CANHUPAIPOOL = _descriptor.Descriptor(
  name='CanHuPaiPool',
  full_name='CanHuPaiPool',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pai', full_name='CanHuPaiPool.pai', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pool', full_name='CanHuPaiPool.pool', index=1,
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
  serialized_start=429,
  serialized_end=487,
)


_GAMERPAIPOOL = _descriptor.Descriptor(
  name='GamerPaiPool',
  full_name='GamerPaiPool',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nID', full_name='GamerPaiPool.nID', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pool', full_name='GamerPaiPool.pool', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chiPool', full_name='GamerPaiPool.chiPool', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pengPool', full_name='GamerPaiPool.pengPool', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mGangPool', full_name='GamerPaiPool.mGangPool', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aGangPool', full_name='GamerPaiPool.aGangPool', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='putPool', full_name='GamerPaiPool.putPool', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orderPai', full_name='GamerPaiPool.orderPai', index=7,
      number=8, type=11, cpp_type=10, label=3,
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
  serialized_start=490,
  serialized_end=710,
)

_ORDERPAI.fields_by_name['pai'].message_type = _PAI
_ORDERPAI.fields_by_name['chipai'].message_type = _CHIPAI
_ORDERPAI.fields_by_name['pengpai'].message_type = _PENGPAI
_ORDERPAI.fields_by_name['gangpai'].message_type = _GANGPAI
_CANHUPAI.fields_by_name['pai'].message_type = _PAI
_CANHUPAIPOOL.fields_by_name['pai'].message_type = _PAI
_CANHUPAIPOOL.fields_by_name['pool'].message_type = _CANHUPAI
_GAMERPAIPOOL.fields_by_name['pool'].message_type = _PAIPOOL
_GAMERPAIPOOL.fields_by_name['chiPool'].message_type = _PAIPOOL
_GAMERPAIPOOL.fields_by_name['pengPool'].message_type = _PAIPOOL
_GAMERPAIPOOL.fields_by_name['mGangPool'].message_type = _PAIPOOL
_GAMERPAIPOOL.fields_by_name['aGangPool'].message_type = _PAIPOOL
_GAMERPAIPOOL.fields_by_name['putPool'].message_type = _PAIPOOL
_GAMERPAIPOOL.fields_by_name['orderPai'].message_type = _ORDERPAI
DESCRIPTOR.message_types_by_name['Pai'] = _PAI
DESCRIPTOR.message_types_by_name['ChiPai'] = _CHIPAI
DESCRIPTOR.message_types_by_name['PengPai'] = _PENGPAI
DESCRIPTOR.message_types_by_name['GangPai'] = _GANGPAI
DESCRIPTOR.message_types_by_name['OrderPai'] = _ORDERPAI
DESCRIPTOR.message_types_by_name['PaiPool'] = _PAIPOOL
DESCRIPTOR.message_types_by_name['CanHuPai'] = _CANHUPAI
DESCRIPTOR.message_types_by_name['CanHuPaiPool'] = _CANHUPAIPOOL
DESCRIPTOR.message_types_by_name['GamerPaiPool'] = _GAMERPAIPOOL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Pai = _reflection.GeneratedProtocolMessageType('Pai', (_message.Message,), dict(
  DESCRIPTOR = _PAI,
  __module__ = 'pai_pb2'
  # @@protoc_insertion_point(class_scope:Pai)
  ))
_sym_db.RegisterMessage(Pai)

ChiPai = _reflection.GeneratedProtocolMessageType('ChiPai', (_message.Message,), dict(
  DESCRIPTOR = _CHIPAI,
  __module__ = 'pai_pb2'
  # @@protoc_insertion_point(class_scope:ChiPai)
  ))
_sym_db.RegisterMessage(ChiPai)

PengPai = _reflection.GeneratedProtocolMessageType('PengPai', (_message.Message,), dict(
  DESCRIPTOR = _PENGPAI,
  __module__ = 'pai_pb2'
  # @@protoc_insertion_point(class_scope:PengPai)
  ))
_sym_db.RegisterMessage(PengPai)

GangPai = _reflection.GeneratedProtocolMessageType('GangPai', (_message.Message,), dict(
  DESCRIPTOR = _GANGPAI,
  __module__ = 'pai_pb2'
  # @@protoc_insertion_point(class_scope:GangPai)
  ))
_sym_db.RegisterMessage(GangPai)

OrderPai = _reflection.GeneratedProtocolMessageType('OrderPai', (_message.Message,), dict(
  DESCRIPTOR = _ORDERPAI,
  __module__ = 'pai_pb2'
  # @@protoc_insertion_point(class_scope:OrderPai)
  ))
_sym_db.RegisterMessage(OrderPai)

PaiPool = _reflection.GeneratedProtocolMessageType('PaiPool', (_message.Message,), dict(
  DESCRIPTOR = _PAIPOOL,
  __module__ = 'pai_pb2'
  # @@protoc_insertion_point(class_scope:PaiPool)
  ))
_sym_db.RegisterMessage(PaiPool)

CanHuPai = _reflection.GeneratedProtocolMessageType('CanHuPai', (_message.Message,), dict(
  DESCRIPTOR = _CANHUPAI,
  __module__ = 'pai_pb2'
  # @@protoc_insertion_point(class_scope:CanHuPai)
  ))
_sym_db.RegisterMessage(CanHuPai)

CanHuPaiPool = _reflection.GeneratedProtocolMessageType('CanHuPaiPool', (_message.Message,), dict(
  DESCRIPTOR = _CANHUPAIPOOL,
  __module__ = 'pai_pb2'
  # @@protoc_insertion_point(class_scope:CanHuPaiPool)
  ))
_sym_db.RegisterMessage(CanHuPaiPool)

GamerPaiPool = _reflection.GeneratedProtocolMessageType('GamerPaiPool', (_message.Message,), dict(
  DESCRIPTOR = _GAMERPAIPOOL,
  __module__ = 'pai_pb2'
  # @@protoc_insertion_point(class_scope:GamerPaiPool)
  ))
_sym_db.RegisterMessage(GamerPaiPool)


# @@protoc_insertion_point(module_scope)
