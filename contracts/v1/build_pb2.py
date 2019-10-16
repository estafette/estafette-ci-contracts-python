# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contracts.v1/build.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from contracts.v1 import label_pb2 as contracts_dot_v1_dot_label__pb2
from contracts.v1 import release_target_pb2 as contracts_dot_v1_dot_release__target__pb2
from contracts.v1 import git_commit_pb2 as contracts_dot_v1_dot_git__commit__pb2
from manifest.v1 import estafette_trigger_pb2 as manifest_dot_v1_dot_estafette__trigger__pb2
from manifest.v1 import estafette_event_pb2 as manifest_dot_v1_dot_estafette__event__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='contracts.v1/build.proto',
  package='contracts.v1',
  syntax='proto3',
  serialized_options=_b('Z?github.com/estafette/estafette-ci-contracts-golang/contracts_v1'),
  serialized_pb=_b('\n\x18\x63ontracts.v1/build.proto\x12\x0c\x63ontracts.v1\x1a\x18\x63ontracts.v1/label.proto\x1a!contracts.v1/release_target.proto\x1a\x1d\x63ontracts.v1/git_commit.proto\x1a#manifest.v1/estafette_trigger.proto\x1a!manifest.v1/estafette_event.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\"\xcb\x04\n\x05\x42uild\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0brepo_source\x18\x02 \x01(\t\x12\x12\n\nrepo_owner\x18\x03 \x01(\t\x12\x11\n\trepo_name\x18\x04 \x01(\t\x12\x13\n\x0brepo_branch\x18\x05 \x01(\t\x12\x15\n\rrepo_revision\x18\x06 \x01(\t\x12\x15\n\rbuild_version\x18\x07 \x01(\t\x12\x14\n\x0c\x62uild_status\x18\x08 \x01(\t\x12#\n\x06labels\x18\t \x03(\x0b\x32\x13.contracts.v1.Label\x12\x34\n\x0frelease_targets\x18\n \x03(\x0b\x32\x1b.contracts.v1.ReleaseTarget\x12\x10\n\x08manifest\x18\x0b \x01(\t\x12\x1e\n\x16manifest_with_defaults\x18\x0c \x01(\t\x12(\n\x07\x63ommits\x18\r \x03(\x0b\x32\x17.contracts.v1.GitCommit\x12/\n\x08triggers\x18\x0e \x03(\x0b\x32\x1d.manifest.v1.EstafetteTrigger\x12+\n\x06\x65vents\x18\x0f \x03(\x0b\x32\x1b.manifest.v1.EstafetteEvent\x12/\n\x0binserted_at\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x11 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x08\x64uration\x18\x12 \x01(\x0b\x32\x19.google.protobuf.DurationBAZ?github.com/estafette/estafette-ci-contracts-golang/contracts_v1b\x06proto3')
  ,
  dependencies=[contracts_dot_v1_dot_label__pb2.DESCRIPTOR,contracts_dot_v1_dot_release__target__pb2.DESCRIPTOR,contracts_dot_v1_dot_git__commit__pb2.DESCRIPTOR,manifest_dot_v1_dot_estafette__trigger__pb2.DESCRIPTOR,manifest_dot_v1_dot_estafette__event__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])




_BUILD = _descriptor.Descriptor(
  name='Build',
  full_name='contracts.v1.Build',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='contracts.v1.Build.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo_source', full_name='contracts.v1.Build.repo_source', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo_owner', full_name='contracts.v1.Build.repo_owner', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo_name', full_name='contracts.v1.Build.repo_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo_branch', full_name='contracts.v1.Build.repo_branch', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo_revision', full_name='contracts.v1.Build.repo_revision', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='build_version', full_name='contracts.v1.Build.build_version', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='build_status', full_name='contracts.v1.Build.build_status', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='contracts.v1.Build.labels', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='release_targets', full_name='contracts.v1.Build.release_targets', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manifest', full_name='contracts.v1.Build.manifest', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manifest_with_defaults', full_name='contracts.v1.Build.manifest_with_defaults', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commits', full_name='contracts.v1.Build.commits', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='triggers', full_name='contracts.v1.Build.triggers', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='events', full_name='contracts.v1.Build.events', index=14,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inserted_at', full_name='contracts.v1.Build.inserted_at', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='contracts.v1.Build.updated_at', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='contracts.v1.Build.duration', index=17,
      number=18, type=11, cpp_type=10, label=1,
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
  serialized_start=272,
  serialized_end=859,
)

_BUILD.fields_by_name['labels'].message_type = contracts_dot_v1_dot_label__pb2._LABEL
_BUILD.fields_by_name['release_targets'].message_type = contracts_dot_v1_dot_release__target__pb2._RELEASETARGET
_BUILD.fields_by_name['commits'].message_type = contracts_dot_v1_dot_git__commit__pb2._GITCOMMIT
_BUILD.fields_by_name['triggers'].message_type = manifest_dot_v1_dot_estafette__trigger__pb2._ESTAFETTETRIGGER
_BUILD.fields_by_name['events'].message_type = manifest_dot_v1_dot_estafette__event__pb2._ESTAFETTEEVENT
_BUILD.fields_by_name['inserted_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BUILD.fields_by_name['updated_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_BUILD.fields_by_name['duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
DESCRIPTOR.message_types_by_name['Build'] = _BUILD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Build = _reflection.GeneratedProtocolMessageType('Build', (_message.Message,), dict(
  DESCRIPTOR = _BUILD,
  __module__ = 'contracts.v1.build_pb2'
  # @@protoc_insertion_point(class_scope:contracts.v1.Build)
  ))
_sym_db.RegisterMessage(Build)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
