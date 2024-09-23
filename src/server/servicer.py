from proto import guide_pb2
from proto import guide_pb2_grpc
from guide import guide


class GuideServicer(guide_pb2_grpc.GuideServicer):
    def ThinkResponseMsg(self, request, context):
        response_msg = guide.think_response_msg(request.msg)
        return guide_pb2.GuideMsg(msg="Hello, {}".format(response_msg))
