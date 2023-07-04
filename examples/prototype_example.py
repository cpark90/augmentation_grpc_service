from augmentation_grpc_service.grpc_server_sync import GrpcServerSync
import protos.augmentation_service_pb2_grpc as augmentation_service_pb2_grpc
from augmentation_grpc_service.services.prototype_service_sync import PrototypeAlgorithmServicer

if __name__ == "__main__":
    server = GrpcServerSync(augmentation_service_pb2_grpc, "AugmentationServicer", PrototypeAlgorithmServicer)
    server.serve()