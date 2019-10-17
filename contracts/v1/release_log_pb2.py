# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contracts.v1/release_log.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from contracts.v1 import build_log_step_pb2 as contracts_dot_v1_dot_build__log__step__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='contracts.v1/release_log.proto',
  package='contracts.v1',
  syntax='proto3',
  serialized_options=_b('Z?github.com/estafette/estafette-ci-contracts-golang/contracts_v1\252\002\031Estafette.CI.Contracts.V1'),
  serialized_pb=_b('\n\x1e\x63ontracts.v1/release_log.proto\x12\x0c\x63ontracts.v1\x1a!contracts.v1/build_log_step.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc4\x01\n\nReleaseLog\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0brepo_source\x18\x02 \x01(\t\x12\x12\n\nrepo_owner\x18\x03 \x01(\t\x12\x11\n\trepo_name\x18\x04 \x01(\t\x12\x12\n\nrelease_id\x18\x05 \x01(\t\x12)\n\x05steps\x18\x06 \x03(\x0b\x32\x1a.contracts.v1.BuildLogStep\x12/\n\x0binserted_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampB]Z?github.com/estafette/estafette-ci-contracts-golang/contracts_v1\xaa\x02\x19\x45stafette.CI.Contracts.V1b\x06proto3')
  ,
  dependencies=[contracts_dot_v1_dot_build__log__step__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_RELEASELOG = _descriptor.Descriptor(
  name='ReleaseLog',
  full_name='contracts.v1.ReleaseLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='contracts.v1.ReleaseLog.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo_source', full_name='contracts.v1.ReleaseLog.repo_source', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo_owner', full_name='contracts.v1.ReleaseLog.repo_owner', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo_name', full_name='contracts.v1.ReleaseLog.repo_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='release_id', full_name='contracts.v1.ReleaseLog.release_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='steps', full_name='contracts.v1.ReleaseLog.steps', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inserted_at', full_name='contracts.v1.ReleaseLog.inserted_at', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=117,
  serialized_end=313,
)

_RELEASELOG.fields_by_name['steps'].message_type = contracts_dot_v1_dot_build__log__step__pb2._BUILDLOGSTEP
_RELEASELOG.fields_by_name['inserted_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['ReleaseLog'] = _RELEASELOG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReleaseLog = _reflection.GeneratedProtocolMessageType('ReleaseLog', (_message.Message,), dict(
  DESCRIPTOR = _RELEASELOG,
  __module__ = 'contracts.v1.release_log_pb2'
  # @@protoc_insertion_point(class_scope:contracts.v1.ReleaseLog)
  ))
_sym_db.RegisterMessage(ReleaseLog)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
