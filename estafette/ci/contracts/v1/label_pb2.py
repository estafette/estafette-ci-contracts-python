# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: estafette/ci/contracts/v1/label.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='estafette/ci/contracts/v1/label.proto',
  package='estafette.ci.contracts.v1',
  syntax='proto3',
  serialized_options=_b('\n\035com.estafette.ci.contracts.v1P\001Z<github.com/estafette/estafette-ci-protos-golang/contracts/v1\252\002\031Estafette.Ci.Contracts.V1'),
  serialized_pb=_b('\n%estafette/ci/contracts/v1/label.proto\x12\x19\x65stafette.ci.contracts.v1\"#\n\x05Label\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\tB{\n\x1d\x63om.estafette.ci.contracts.v1P\x01Z<github.com/estafette/estafette-ci-protos-golang/contracts/v1\xaa\x02\x19\x45stafette.Ci.Contracts.V1b\x06proto3')
)




_LABEL = _descriptor.Descriptor(
  name='Label',
  full_name='estafette.ci.contracts.v1.Label',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='estafette.ci.contracts.v1.Label.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='estafette.ci.contracts.v1.Label.value', index=1,
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
  serialized_start=68,
  serialized_end=103,
)

DESCRIPTOR.message_types_by_name['Label'] = _LABEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Label = _reflection.GeneratedProtocolMessageType('Label', (_message.Message,), {
  'DESCRIPTOR' : _LABEL,
  '__module__' : 'estafette.ci.contracts.v1.label_pb2'
  # @@protoc_insertion_point(class_scope:estafette.ci.contracts.v1.Label)
  })
_sym_db.RegisterMessage(Label)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
