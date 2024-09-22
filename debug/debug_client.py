import grpc
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.proto import guide_pb2
from src.proto import guide_pb2_grpc


def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = guide_pb2_grpc.GuideStub(channel)
    response = stub.ThinkResponseMsg(guide_pb2.UserMsg(msg="hello"))
    print("Response received: " + response.msg)


if __name__ == "__main__":
    run()
