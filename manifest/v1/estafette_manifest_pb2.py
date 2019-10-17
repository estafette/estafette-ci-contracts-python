# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: manifest.v1/estafette_manifest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from manifest.v1 import estafette_builder_pb2 as manifest_dot_v1_dot_estafette__builder__pb2
from manifest.v1 import estafette_version_pb2 as manifest_dot_v1_dot_estafette__version__pb2
from manifest.v1 import estafette_trigger_pb2 as manifest_dot_v1_dot_estafette__trigger__pb2
from manifest.v1 import estafette_stage_pb2 as manifest_dot_v1_dot_estafette__stage__pb2
from manifest.v1 import estafette_release_pb2 as manifest_dot_v1_dot_estafette__release__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='manifest.v1/estafette_manifest.proto',
  package='manifest.v1',
  syntax='proto3',
  serialized_options=_b('Z>github.com/estafette/estafette-ci-contracts-golang/manifest_v1\252\002\030Estafette.CI.Manifest.V1'),
  serialized_pb=_b('\n$manifest.v1/estafette_manifest.proto\x12\x0bmanifest.v1\x1a#manifest.v1/estafette_builder.proto\x1a#manifest.v1/estafette_version.proto\x1a#manifest.v1/estafette_trigger.proto\x1a!manifest.v1/estafette_stage.proto\x1a#manifest.v1/estafette_release.proto\"\xef\x03\n\x11\x45stafetteManifest\x12.\n\x07\x62uilder\x18\x01 \x01(\x0b\x32\x1d.manifest.v1.EstafetteBuilder\x12:\n\x06labels\x18\x02 \x03(\x0b\x32*.manifest.v1.EstafetteManifest.LabelsEntry\x12.\n\x07version\x18\x03 \x01(\x0b\x32\x1d.manifest.v1.EstafetteVersion\x12J\n\x0fglobal_env_vars\x18\x04 \x03(\x0b\x32\x31.manifest.v1.EstafetteManifest.GlobalEnvVarsEntry\x12/\n\x08triggers\x18\x05 \x03(\x0b\x32\x1d.manifest.v1.EstafetteTrigger\x12+\n\x06stages\x18\x06 \x03(\x0b\x32\x1b.manifest.v1.EstafetteStage\x12/\n\x08releases\x18\x07 \x03(\x0b\x32\x1d.manifest.v1.EstafetteRelease\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x34\n\x12GlobalEnvVarsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42[Z>github.com/estafette/estafette-ci-contracts-golang/manifest_v1\xaa\x02\x18\x45stafette.CI.Manifest.V1b\x06proto3')
  ,
  dependencies=[manifest_dot_v1_dot_estafette__builder__pb2.DESCRIPTOR,manifest_dot_v1_dot_estafette__version__pb2.DESCRIPTOR,manifest_dot_v1_dot_estafette__trigger__pb2.DESCRIPTOR,manifest_dot_v1_dot_estafette__stage__pb2.DESCRIPTOR,manifest_dot_v1_dot_estafette__release__pb2.DESCRIPTOR,])




_ESTAFETTEMANIFEST_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='manifest.v1.EstafetteManifest.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='manifest.v1.EstafetteManifest.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='manifest.v1.EstafetteManifest.LabelsEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=633,
  serialized_end=678,
)

_ESTAFETTEMANIFEST_GLOBALENVVARSENTRY = _descriptor.Descriptor(
  name='GlobalEnvVarsEntry',
  full_name='manifest.v1.EstafetteManifest.GlobalEnvVarsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='manifest.v1.EstafetteManifest.GlobalEnvVarsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='manifest.v1.EstafetteManifest.GlobalEnvVarsEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=680,
  serialized_end=732,
)

_ESTAFETTEMANIFEST = _descriptor.Descriptor(
  name='EstafetteManifest',
  full_name='manifest.v1.EstafetteManifest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='builder', full_name='manifest.v1.EstafetteManifest.builder', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='manifest.v1.EstafetteManifest.labels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='manifest.v1.EstafetteManifest.version', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='global_env_vars', full_name='manifest.v1.EstafetteManifest.global_env_vars', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='triggers', full_name='manifest.v1.EstafetteManifest.triggers', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stages', full_name='manifest.v1.EstafetteManifest.stages', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='releases', full_name='manifest.v1.EstafetteManifest.releases', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ESTAFETTEMANIFEST_LABELSENTRY, _ESTAFETTEMANIFEST_GLOBALENVVARSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=237,
  serialized_end=732,
)

_ESTAFETTEMANIFEST_LABELSENTRY.containing_type = _ESTAFETTEMANIFEST
_ESTAFETTEMANIFEST_GLOBALENVVARSENTRY.containing_type = _ESTAFETTEMANIFEST
_ESTAFETTEMANIFEST.fields_by_name['builder'].message_type = manifest_dot_v1_dot_estafette__builder__pb2._ESTAFETTEBUILDER
_ESTAFETTEMANIFEST.fields_by_name['labels'].message_type = _ESTAFETTEMANIFEST_LABELSENTRY
_ESTAFETTEMANIFEST.fields_by_name['version'].message_type = manifest_dot_v1_dot_estafette__version__pb2._ESTAFETTEVERSION
_ESTAFETTEMANIFEST.fields_by_name['global_env_vars'].message_type = _ESTAFETTEMANIFEST_GLOBALENVVARSENTRY
_ESTAFETTEMANIFEST.fields_by_name['triggers'].message_type = manifest_dot_v1_dot_estafette__trigger__pb2._ESTAFETTETRIGGER
_ESTAFETTEMANIFEST.fields_by_name['stages'].message_type = manifest_dot_v1_dot_estafette__stage__pb2._ESTAFETTESTAGE
_ESTAFETTEMANIFEST.fields_by_name['releases'].message_type = manifest_dot_v1_dot_estafette__release__pb2._ESTAFETTERELEASE
DESCRIPTOR.message_types_by_name['EstafetteManifest'] = _ESTAFETTEMANIFEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EstafetteManifest = _reflection.GeneratedProtocolMessageType('EstafetteManifest', (_message.Message,), dict(

  LabelsEntry = _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), dict(
    DESCRIPTOR = _ESTAFETTEMANIFEST_LABELSENTRY,
    __module__ = 'manifest.v1.estafette_manifest_pb2'
    # @@protoc_insertion_point(class_scope:manifest.v1.EstafetteManifest.LabelsEntry)
    ))
  ,

  GlobalEnvVarsEntry = _reflection.GeneratedProtocolMessageType('GlobalEnvVarsEntry', (_message.Message,), dict(
    DESCRIPTOR = _ESTAFETTEMANIFEST_GLOBALENVVARSENTRY,
    __module__ = 'manifest.v1.estafette_manifest_pb2'
    # @@protoc_insertion_point(class_scope:manifest.v1.EstafetteManifest.GlobalEnvVarsEntry)
    ))
  ,
  DESCRIPTOR = _ESTAFETTEMANIFEST,
  __module__ = 'manifest.v1.estafette_manifest_pb2'
  # @@protoc_insertion_point(class_scope:manifest.v1.EstafetteManifest)
  ))
_sym_db.RegisterMessage(EstafetteManifest)
_sym_db.RegisterMessage(EstafetteManifest.LabelsEntry)
_sym_db.RegisterMessage(EstafetteManifest.GlobalEnvVarsEntry)


DESCRIPTOR._options = None
_ESTAFETTEMANIFEST_LABELSENTRY._options = None
_ESTAFETTEMANIFEST_GLOBALENVVARSENTRY._options = None
# @@protoc_insertion_point(module_scope)
