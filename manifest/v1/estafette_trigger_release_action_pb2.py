# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: manifest.v1/estafette_trigger_release_action.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='manifest.v1/estafette_trigger_release_action.proto',
  package='manifest.v1',
  syntax='proto3',
  serialized_options=_b('Z>github.com/estafette/estafette-ci-contracts-golang/manifest_v1\252\002\030Estafette.CI.Manifest.V1'),
  serialized_pb=_b('\n2manifest.v1/estafette_trigger_release_action.proto\x12\x0bmanifest.v1\"P\n\x1d\x45stafetteTriggerReleaseAction\x12\x0e\n\x06target\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\tB[Z>github.com/estafette/estafette-ci-contracts-golang/manifest_v1\xaa\x02\x18\x45stafette.CI.Manifest.V1b\x06proto3')
)




_ESTAFETTETRIGGERRELEASEACTION = _descriptor.Descriptor(
  name='EstafetteTriggerReleaseAction',
  full_name='manifest.v1.EstafetteTriggerReleaseAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='manifest.v1.EstafetteTriggerReleaseAction.target', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='manifest.v1.EstafetteTriggerReleaseAction.action', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='manifest.v1.EstafetteTriggerReleaseAction.version', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=67,
  serialized_end=147,
)

DESCRIPTOR.message_types_by_name['EstafetteTriggerReleaseAction'] = _ESTAFETTETRIGGERRELEASEACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EstafetteTriggerReleaseAction = _reflection.GeneratedProtocolMessageType('EstafetteTriggerReleaseAction', (_message.Message,), dict(
  DESCRIPTOR = _ESTAFETTETRIGGERRELEASEACTION,
  __module__ = 'manifest.v1.estafette_trigger_release_action_pb2'
  # @@protoc_insertion_point(class_scope:manifest.v1.EstafetteTriggerReleaseAction)
  ))
_sym_db.RegisterMessage(EstafetteTriggerReleaseAction)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
