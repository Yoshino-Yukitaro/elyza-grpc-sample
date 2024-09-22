# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import guide_pb2 as guide__pb2

GRPC_GENERATED_VERSION = "1.66.1"
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower

    _version_not_supported = first_version_is_lower(
        GRPC_VERSION, GRPC_GENERATED_VERSION
    )
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f"The grpc package installed is at version {GRPC_VERSION},"
        + f" but the generated code in guide_pb2_grpc.py depends on"
        + f" grpcio>={GRPC_GENERATED_VERSION}."
        + f" Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}"
        + f" or downgrade your generated code using grpcio-tools<={GRPC_VERSION}."
    )


class GuideStub(object):
    """ゆっきーの砂場の案内をするAI機能の定義"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ThinkResponseMsg = channel.unary_unary(
            "/guide.Guide/ThinkResponseMsg",
            request_serializer=guide__pb2.UserMsg.SerializeToString,
            response_deserializer=guide__pb2.GuideMsg.FromString,
            _registered_method=True,
        )


class GuideServicer(object):
    """ゆっきーの砂場の案内をするAI機能の定義"""

    def ThinkResponseMsg(self, request, context):
        """ユーザーからのメッセージを受けてレスポンス内容を考える"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_GuideServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ThinkResponseMsg": grpc.unary_unary_rpc_method_handler(
            servicer.ThinkResponseMsg,
            request_deserializer=guide__pb2.UserMsg.FromString,
            response_serializer=guide__pb2.GuideMsg.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "guide.Guide", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers("guide.Guide", rpc_method_handlers)


# This class is part of an EXPERIMENTAL API.
class Guide(object):
    """ゆっきーの砂場の案内をするAI機能の定義"""

    @staticmethod
    def ThinkResponseMsg(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/guide.Guide/ThinkResponseMsg",
            guide__pb2.UserMsg.SerializeToString,
            guide__pb2.GuideMsg.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )
