# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: manifest.v1/estafette_semver_version.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from manifest.v1 import string_or_string_array_pb2 as manifest_dot_v1_dot_string__or__string__array__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='manifest.v1/estafette_semver_version.proto',
  package='manifest.v1',
  syntax='proto3',
  serialized_options=_b('\n\033io.estafette.ci.manifest.v1Z;github.com/estafette/estafette-ci-protos-golang/manifest_v1\252\002\030Estafette.CI.Manifest.V1'),
  serialized_pb=_b('\n*manifest.v1/estafette_semver_version.proto\x12\x0bmanifest.v1\x1a(manifest.v1/string_or_string_array.proto\"\x97\x01\n\x16\x45stafetteSemverVersion\x12\r\n\x05major\x18\x01 \x01(\x03\x12\r\n\x05minor\x18\x02 \x01(\x03\x12\r\n\x05patch\x18\x03 \x01(\t\x12\x16\n\x0elabel_template\x18\x04 \x01(\t\x12\x38\n\x0erelease_branch\x18\x05 \x01(\x0b\x32 .manifest.v1.StringOrStringArrayBu\n\x1bio.estafette.ci.manifest.v1Z;github.com/estafette/estafette-ci-protos-golang/manifest_v1\xaa\x02\x18\x45stafette.CI.Manifest.V1b\x06proto3')
  ,
  dependencies=[manifest_dot_v1_dot_string__or__string__array__pb2.DESCRIPTOR,])




_ESTAFETTESEMVERVERSION = _descriptor.Descriptor(
  name='EstafetteSemverVersion',
  full_name='manifest.v1.EstafetteSemverVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='major', full_name='manifest.v1.EstafetteSemverVersion.major', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minor', full_name='manifest.v1.EstafetteSemverVersion.minor', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='patch', full_name='manifest.v1.EstafetteSemverVersion.patch', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label_template', full_name='manifest.v1.EstafetteSemverVersion.label_template', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='release_branch', full_name='manifest.v1.EstafetteSemverVersion.release_branch', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=102,
  serialized_end=253,
)

_ESTAFETTESEMVERVERSION.fields_by_name['release_branch'].message_type = manifest_dot_v1_dot_string__or__string__array__pb2._STRINGORSTRINGARRAY
DESCRIPTOR.message_types_by_name['EstafetteSemverVersion'] = _ESTAFETTESEMVERVERSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EstafetteSemverVersion = _reflection.GeneratedProtocolMessageType('EstafetteSemverVersion', (_message.Message,), dict(
  DESCRIPTOR = _ESTAFETTESEMVERVERSION,
  __module__ = 'manifest.v1.estafette_semver_version_pb2'
  # @@protoc_insertion_point(class_scope:manifest.v1.EstafetteSemverVersion)
  ))
_sym_db.RegisterMessage(EstafetteSemverVersion)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
