# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: manifest.v1/estafette_release_action.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='manifest.v1/estafette_release_action.proto',
  package='manifest.v1',
  syntax='proto3',
  serialized_options=_b('Z>github.com/estafette/estafette-ci-contracts-golang/manifest_v1'),
  serialized_pb=_b('\n*manifest.v1/estafette_release_action.proto\x12\x0bmanifest.v1\"&\n\x16\x45stafetteReleaseAction\x12\x0c\n\x04name\x18\x01 \x01(\tB@Z>github.com/estafette/estafette-ci-contracts-golang/manifest_v1b\x06proto3')
)




_ESTAFETTERELEASEACTION = _descriptor.Descriptor(
  name='EstafetteReleaseAction',
  full_name='manifest.v1.EstafetteReleaseAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='manifest.v1.EstafetteReleaseAction.name', index=0,
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
  serialized_start=59,
  serialized_end=97,
)

DESCRIPTOR.message_types_by_name['EstafetteReleaseAction'] = _ESTAFETTERELEASEACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EstafetteReleaseAction = _reflection.GeneratedProtocolMessageType('EstafetteReleaseAction', (_message.Message,), dict(
  DESCRIPTOR = _ESTAFETTERELEASEACTION,
  __module__ = 'manifest.v1.estafette_release_action_pb2'
  # @@protoc_insertion_point(class_scope:manifest.v1.EstafetteReleaseAction)
  ))
_sym_db.RegisterMessage(EstafetteReleaseAction)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
