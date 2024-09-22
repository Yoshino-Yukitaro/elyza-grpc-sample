from concurrent import futures
import logging

import grpc
import proto.guide_pb2_grpc as guide_pb2_grpc
import server.servicer as servicer


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    guide_pb2_grpc.add_GuideServicer_to_server(servicer.GuideServicer(), server)
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    print(f"Server started on port {port}")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
