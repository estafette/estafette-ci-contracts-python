# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contracts.v1/pagination.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='contracts.v1/pagination.proto',
  package='contracts.v1',
  syntax='proto3',
  serialized_options=_b('\n\034io.estafette.ci.contracts.v1Z?github.com/estafette/estafette-ci-contracts-golang/contracts_v1\252\002\031Estafette.CI.Contracts.V1'),
  serialized_pb=_b('\n\x1d\x63ontracts.v1/pagination.proto\x12\x0c\x63ontracts.v1\"R\n\nPagination\x12\x0c\n\x04page\x18\x01 \x01(\x03\x12\x0c\n\x04size\x18\x02 \x01(\x03\x12\x13\n\x0btotal_pages\x18\x03 \x01(\x03\x12\x13\n\x0btotal_items\x18\x04 \x01(\x03\x42{\n\x1cio.estafette.ci.contracts.v1Z?github.com/estafette/estafette-ci-contracts-golang/contracts_v1\xaa\x02\x19\x45stafette.CI.Contracts.V1b\x06proto3')
)




_PAGINATION = _descriptor.Descriptor(
  name='Pagination',
  full_name='contracts.v1.Pagination',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='contracts.v1.Pagination.page', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='contracts.v1.Pagination.size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_pages', full_name='contracts.v1.Pagination.total_pages', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_items', full_name='contracts.v1.Pagination.total_items', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_end=129,
)

DESCRIPTOR.message_types_by_name['Pagination'] = _PAGINATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Pagination = _reflection.GeneratedProtocolMessageType('Pagination', (_message.Message,), dict(
  DESCRIPTOR = _PAGINATION,
  __module__ = 'contracts.v1.pagination_pb2'
  # @@protoc_insertion_point(class_scope:contracts.v1.Pagination)
  ))
_sym_db.RegisterMessage(Pagination)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
