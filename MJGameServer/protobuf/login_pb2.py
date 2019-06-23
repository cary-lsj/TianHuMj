# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: login.proto

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
  name='login.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0blogin.proto\"\xa6\x03\n\x04User\x12\x0f\n\x07nUserID\x18\x01 \x02(\x05\x12\r\n\x05sNick\x18\x02 \x01(\t\x12\x0c\n\x04nExp\x18\x03 \x01(\x05\x12\r\n\x05nGold\x18\x04 \x01(\x05\x12\x0e\n\x06nMoney\x18\x05 \x01(\x05\x12\x10\n\x08sHeadimg\x18\x06 \x01(\t\x12\x0e\n\x06sPhone\x18\x07 \x01(\t\x12\x10\n\x08sRecords\x18\x08 \x01(\t\x12\x0f\n\x07sAssets\x18\t \x01(\t\x12\r\n\x05sRoom\x18\n \x01(\t\x12\x0f\n\x07nParent\x18\x0b \x01(\x05\x12\x0e\n\x06sICode\x18\x0c \x01(\t\x12\r\n\x05sName\x18\r \x01(\t\x12\x13\n\x0b\x62LuckyToday\x18\x0e \x01(\x08\x12\x15\n\rbWelfareToday\x18\x0f \x01(\x08\x12\x0f\n\x07nGender\x18\x10 \x01(\x05\x12\x15\n\rbRkAwardFlags\x18\x11 \x03(\x08\x12\x17\n\x0f\x62ShareAwardWeek\x18\x12 \x01(\x08\x12\x11\n\tnWinCount\x18\x13 \x01(\x05\x12\x13\n\x0bnTotalCount\x18\x14 \x01(\x05\x12\x0b\n\x03sIP\x18\x15 \x01(\t\x12\x0e\n\x06sToken\x18\x16 \x01(\t\x12\x1b\n\x08location\x18\x17 \x01(\x0b\x32\t.Location\"M\n\x08Location\x12\x13\n\x0b\x62IsLocation\x18\x01 \x02(\x08\x12\x0c\n\x04sLng\x18\x02 \x01(\t\x12\x0c\n\x04sLat\x18\x03 \x01(\t\x12\x10\n\x08sAddress\x18\x04 \x01(\t\"M\n\x0cLoginRequest\x12\r\n\x05sName\x18\x01 \x02(\t\x12\x11\n\tsPassWord\x18\x02 \x02(\t\x12\x1b\n\x08location\x18\x03 \x01(\x0b\x32\t.Location\"\x81\x01\n\x0eLoginWXRequest\x12\x0f\n\x07sOpenID\x18\x01 \x02(\t\x12\r\n\x05sNick\x18\x02 \x01(\t\x12\x12\n\nsHeadImage\x18\x03 \x01(\t\x12\x0f\n\x07nGender\x18\x04 \x01(\x05\x12\r\n\x05iCode\x18\x05 \x01(\t\x12\x1b\n\x08location\x18\x06 \x01(\x0b\x32\t.Location\"R\n\rLoginResponse\x12\x12\n\nnErrorCode\x18\x01 \x02(\x05\x12\x18\n\trequester\x18\x02 \x01(\x0b\x32\x05.User\x12\x13\n\x0brookieAward\x18\x03 \x01(\x05\"\"\n\x0fLoginOutRequest\x12\x0f\n\x07nUserID\x18\x01 \x02(\x05\"&\n\x10LoginOutResponse\x12\x12\n\nnErrorCode\x18\x01 \x02(\x05')
)




_USER = _descriptor.Descriptor(
  name='User',
  full_name='User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nUserID', full_name='User.nUserID', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sNick', full_name='User.sNick', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nExp', full_name='User.nExp', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nGold', full_name='User.nGold', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nMoney', full_name='User.nMoney', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sHeadimg', full_name='User.sHeadimg', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sPhone', full_name='User.sPhone', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sRecords', full_name='User.sRecords', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sAssets', full_name='User.sAssets', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sRoom', full_name='User.sRoom', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nParent', full_name='User.nParent', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sICode', full_name='User.sICode', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sName', full_name='User.sName', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bLuckyToday', full_name='User.bLuckyToday', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bWelfareToday', full_name='User.bWelfareToday', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nGender', full_name='User.nGender', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bRkAwardFlags', full_name='User.bRkAwardFlags', index=16,
      number=17, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bShareAwardWeek', full_name='User.bShareAwardWeek', index=17,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nWinCount', full_name='User.nWinCount', index=18,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nTotalCount', full_name='User.nTotalCount', index=19,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sIP', full_name='User.sIP', index=20,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sToken', full_name='User.sToken', index=21,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location', full_name='User.location', index=22,
      number=23, type=11, cpp_type=10, label=1,
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
  serialized_start=16,
  serialized_end=438,
)


