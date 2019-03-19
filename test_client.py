import logging

import grpc
import test_service_pb2
import test_service_pb2_grpc

ENDPOINT_URL = '35.194.63.178:80'


def get_points(stub):
    request = test_service_pb2.GetPositionRequest()
    points = stub.GetPosition(request)
    for p in points:
        print(p)
        print("Point (%s, %s)" % (p.x, p.y))


def run():
    with grpc.insecure_channel(ENDPOINT_URL) as channel:
        stub = test_service_pb2_grpc.PositionServiceStub(channel)
        get_points(stub)


if __name__ == '__main__':
    logging.basicConfig()
    print('Starting client')
    run()
