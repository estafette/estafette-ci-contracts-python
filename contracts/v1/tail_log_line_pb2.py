# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contracts.v1/tail_log_line.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from contracts.v1 import build_log_line_pb2 as contracts_dot_v1_dot_build__log__line__pb2
from contracts.v1 import build_log_step_docker_image_pb2 as contracts_dot_v1_dot_build__log__step__docker__image__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='contracts.v1/tail_log_line.proto',
  package='contracts.v1',
  syntax='proto3',
  serialized_options=_b('Z?github.com/estafette/estafette-ci-contracts-golang/contracts_v1'),
  serialized_pb=_b('\n contracts.v1/tail_log_line.proto\x12\x0c\x63ontracts.v1\x1a\x1egoogle/protobuf/duration.proto\x1a!contracts.v1/build_log_line.proto\x1a.contracts.v1/build_log_step_docker_image.proto\"\xe6\x01\n\x0bTailLogLine\x12\x0c\n\x04step\x18\x01 \x01(\t\x12,\n\x08log_line\x18\x02 \x01(\x0b\x32\x1a.contracts.v1.BuildLogLine\x12\x34\n\x05image\x18\x03 \x01(\x0b\x32%.contracts.v1.BuildLogStepDockerImage\x12+\n\x08\x64uration\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x11\n\texit_code\x18\x05 \x01(\x03\x12\x0e\n\x06status\x18\x06 \x01(\t\x12\x15\n\rauto_injected\x18\x07 \x01(\x08\x42\x41Z?github.com/estafette/estafette-ci-contracts-golang/contracts_v1b\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,contracts_dot_v1_dot_build__log__line__pb2.DESCRIPTOR,contracts_dot_v1_dot_build__log__step__docker__image__pb2.DESCRIPTOR,])




_TAILLOGLINE = _descriptor.Descriptor(
  name='TailLogLine',
  full_name='contracts.v1.TailLogLine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='step', full_name='contracts.v1.TailLogLine.step', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_line', full_name='contracts.v1.TailLogLine.log_line', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image', full_name='contracts.v1.TailLogLine.image', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='contracts.v1.TailLogLine.duration', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exit_code', full_name='contracts.v1.TailLogLine.exit_code', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='contracts.v1.TailLogLine.status', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auto_injected', full_name='contracts.v1.TailLogLine.auto_injected', index=6,
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
  serialized_start=166,
  serialized_end=396,
)

_TAILLOGLINE.fields_by_name['log_line'].message_type = contracts_dot_v1_dot_build__log__line__pb2._BUILDLOGLINE
_TAILLOGLINE.fields_by_name['image'].message_type = contracts_dot_v1_dot_build__log__step__docker__image__pb2._BUILDLOGSTEPDOCKERIMAGE
_TAILLOGLINE.fields_by_name['duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
DESCRIPTOR.message_types_by_name['TailLogLine'] = _TAILLOGLINE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TailLogLine = _reflection.GeneratedProtocolMessageType('TailLogLine', (_message.Message,), dict(
  DESCRIPTOR = _TAILLOGLINE,
  __module__ = 'contracts.v1.tail_log_line_pb2'
  # @@protoc_insertion_point(class_scope:contracts.v1.TailLogLine)
  ))
_sym_db.RegisterMessage(TailLogLine)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
