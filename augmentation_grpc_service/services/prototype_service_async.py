from grpc import aio

import .scenario_control_pb2_grpc as scenario_control
import .scenario_control_message_pb2 as scenario_control_message

class ScenarioControlService(scenario_control.ScenarioControlServicer):
    
    def InitScenario(
            self, request: scenario_control_message.ScenarioInitRequest,
            context: aio.ServicerContext) -> scenario_control_message.ScenarioInitResponse:
        metadata = dict(context.invocation_metadata())
        print(metadata)
        scenario_info = request.info

        if scenario_info.data == "success":
            result = True
        else:
            result = False

        return scenario_control_message.ScenarioInitResponse(success=result)

    def ModifyScenario(
            self, request: scenario_control_message.ScenarioModifyRequest,
            context: aio.ServicerContext) -> scenario_control_message.ScenarioModifyResponse:
        metadata = dict(context.invocation_metadata())
        print(metadata)
        scenario_info = request.info

        if scenario_info.data == "success":
            pre_check = True
        else:
            pre_check = False

        for scenario_modify_data in request.data:
            if pre_check and scenario_modify_data == "success":
                result = True
            else:
                result = False
            yield scenario_control_message.ScenarioModifyResponse(success=result)
        

    def TerminateScenario(self, request, context):
        metadata = dict(context.invocation_metadata())
        print(metadata)
        scenario_info = request.info

        if scenario_info.data == "success":
            result = True
        else:
            result = False

        return scenario_control_message.ScenarioTerminateResponse(success=result)