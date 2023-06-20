import .scenario_control_pb2_grpc as scenario_control
import .scenario_control_message_pb2 as scenario_control_message
from .augmentation_grpc_service.augmentation_algorithms import PrototypeAlgorithm

class ScenarioControlServicer(scenario_control.ScenarioControlServicer):

    def InitScenario(self, request, context):
        metadata = dict(context.invocation_metadata())
        scenario_info = request.info

        if scenario_info.data == "init":
            result = True
        else:
            result = False

        return scenario_control_message.ScenarioInitResponse(status=result)

    def ModifyScenario(self, request, context):
        metadata = dict(context.invocation_metadata())
        scenario_info = request.info

        if scenario_info.data == "modify":
            pre_check = True
        else:
            pre_check = False

        for scenario_modify_data in request.data:
            if pre_check and scenario_modify_data == "success":
                result = True
            else:
                result = False
            yield scenario_control_message.ScenarioModifyResponse(status=result)
        prototype_algorithm = PrototypeAlgorithm("test")
        prototype_algorithm.run()
        

    def TerminateScenario(self, request, context):
        metadata = dict(context.invocation_metadata())

        scenario_info = request.info

        if scenario_info.data == "terminate":
            result = True
        else:
            result = False

        return scenario_control_message.ScenarioTerminateResponse(status=result)