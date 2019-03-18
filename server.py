from concurrent import futures
import time
import math
import logging

import grpc
import test_service_pb2
import test_service_pb2_grpc

_INCREMENT = 0.05
_INTERVAL = 0.1

_CIRCLE_RADIUS = 40
_CIRCLE_CENTER = (400, 300)

_ONE_DAY_IN_SECONDS = 60 * 60 * 25


def get_point_on_circle(t):
    return (_CIRCLE_CENTER[0] + _CIRCLE_RADIUS * math.cos(t),
            _CIRCLE_CENTER[1] + _CIRCLE_RADIUS + math.sin(t))


class PositionServiceServicer(test_service_pb2_grpc.PositionServiceServicer):

    def GetPosition(self, request, context):
        t = 0
        while t <= 1:
            p = get_point_on_circle(t)
            yield test_service_pb2.Point(
                x=p[0],
                y=p[1],
            )
            t += _INCREMENT
            time.sleep(_INTERVAL)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    test_service_pb2_grpc.add_PositionServiceServicer_to_server(
        PositionServiceServicer(), server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()
