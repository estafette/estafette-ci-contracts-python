# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: estafette/ci/contracts/v1/git_commit.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from estafette.ci.contracts.v1 import git_author_pb2 as estafette_dot_ci_dot_contracts_dot_v1_dot_git__author__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='estafette/ci/contracts/v1/git_commit.proto',
  package='estafette.ci.contracts.v1',
  syntax='proto3',
  serialized_options=_b('\n\035com.estafette.ci.contracts.v1P\001Z<github.com/estafette/estafette-ci-protos-golang/contracts/v1\252\002\031Estafette.Ci.Contracts.V1'),
  serialized_pb=_b('\n*estafette/ci/contracts/v1/git_commit.proto\x12\x19\x65stafette.ci.contracts.v1\x1a*estafette/ci/contracts/v1/git_author.proto\"R\n\tGitCommit\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x34\n\x06\x61uthor\x18\x02 \x01(\x0b\x32$.estafette.ci.contracts.v1.GitAuthorB{\n\x1d\x63om.estafette.ci.contracts.v1P\x01Z<github.com/estafette/estafette-ci-protos-golang/contracts/v1\xaa\x02\x19\x45stafette.Ci.Contracts.V1b\x06proto3')
  ,
  dependencies=[estafette_dot_ci_dot_contracts_dot_v1_dot_git__author__pb2.DESCRIPTOR,])




_GITCOMMIT = _descriptor.Descriptor(
  name='GitCommit',
  full_name='estafette.ci.contracts.v1.GitCommit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='estafette.ci.contracts.v1.GitCommit.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='author', full_name='estafette.ci.contracts.v1.GitCommit.author', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_end=199,
)

_GITCOMMIT.fields_by_name['author'].message_type = estafette_dot_ci_dot_contracts_dot_v1_dot_git__author__pb2._GITAUTHOR
DESCRIPTOR.message_types_by_name['GitCommit'] = _GITCOMMIT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GitCommit = _reflection.GeneratedProtocolMessageType('GitCommit', (_message.Message,), {
  'DESCRIPTOR' : _GITCOMMIT,
  '__module__' : 'estafette.ci.contracts.v1.git_commit_pb2'
  # @@protoc_insertion_point(class_scope:estafette.ci.contracts.v1.GitCommit)
  })
_sym_db.RegisterMessage(GitCommit)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
