# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import synerex_pb2 as api_dot_synerex__pb2


class SynerexStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.NotifyDemand = channel.unary_unary(
                '/api.Synerex/NotifyDemand',
                request_serializer=api_dot_synerex__pb2.Demand.SerializeToString,
                response_deserializer=api_dot_synerex__pb2.Response.FromString,
                )
        self.NotifySupply = channel.unary_unary(
                '/api.Synerex/NotifySupply',
                request_serializer=api_dot_synerex__pb2.Supply.SerializeToString,
                response_deserializer=api_dot_synerex__pb2.Response.FromString,
                )
        self.ProposeDemand = channel.unary_unary(
                '/api.Synerex/ProposeDemand',
                request_serializer=api_dot_synerex__pb2.Demand.SerializeToString,
                response_deserializer=api_dot_synerex__pb2.Response.FromString,
                )
        self.ProposeSupply = channel.unary_unary(
                '/api.Synerex/ProposeSupply',
                request_serializer=api_dot_synerex__pb2.Supply.SerializeToString,
                response_deserializer=api_dot_synerex__pb2.Response.FromString,
                )
        self.SelectSupply = channel.unary_unary(
                '/api.Synerex/SelectSupply',
                request_serializer=api_dot_synerex__pb2.Target.SerializeToString,
                response_deserializer=api_dot_synerex__pb2.ConfirmResponse.FromString,
                )
        self.SelectModifiedSupply = channel.unary_unary(
                '/api.Synerex/SelectModifiedSupply',
                request_serializer=api_dot_synerex__pb2.Supply.SerializeToString,
                response_deserializer=api_dot_synerex__pb2.ConfirmResponse.FromString,
                )
        self.SelectDemand = channel.unary_unary(
                '/api.Synerex/SelectDemand',
                request_serializer=api_dot_synerex__pb2.Target.SerializeToString,
                response_deserializer=api_dot_synerex__pb2.ConfirmResponse.FromString,
                )
        self.Confirm = channel.unary_unary(
                '/api.Synerex/Confirm',
                request_serializer=api_dot_synerex__pb2.Target.SerializeToString,
                response_deserializer=api_dot_synerex__pb2.Response.FromString,
                )
        self.SubscribeDemand = channel.unary_stream(
                '/api.Synerex/SubscribeDemand',
                request_serializer=api_dot_synerex__pb2.Channel.SerializeToString,
                response_deserializer=api_dot_synerex__pb2.Demand.FromString,
                )
        self.SubscribeSupply = channel.unary_stream(
                '/api.Synerex/SubscribeSupply',
                request_serializer=api_dot_synerex__pb2.Channel.SerializeToString,
                response_deserializer=api_dot_synerex__pb2.Supply.FromString,
                )
        self.CreateMbus = channel.unary_unary(
                '/api.Synerex/CreateMbus',
                request_serializer=api_dot_synerex__pb2.MbusOpt.SerializeToString,
                response_deserializer=api_dot_synerex__pb2.Mbus.FromString,
                )
        self.CloseMbus = channel.unary_unary(
                '/api.Synerex/CloseMbus',
                request_serializer=api_dot_synerex__pb2.Mbus.SerializeToString,
                response_deserializer=api_dot_synerex__pb2.Response.FromString,
                )
        self.SubscribeMbus = channel.unary_stream(
                '/api.Synerex/SubscribeMbus',
                request_serializer=api_dot_synerex__pb2.Mbus.SerializeToString,
                response_deserializer=api_dot_synerex__pb2.MbusMsg.FromString,
                )
        self.SendMbusMsg = channel.unary_unary(
                '/api.Synerex/SendMbusMsg',
                request_serializer=api_dot_synerex__pb2.MbusMsg.SerializeToString,
                response_deserializer=api_dot_synerex__pb2.Response.FromString,
                )
        self.GetMbusState = channel.unary_unary(
                '/api.Synerex/GetMbusState',
                request_serializer=api_dot_synerex__pb2.Mbus.SerializeToString,
                response_deserializer=api_dot_synerex__pb2.MbusState.FromString,
                )
        self.SubscribeGateway = channel.unary_stream(
                '/api.Synerex/SubscribeGateway',
                request_serializer=api_dot_synerex__pb2.GatewayInfo.SerializeToString,
                response_deserializer=api_dot_synerex__pb2.GatewayMsg.FromString,
                )
        self.ForwardToGateway = channel.unary_unary(
                '/api.Synerex/ForwardToGateway',
                request_serializer=api_dot_synerex__pb2.GatewayMsg.SerializeToString,
                response_deserializer=api_dot_synerex__pb2.Response.FromString,
                )
        self.CloseDemandChannel = channel.unary_unary(
                '/api.Synerex/CloseDemandChannel',
                request_serializer=api_dot_synerex__pb2.Channel.SerializeToString,
                response_deserializer=api_dot_synerex__pb2.Response.FromString,
                )
        self.CloseSupplyChannel = channel.unary_unary(
                '/api.Synerex/CloseSupplyChannel',
                request_serializer=api_dot_synerex__pb2.Channel.SerializeToString,
                response_deserializer=api_dot_synerex__pb2.Response.FromString,
                )
        self.CloseAllChannels = channel.unary_unary(
                '/api.Synerex/CloseAllChannels',
                request_serializer=api_dot_synerex__pb2.ProviderID.SerializeToString,
                response_deserializer=api_dot_synerex__pb2.Response.FromString,
                )


