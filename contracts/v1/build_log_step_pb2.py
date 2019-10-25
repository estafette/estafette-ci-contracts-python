# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contracts.v1/build_log_step.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from contracts.v1 import build_log_line_pb2 as contracts_dot_v1_dot_build__log__line__pb2
from contracts.v1 import build_log_step_docker_image_pb2 as contracts_dot_v1_dot_build__log__step__docker__image__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='contracts.v1/build_log_step.proto',
  package='contracts.v1',
  syntax='proto3',
  serialized_options=_b('\n\034io.estafette.ci.contracts.v1Z<github.com/estafette/estafette-ci-protos-golang/contracts_v1\252\002\031Estafette.CI.Contracts.V1'),
  serialized_pb=_b('\n!contracts.v1/build_log_step.proto\x12\x0c\x63ontracts.v1\x1a!contracts.v1/build_log_line.proto\x1a.contracts.v1/build_log_step_docker_image.proto\x1a\x1egoogle/protobuf/duration.proto\"\xfb\x01\n\x0c\x42uildLogStep\x12\x0c\n\x04step\x18\x01 \x01(\t\x12\x34\n\x05image\x18\x02 \x01(\x0b\x32%.contracts.v1.BuildLogStepDockerImage\x12\x11\n\trun_index\x18\x03 \x01(\x03\x12+\n\x08\x64uration\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12-\n\tlog_lines\x18\x05 \x03(\x0b\x32\x1a.contracts.v1.BuildLogLine\x12\x11\n\texit_code\x18\x06 \x01(\x03\x12\x0e\n\x06status\x18\x07 \x01(\t\x12\x15\n\rauto_injected\x18\x08 \x01(\x08\x42x\n\x1cio.estafette.ci.contracts.v1Z<github.com/estafette/estafette-ci-protos-golang/contracts_v1\xaa\x02\x19\x45stafette.CI.Contracts.V1b\x06proto3')
  ,
  dependencies=[contracts_dot_v1_dot_build__log__line__pb2.DESCRIPTOR,contracts_dot_v1_dot_build__log__step__docker__image__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])




_BUILDLOGSTEP = _descriptor.Descriptor(
  name='BuildLogStep',
  full_name='contracts.v1.BuildLogStep',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='step', full_name='contracts.v1.BuildLogStep.step', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image', full_name='contracts.v1.BuildLogStep.image', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='run_index', full_name='contracts.v1.BuildLogStep.run_index', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='contracts.v1.BuildLogStep.duration', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_lines', full_name='contracts.v1.BuildLogStep.log_lines', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exit_code', full_name='contracts.v1.BuildLogStep.exit_code', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='contracts.v1.BuildLogStep.status', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auto_injected', full_name='contracts.v1.BuildLogStep.auto_injected', index=7,
      number=8, type=8, cpp_type=7, label=1,
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
  serialized_start=167,
  serialized_end=418,
)

_BUILDLOGSTEP.fields_by_name['image'].message_type = contracts_dot_v1_dot_build__log__step__docker__image__pb2._BUILDLOGSTEPDOCKERIMAGE
_BUILDLOGSTEP.fields_by_name['duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_BUILDLOGSTEP.fields_by_name['log_lines'].message_type = contracts_dot_v1_dot_build__log__line__pb2._BUILDLOGLINE
DESCRIPTOR.message_types_by_name['BuildLogStep'] = _BUILDLOGSTEP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BuildLogStep = _reflection.GeneratedProtocolMessageType('BuildLogStep', (_message.Message,), dict(
  DESCRIPTOR = _BUILDLOGSTEP,
  __module__ = 'contracts.v1.build_log_step_pb2'
  # @@protoc_insertion_point(class_scope:contracts.v1.BuildLogStep)
  ))
_sym_db.RegisterMessage(BuildLogStep)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
