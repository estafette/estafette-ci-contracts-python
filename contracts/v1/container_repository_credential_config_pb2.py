# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contracts.v1/container_repository_credential_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='contracts.v1/container_repository_credential_config.proto',
  package='contracts.v1',
  syntax='proto3',
  serialized_options=_b('Z?github.com/estafette/estafette-ci-contracts-golang/contracts_v1'),
  serialized_pb=_b('\n9contracts.v1/container_repository_credential_config.proto\x12\x0c\x63ontracts.v1\"]\n#ContainerRepositoryCredentialConfig\x12\x12\n\nrepository\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\tBAZ?github.com/estafette/estafette-ci-contracts-golang/contracts_v1b\x06proto3')
)




_CONTAINERREPOSITORYCREDENTIALCONFIG = _descriptor.Descriptor(
  name='ContainerRepositoryCredentialConfig',
  full_name='contracts.v1.ContainerRepositoryCredentialConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repository', full_name='contracts.v1.ContainerRepositoryCredentialConfig.repository', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='contracts.v1.ContainerRepositoryCredentialConfig.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='contracts.v1.ContainerRepositoryCredentialConfig.password', index=2,
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
  serialized_start=75,
  serialized_end=168,
)

DESCRIPTOR.message_types_by_name['ContainerRepositoryCredentialConfig'] = _CONTAINERREPOSITORYCREDENTIALCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ContainerRepositoryCredentialConfig = _reflection.GeneratedProtocolMessageType('ContainerRepositoryCredentialConfig', (_message.Message,), dict(
  DESCRIPTOR = _CONTAINERREPOSITORYCREDENTIALCONFIG,
  __module__ = 'contracts.v1.container_repository_credential_config_pb2'
  # @@protoc_insertion_point(class_scope:contracts.v1.ContainerRepositoryCredentialConfig)
  ))
_sym_db.RegisterMessage(ContainerRepositoryCredentialConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