class SynerexServicer(object):
    """Missing associated documentation comment in .proto file."""

    def NotifyDemand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NotifySupply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProposeDemand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProposeSupply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SelectSupply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SelectModifiedSupply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SelectDemand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Confirm(self, request, context):
        """rpc SelectModifiedDemand(Demand) returns (ConfirmResponse) {} // select with modification(since 0.5.1)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeDemand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeSupply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateMbus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloseMbus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeMbus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendMbusMsg(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMbusState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeGateway(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ForwardToGateway(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloseDemandChannel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloseSupplyChannel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloseAllChannels(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SynerexServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'NotifyDemand': grpc.unary_unary_rpc_method_handler(
                    servicer.NotifyDemand,
                    request_deserializer=api_dot_synerex__pb2.Demand.FromString,
                    response_serializer=api_dot_synerex__pb2.Response.SerializeToString,
            ),
            'NotifySupply': grpc.unary_unary_rpc_method_handler(
                    servicer.NotifySupply,
                    request_deserializer=api_dot_synerex__pb2.Supply.FromString,
                    response_serializer=api_dot_synerex__pb2.Response.SerializeToString,
            ),
            'ProposeDemand': grpc.unary_unary_rpc_method_handler(
                    servicer.ProposeDemand,
                    request_deserializer=api_dot_synerex__pb2.Demand.FromString,
                    response_serializer=api_dot_synerex__pb2.Response.SerializeToString,
            ),
            'ProposeSupply': grpc.unary_unary_rpc_method_handler(
                    servicer.ProposeSupply,
                    request_deserializer=api_dot_synerex__pb2.Supply.FromString,
                    response_serializer=api_dot_synerex__pb2.Response.SerializeToString,
            ),
            'SelectSupply': grpc.unary_unary_rpc_method_handler(
                    servicer.SelectSupply,
                    request_deserializer=api_dot_synerex__pb2.Target.FromString,
                    response_serializer=api_dot_synerex__pb2.ConfirmResponse.SerializeToString,
            ),
            'SelectModifiedSupply': grpc.unary_unary_rpc_method_handler(
                    servicer.SelectModifiedSupply,
                    request_deserializer=api_dot_synerex__pb2.Supply.FromString,
                    response_serializer=api_dot_synerex__pb2.ConfirmResponse.SerializeToString,
            ),
            'SelectDemand': grpc.unary_unary_rpc_method_handler(
                    servicer.SelectDemand,
                    request_deserializer=api_dot_synerex__pb2.Target.FromString,
                    response_serializer=api_dot_synerex__pb2.ConfirmResponse.SerializeToString,
            ),
            'Confirm': grpc.unary_unary_rpc_method_handler(
                    servicer.Confirm,
                    request_deserializer=api_dot_synerex__pb2.Target.FromString,
                    response_serializer=api_dot_synerex__pb2.Response.SerializeToString,
            ),
            'SubscribeDemand': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeDemand,
                    request_deserializer=api_dot_synerex__pb2.Channel.FromString,
                    response_serializer=api_dot_synerex__pb2.Demand.SerializeToString,
            ),
            'SubscribeSupply': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeSupply,
                    request_deserializer=api_dot_synerex__pb2.Channel.FromString,
                    response_serializer=api_dot_synerex__pb2.Supply.SerializeToString,
            ),
            'CreateMbus': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateMbus,
                    request_deserializer=api_dot_synerex__pb2.MbusOpt.FromString,
                    response_serializer=api_dot_synerex__pb2.Mbus.SerializeToString,
            ),
            'CloseMbus': grpc.unary_unary_rpc_method_handler(
                    servicer.CloseMbus,
                    request_deserializer=api_dot_synerex__pb2.Mbus.FromString,
                    response_serializer=api_dot_synerex__pb2.Response.SerializeToString,
            ),
            'SubscribeMbus': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeMbus,
                    request_deserializer=api_dot_synerex__pb2.Mbus.FromString,
                    response_serializer=api_dot_synerex__pb2.MbusMsg.SerializeToString,
            ),
            'SendMbusMsg': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMbusMsg,
                    request_deserializer=api_dot_synerex__pb2.MbusMsg.FromString,
                    response_serializer=api_dot_synerex__pb2.Response.SerializeToString,
            ),
            'GetMbusState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMbusState,
                    request_deserializer=api_dot_synerex__pb2.Mbus.FromString,
                    response_serializer=api_dot_synerex__pb2.MbusState.SerializeToString,
            ),
            'SubscribeGateway': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeGateway,
                    request_deserializer=api_dot_synerex__pb2.GatewayInfo.FromString,
                    response_serializer=api_dot_synerex__pb2.GatewayMsg.SerializeToString,
            ),
            'ForwardToGateway': grpc.unary_unary_rpc_method_handler(
                    servicer.ForwardToGateway,
                    request_deserializer=api_dot_synerex__pb2.GatewayMsg.FromString,
                    response_serializer=api_dot_synerex__pb2.Response.SerializeToString,
            ),
            'CloseDemandChannel': grpc.unary_unary_rpc_method_handler(
                    servicer.CloseDemandChannel,
                    request_deserializer=api_dot_synerex__pb2.Channel.FromString,
                    response_serializer=api_dot_synerex__pb2.Response.SerializeToString,
            ),
            'CloseSupplyChannel': grpc.unary_unary_rpc_method_handler(
                    servicer.CloseSupplyChannel,
                    request_deserializer=api_dot_synerex__pb2.Channel.FromString,
                    response_serializer=api_dot_synerex__pb2.Response.SerializeToString,
            ),
            'CloseAllChannels': grpc.unary_unary_rpc_method_handler(
                    servicer.CloseAllChannels,
                    request_deserializer=api_dot_synerex__pb2.ProviderID.FromString,
                    response_serializer=api_dot_synerex__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.Synerex', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Synerex(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def NotifyDemand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.Synerex/NotifyDemand',
            api_dot_synerex__pb2.Demand.SerializeToString,
            api_dot_synerex__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NotifySupply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.Synerex/NotifySupply',
            api_dot_synerex__pb2.Supply.SerializeToString,
            api_dot_synerex__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ProposeDemand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.Synerex/ProposeDemand',
            api_dot_synerex__pb2.Demand.SerializeToString,
            api_dot_synerex__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ProposeSupply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.Synerex/ProposeSupply',
            api_dot_synerex__pb2.Supply.SerializeToString,
            api_dot_synerex__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SelectSupply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.Synerex/SelectSupply',
            api_dot_synerex__pb2.Target.SerializeToString,
            api_dot_synerex__pb2.ConfirmResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SelectModifiedSupply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.Synerex/SelectModifiedSupply',
            api_dot_synerex__pb2.Supply.SerializeToString,
            api_dot_synerex__pb2.ConfirmResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SelectDemand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.Synerex/SelectDemand',
            api_dot_synerex__pb2.Target.SerializeToString,
            api_dot_synerex__pb2.ConfirmResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Confirm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.Synerex/Confirm',
            api_dot_synerex__pb2.Target.SerializeToString,
            api_dot_synerex__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeDemand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/api.Synerex/SubscribeDemand',
            api_dot_synerex__pb2.Channel.SerializeToString,
            api_dot_synerex__pb2.Demand.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeSupply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/api.Synerex/SubscribeSupply',
            api_dot_synerex__pb2.Channel.SerializeToString,
            api_dot_synerex__pb2.Supply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateMbus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.Synerex/CreateMbus',
            api_dot_synerex__pb2.MbusOpt.SerializeToString,
            api_dot_synerex__pb2.Mbus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CloseMbus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.Synerex/CloseMbus',
            api_dot_synerex__pb2.Mbus.SerializeToString,
            api_dot_synerex__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeMbus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/api.Synerex/SubscribeMbus',
            api_dot_synerex__pb2.Mbus.SerializeToString,
            api_dot_synerex__pb2.MbusMsg.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendMbusMsg(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.Synerex/SendMbusMsg',
            api_dot_synerex__pb2.MbusMsg.SerializeToString,
            api_dot_synerex__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMbusState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.Synerex/GetMbusState',
            api_dot_synerex__pb2.Mbus.SerializeToString,
            api_dot_synerex__pb2.MbusState.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeGateway(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/api.Synerex/SubscribeGateway',
            api_dot_synerex__pb2.GatewayInfo.SerializeToString,
            api_dot_synerex__pb2.GatewayMsg.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ForwardToGateway(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.Synerex/ForwardToGateway',
            api_dot_synerex__pb2.GatewayMsg.SerializeToString,
            api_dot_synerex__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CloseDemandChannel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.Synerex/CloseDemandChannel',
            api_dot_synerex__pb2.Channel.SerializeToString,
            api_dot_synerex__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CloseSupplyChannel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.Synerex/CloseSupplyChannel',
            api_dot_synerex__pb2.Channel.SerializeToString,
            api_dot_synerex__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CloseAllChannels(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.Synerex/CloseAllChannels',
            api_dot_synerex__pb2.ProviderID.SerializeToString,
            api_dot_synerex__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
