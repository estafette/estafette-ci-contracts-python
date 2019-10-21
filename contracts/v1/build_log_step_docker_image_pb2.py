# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contracts.v1/build_log_step_docker_image.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='contracts.v1/build_log_step_docker_image.proto',
  package='contracts.v1',
  syntax='proto3',
  serialized_options=_b('\n\034io.estafette.ci.contracts.v1Z?github.com/estafette/estafette-ci-contracts-golang/contracts_v1\252\002\031Estafette.CI.Contracts.V1'),
  serialized_pb=_b('\n.contracts.v1/build_log_step_docker_image.proto\x12\x0c\x63ontracts.v1\x1a\x1egoogle/protobuf/duration.proto\"\xb0\x01\n\x17\x42uildLogStepDockerImage\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03tag\x18\x02 \x01(\t\x12\x11\n\tis_pulled\x18\x03 \x01(\x08\x12\x12\n\nimage_size\x18\x04 \x01(\x03\x12\x30\n\rpull_duration\x18\x05 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\r\n\x05\x65rror\x18\x06 \x01(\t\x12\x12\n\nis_trusted\x18\x07 \x01(\x08\x42{\n\x1cio.estafette.ci.contracts.v1Z?github.com/estafette/estafette-ci-contracts-golang/contracts_v1\xaa\x02\x19\x45stafette.CI.Contracts.V1b\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])




_BUILDLOGSTEPDOCKERIMAGE = _descriptor.Descriptor(
  name='BuildLogStepDockerImage',
  full_name='contracts.v1.BuildLogStepDockerImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='contracts.v1.BuildLogStepDockerImage.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag', full_name='contracts.v1.BuildLogStepDockerImage.tag', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_pulled', full_name='contracts.v1.BuildLogStepDockerImage.is_pulled', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_size', full_name='contracts.v1.BuildLogStepDockerImage.image_size', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pull_duration', full_name='contracts.v1.BuildLogStepDockerImage.pull_duration', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='contracts.v1.BuildLogStepDockerImage.error', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_trusted', full_name='contracts.v1.BuildLogStepDockerImage.is_trusted', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=97,
  serialized_end=273,
)

_BUILDLOGSTEPDOCKERIMAGE.fields_by_name['pull_duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
DESCRIPTOR.message_types_by_name['BuildLogStepDockerImage'] = _BUILDLOGSTEPDOCKERIMAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BuildLogStepDockerImage = _reflection.GeneratedProtocolMessageType('BuildLogStepDockerImage', (_message.Message,), dict(
  DESCRIPTOR = _BUILDLOGSTEPDOCKERIMAGE,
  __module__ = 'contracts.v1.build_log_step_docker_image_pb2'
  # @@protoc_insertion_point(class_scope:contracts.v1.BuildLogStepDockerImage)
  ))
_sym_db.RegisterMessage(BuildLogStepDockerImage)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
