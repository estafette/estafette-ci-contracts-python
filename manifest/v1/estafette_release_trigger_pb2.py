# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: manifest.v1/estafette_release_trigger.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='manifest.v1/estafette_release_trigger.proto',
  package='manifest.v1',
  syntax='proto3',
  serialized_options=_b('\n\033io.estafette.ci.manifest.v1Z>github.com/estafette/estafette-ci-contracts-golang/manifest_v1\252\002\030Estafette.CI.Manifest.V1'),
  serialized_pb=_b('\n+manifest.v1/estafette_release_trigger.proto\x12\x0bmanifest.v1\"V\n\x17\x45stafetteReleaseTrigger\x12\r\n\x05\x65vent\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0e\n\x06target\x18\x04 \x01(\tBx\n\x1bio.estafette.ci.manifest.v1Z>github.com/estafette/estafette-ci-contracts-golang/manifest_v1\xaa\x02\x18\x45stafette.CI.Manifest.V1b\x06proto3')
)




_ESTAFETTERELEASETRIGGER = _descriptor.Descriptor(
  name='EstafetteReleaseTrigger',
  full_name='manifest.v1.EstafetteReleaseTrigger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event', full_name='manifest.v1.EstafetteReleaseTrigger.event', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='manifest.v1.EstafetteReleaseTrigger.status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='manifest.v1.EstafetteReleaseTrigger.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target', full_name='manifest.v1.EstafetteReleaseTrigger.target', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=60,
  serialized_end=146,
)

DESCRIPTOR.message_types_by_name['EstafetteReleaseTrigger'] = _ESTAFETTERELEASETRIGGER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EstafetteReleaseTrigger = _reflection.GeneratedProtocolMessageType('EstafetteReleaseTrigger', (_message.Message,), dict(
  DESCRIPTOR = _ESTAFETTERELEASETRIGGER,
  __module__ = 'manifest.v1.estafette_release_trigger_pb2'
  # @@protoc_insertion_point(class_scope:manifest.v1.EstafetteReleaseTrigger)
  ))
_sym_db.RegisterMessage(EstafetteReleaseTrigger)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
