from augmentation_grpc_service import GrpcServerSync
import protos.scenario_control_pb2_grpc as scenario_control_pb2_grpc
from protos.scenario_control_pb2_grpc import ScenarioControlServicer

if __name__ == "__main__":
    server = GrpcServerSync(scenario_control_pb2_grpc, "ScenarioControlServicer", ScenarioControlServicer)
    server.serve()