# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contracts.v1/release_params_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='contracts.v1/release_params_config.proto',
  package='contracts.v1',
  syntax='proto3',
  serialized_options=_b('Z?github.com/estafette/estafette-ci-contracts-golang/contracts_v1\252\002\031Estafette.CI.Contracts.V1'),
  serialized_pb=_b('\n(contracts.v1/release_params_config.proto\x12\x0c\x63ontracts.v1\"m\n\x13ReleaseParamsConfig\x12\x14\n\x0crelease_name\x18\x01 \x01(\t\x12\x12\n\nrelease_id\x18\x02 \x01(\x03\x12\x16\n\x0erelease_action\x18\x03 \x01(\t\x12\x14\n\x0ctriggered_by\x18\x04 \x01(\tB]Z?github.com/estafette/estafette-ci-contracts-golang/contracts_v1\xaa\x02\x19\x45stafette.CI.Contracts.V1b\x06proto3')
)




_RELEASEPARAMSCONFIG = _descriptor.Descriptor(
  name='ReleaseParamsConfig',
  full_name='contracts.v1.ReleaseParamsConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='release_name', full_name='contracts.v1.ReleaseParamsConfig.release_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='release_id', full_name='contracts.v1.ReleaseParamsConfig.release_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='release_action', full_name='contracts.v1.ReleaseParamsConfig.release_action', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='triggered_by', full_name='contracts.v1.ReleaseParamsConfig.triggered_by', index=3,
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
  serialized_start=58,
  serialized_end=167,
)

DESCRIPTOR.message_types_by_name['ReleaseParamsConfig'] = _RELEASEPARAMSCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReleaseParamsConfig = _reflection.GeneratedProtocolMessageType('ReleaseParamsConfig', (_message.Message,), dict(
  DESCRIPTOR = _RELEASEPARAMSCONFIG,
  __module__ = 'contracts.v1.release_params_config_pb2'
  # @@protoc_insertion_point(class_scope:contracts.v1.ReleaseParamsConfig)
  ))
_sym_db.RegisterMessage(ReleaseParamsConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
