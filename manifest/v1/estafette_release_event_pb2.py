# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: manifest.v1/estafette_release_event.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='manifest.v1/estafette_release_event.proto',
  package='manifest.v1',
  syntax='proto3',
  serialized_options=_b('Z>github.com/estafette/estafette-ci-contracts-golang/manifest_v1'),
  serialized_pb=_b('\n)manifest.v1/estafette_release_event.proto\x12\x0bmanifest.v1\"\x9b\x01\n\x15\x45stafetteReleaseEvent\x12\x17\n\x0frelease_version\x18\x01 \x01(\t\x12\x13\n\x0brepo_source\x18\x02 \x01(\t\x12\x12\n\nrepo_owner\x18\x03 \x01(\t\x12\x11\n\trepo_name\x18\x04 \x01(\t\x12\x0e\n\x06target\x18\x05 \x01(\t\x12\x0e\n\x06status\x18\x06 \x01(\t\x12\r\n\x05\x65vent\x18\x07 \x01(\tB@Z>github.com/estafette/estafette-ci-contracts-golang/manifest_v1b\x06proto3')
)




_ESTAFETTERELEASEEVENT = _descriptor.Descriptor(
  name='EstafetteReleaseEvent',
  full_name='manifest.v1.EstafetteReleaseEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='release_version', full_name='manifest.v1.EstafetteReleaseEvent.release_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo_source', full_name='manifest.v1.EstafetteReleaseEvent.repo_source', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo_owner', full_name='manifest.v1.EstafetteReleaseEvent.repo_owner', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo_name', full_name='manifest.v1.EstafetteReleaseEvent.repo_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target', full_name='manifest.v1.EstafetteReleaseEvent.target', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='manifest.v1.EstafetteReleaseEvent.status', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event', full_name='manifest.v1.EstafetteReleaseEvent.event', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_end=214,
)

DESCRIPTOR.message_types_by_name['EstafetteReleaseEvent'] = _ESTAFETTERELEASEEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EstafetteReleaseEvent = _reflection.GeneratedProtocolMessageType('EstafetteReleaseEvent', (_message.Message,), dict(
  DESCRIPTOR = _ESTAFETTERELEASEEVENT,
  __module__ = 'manifest.v1.estafette_release_event_pb2'
  # @@protoc_insertion_point(class_scope:manifest.v1.EstafetteReleaseEvent)
  ))
_sym_db.RegisterMessage(EstafetteReleaseEvent)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
