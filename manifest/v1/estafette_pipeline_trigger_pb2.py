# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: manifest.v1/estafette_pipeline_trigger.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='manifest.v1/estafette_pipeline_trigger.proto',
  package='manifest.v1',
  syntax='proto3',
  serialized_options=_b('\n\033io.estafette.ci.manifest.v1Z;github.com/estafette/estafette-ci-protos-golang/manifest_v1\252\002\030Estafette.CI.Manifest.V1'),
  serialized_pb=_b('\n,manifest.v1/estafette_pipeline_trigger.proto\x12\x0bmanifest.v1\"W\n\x18\x45stafettePipelineTrigger\x12\r\n\x05\x65vent\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0e\n\x06\x62ranch\x18\x04 \x01(\tBu\n\x1bio.estafette.ci.manifest.v1Z;github.com/estafette/estafette-ci-protos-golang/manifest_v1\xaa\x02\x18\x45stafette.CI.Manifest.V1b\x06proto3')
)




_ESTAFETTEPIPELINETRIGGER = _descriptor.Descriptor(
  name='EstafettePipelineTrigger',
  full_name='manifest.v1.EstafettePipelineTrigger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event', full_name='manifest.v1.EstafettePipelineTrigger.event', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='manifest.v1.EstafettePipelineTrigger.status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='manifest.v1.EstafettePipelineTrigger.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='branch', full_name='manifest.v1.EstafettePipelineTrigger.branch', index=3,
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
  serialized_start=61,
  serialized_end=148,
)

DESCRIPTOR.message_types_by_name['EstafettePipelineTrigger'] = _ESTAFETTEPIPELINETRIGGER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EstafettePipelineTrigger = _reflection.GeneratedProtocolMessageType('EstafettePipelineTrigger', (_message.Message,), dict(
  DESCRIPTOR = _ESTAFETTEPIPELINETRIGGER,
  __module__ = 'manifest.v1.estafette_pipeline_trigger_pb2'
  # @@protoc_insertion_point(class_scope:manifest.v1.EstafettePipelineTrigger)
  ))
_sym_db.RegisterMessage(EstafettePipelineTrigger)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
