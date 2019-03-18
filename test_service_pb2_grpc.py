# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import test_service_pb2 as test__service__pb2


class PositionServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetPosition = channel.unary_unary(
        '/PositionService/GetPosition',
        request_serializer=test__service__pb2.GetPositionRequest.SerializeToString,
        response_deserializer=test__service__pb2.GetPositionResponse.FromString,
        )


class PositionServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetPosition(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PositionServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetPosition': grpc.unary_unary_rpc_method_handler(
          servicer.GetPosition,
          request_deserializer=test__service__pb2.GetPositionRequest.FromString,
          response_serializer=test__service__pb2.GetPositionResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'PositionService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
