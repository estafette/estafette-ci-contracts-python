# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contracts.v1/git_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='contracts.v1/git_config.proto',
  package='contracts.v1',
  syntax='proto3',
  serialized_options=_b('\n\034io.estafette.ci.contracts.v1Z<github.com/estafette/estafette-ci-protos-golang/contracts_v1\252\002\031Estafette.CI.Contracts.V1'),
  serialized_pb=_b('\n\x1d\x63ontracts.v1/git_config.proto\x12\x0c\x63ontracts.v1\"s\n\tGitConfig\x12\x13\n\x0brepo_source\x18\x01 \x01(\t\x12\x12\n\nrepo_owner\x18\x02 \x01(\t\x12\x11\n\trepo_name\x18\x03 \x01(\t\x12\x13\n\x0brepo_branch\x18\x04 \x01(\t\x12\x15\n\rrepo_revision\x18\x05 \x01(\tBx\n\x1cio.estafette.ci.contracts.v1Z<github.com/estafette/estafette-ci-protos-golang/contracts_v1\xaa\x02\x19\x45stafette.CI.Contracts.V1b\x06proto3')
)




_GITCONFIG = _descriptor.Descriptor(
  name='GitConfig',
  full_name='contracts.v1.GitConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repo_source', full_name='contracts.v1.GitConfig.repo_source', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo_owner', full_name='contracts.v1.GitConfig.repo_owner', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo_name', full_name='contracts.v1.GitConfig.repo_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo_branch', full_name='contracts.v1.GitConfig.repo_branch', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repo_revision', full_name='contracts.v1.GitConfig.repo_revision', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=47,
  serialized_end=162,
)

DESCRIPTOR.message_types_by_name['GitConfig'] = _GITCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GitConfig = _reflection.GeneratedProtocolMessageType('GitConfig', (_message.Message,), dict(
  DESCRIPTOR = _GITCONFIG,
  __module__ = 'contracts.v1.git_config_pb2'
  # @@protoc_insertion_point(class_scope:contracts.v1.GitConfig)
  ))
_sym_db.RegisterMessage(GitConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
