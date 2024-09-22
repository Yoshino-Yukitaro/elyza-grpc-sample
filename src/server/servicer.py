from proto import guide_pb2
from proto import guide_pb2_grpc


class GuideServicer(guide_pb2_grpc.GuideServicer):
    def ThinkResponseMsg(self, request, context):
        return guide_pb2.GuideMsg(msg="Hello, {}".format(request.msg))
