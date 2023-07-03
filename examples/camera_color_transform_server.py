from augmentation_grpc_service import GrpcServerSync
import protos.augmentation_service_pb2_grpc as augmentation_service_pb2_grpc
from augmentation_grpc_service.services.prototype_service_sync import AugmentationServicer

if __name__ == "__main__":
    server = GrpcServerSync(augmentation_service_pb2_grpc, "AugmentationServicer", AugmentationServicer)
    server.serve()