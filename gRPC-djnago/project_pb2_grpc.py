# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import project_pb2 as project__pb2


class AuthorModelControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
                '/project.AuthorModelController/List',
                request_serializer=project__pb2.AuthorModelListRequest.SerializeToString,
                response_deserializer=project__pb2.AuthorModel.FromString,
                )
        self.Create = channel.unary_unary(
                '/project.AuthorModelController/Create',
                request_serializer=project__pb2.AuthorModel.SerializeToString,
                response_deserializer=project__pb2.AuthorModel.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/project.AuthorModelController/Retrieve',
                request_serializer=project__pb2.AuthorModelRetrieveRequest.SerializeToString,
                response_deserializer=project__pb2.AuthorModel.FromString,
                )
        self.Update = channel.unary_unary(
                '/project.AuthorModelController/Update',
                request_serializer=project__pb2.AuthorModel.SerializeToString,
                response_deserializer=project__pb2.AuthorModel.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/project.AuthorModelController/Destroy',
                request_serializer=project__pb2.AuthorModel.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class AuthorModelControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthorModelControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=project__pb2.AuthorModelListRequest.FromString,
                    response_serializer=project__pb2.AuthorModel.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=project__pb2.AuthorModel.FromString,
                    response_serializer=project__pb2.AuthorModel.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=project__pb2.AuthorModelRetrieveRequest.FromString,
                    response_serializer=project__pb2.AuthorModel.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=project__pb2.AuthorModel.FromString,
                    response_serializer=project__pb2.AuthorModel.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=project__pb2.AuthorModel.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'project.AuthorModelController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AuthorModelController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/project.AuthorModelController/List',
            project__pb2.AuthorModelListRequest.SerializeToString,
            project__pb2.AuthorModel.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/project.AuthorModelController/Create',
            project__pb2.AuthorModel.SerializeToString,
            project__pb2.AuthorModel.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/project.AuthorModelController/Retrieve',
            project__pb2.AuthorModelRetrieveRequest.SerializeToString,
            project__pb2.AuthorModel.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/project.AuthorModelController/Update',
            project__pb2.AuthorModel.SerializeToString,
            project__pb2.AuthorModel.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Destroy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/project.AuthorModelController/Destroy',
            project__pb2.AuthorModel.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class BookControllerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
                '/project.BookController/List',
                request_serializer=project__pb2.BookRequest.SerializeToString,
                response_deserializer=project__pb2.BookResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/project.BookController/Create',
                request_serializer=project__pb2.BookResponse.SerializeToString,
                response_deserializer=project__pb2.BookResponse.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/project.BookController/Retrieve',
                request_serializer=project__pb2.BookRequest.SerializeToString,
                response_deserializer=project__pb2.BookResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/project.BookController/Update',
                request_serializer=project__pb2.BookResponse.SerializeToString,
                response_deserializer=project__pb2.BookResponse.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/project.BookController/Destroy',
                request_serializer=project__pb2.BookResponse.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class BookControllerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BookControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=project__pb2.BookRequest.FromString,
                    response_serializer=project__pb2.BookResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=project__pb2.BookResponse.FromString,
                    response_serializer=project__pb2.BookResponse.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=project__pb2.BookRequest.FromString,
                    response_serializer=project__pb2.BookResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=project__pb2.BookResponse.FromString,
                    response_serializer=project__pb2.BookResponse.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=project__pb2.BookResponse.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'project.BookController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BookController(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/project.BookController/List',
            project__pb2.BookRequest.SerializeToString,
            project__pb2.BookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/project.BookController/Create',
            project__pb2.BookResponse.SerializeToString,
            project__pb2.BookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/project.BookController/Retrieve',
            project__pb2.BookRequest.SerializeToString,
            project__pb2.BookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/project.BookController/Update',
            project__pb2.BookResponse.SerializeToString,
            project__pb2.BookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Destroy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/project.BookController/Destroy',
            project__pb2.BookResponse.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