_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bIsLocation', full_name='Location.bIsLocation', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sLng', full_name='Location.sLng', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sLat', full_name='Location.sLat', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sAddress', full_name='Location.sAddress', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=440,
  serialized_end=517,
)


_LOGINREQUEST = _descriptor.Descriptor(
  name='LoginRequest',
  full_name='LoginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sName', full_name='LoginRequest.sName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sPassWord', full_name='LoginRequest.sPassWord', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location', full_name='LoginRequest.location', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=519,
  serialized_end=596,
)


_LOGINWXREQUEST = _descriptor.Descriptor(
  name='LoginWXRequest',
  full_name='LoginWXRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sOpenID', full_name='LoginWXRequest.sOpenID', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sNick', full_name='LoginWXRequest.sNick', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sHeadImage', full_name='LoginWXRequest.sHeadImage', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nGender', full_name='LoginWXRequest.nGender', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iCode', full_name='LoginWXRequest.iCode', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location', full_name='LoginWXRequest.location', index=5,
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
  serialized_start=599,
  serialized_end=728,
)


_LOGINRESPONSE = _descriptor.Descriptor(
  name='LoginResponse',
  full_name='LoginResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nErrorCode', full_name='LoginResponse.nErrorCode', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='requester', full_name='LoginResponse.requester', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rookieAward', full_name='LoginResponse.rookieAward', index=2,
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
  serialized_start=730,
  serialized_end=812,
)


_LOGINOUTREQUEST = _descriptor.Descriptor(
  name='LoginOutRequest',
  full_name='LoginOutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nUserID', full_name='LoginOutRequest.nUserID', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  serialized_start=814,
  serialized_end=848,
)


_LOGINOUTRESPONSE = _descriptor.Descriptor(
  name='LoginOutResponse',
  full_name='LoginOutResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nErrorCode', full_name='LoginOutResponse.nErrorCode', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  serialized_start=850,
  serialized_end=888,
)

_USER.fields_by_name['location'].message_type = _LOCATION
_LOGINREQUEST.fields_by_name['location'].message_type = _LOCATION
_LOGINWXREQUEST.fields_by_name['location'].message_type = _LOCATION
_LOGINRESPONSE.fields_by_name['requester'].message_type = _USER
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.message_types_by_name['LoginRequest'] = _LOGINREQUEST
DESCRIPTOR.message_types_by_name['LoginWXRequest'] = _LOGINWXREQUEST
DESCRIPTOR.message_types_by_name['LoginResponse'] = _LOGINRESPONSE
DESCRIPTOR.message_types_by_name['LoginOutRequest'] = _LOGINOUTREQUEST
DESCRIPTOR.message_types_by_name['LoginOutResponse'] = _LOGINOUTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), dict(
  DESCRIPTOR = _USER,
  __module__ = 'login_pb2'
  # @@protoc_insertion_point(class_scope:User)
  ))
_sym_db.RegisterMessage(User)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), dict(
  DESCRIPTOR = _LOCATION,
  __module__ = 'login_pb2'
  # @@protoc_insertion_point(class_scope:Location)
  ))
_sym_db.RegisterMessage(Location)

LoginRequest = _reflection.GeneratedProtocolMessageType('LoginRequest', (_message.Message,), dict(
  DESCRIPTOR = _LOGINREQUEST,
  __module__ = 'login_pb2'
  # @@protoc_insertion_point(class_scope:LoginRequest)
  ))
_sym_db.RegisterMessage(LoginRequest)

LoginWXRequest = _reflection.GeneratedProtocolMessageType('LoginWXRequest', (_message.Message,), dict(
  DESCRIPTOR = _LOGINWXREQUEST,
  __module__ = 'login_pb2'
  # @@protoc_insertion_point(class_scope:LoginWXRequest)
  ))
_sym_db.RegisterMessage(LoginWXRequest)

LoginResponse = _reflection.GeneratedProtocolMessageType('LoginResponse', (_message.Message,), dict(
  DESCRIPTOR = _LOGINRESPONSE,
  __module__ = 'login_pb2'
  # @@protoc_insertion_point(class_scope:LoginResponse)
  ))
_sym_db.RegisterMessage(LoginResponse)

LoginOutRequest = _reflection.GeneratedProtocolMessageType('LoginOutRequest', (_message.Message,), dict(
  DESCRIPTOR = _LOGINOUTREQUEST,
  __module__ = 'login_pb2'
  # @@protoc_insertion_point(class_scope:LoginOutRequest)
  ))
_sym_db.RegisterMessage(LoginOutRequest)

LoginOutResponse = _reflection.GeneratedProtocolMessageType('LoginOutResponse', (_message.Message,), dict(
  DESCRIPTOR = _LOGINOUTRESPONSE,
  __module__ = 'login_pb2'
  # @@protoc_insertion_point(class_scope:LoginOutResponse)
  ))
_sym_db.RegisterMessage(LoginOutResponse)


# @@protoc_insertion_point(module_scope)