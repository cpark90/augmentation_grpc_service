import .augmentation_service_pb2_grpc as augmentation_service
import .augmentation_service_message_pb2 as augmentation_service_message
from augmentation_grpc_service.augmentation_algorithms import PrototypeValidationAlgorithm

class AugmentationServicer(augmentation_service.AugmentationServicer):

    def InitEngine(self, request, context):
        metadata = dict(context.invocation_metadata())
        request_data = request.data

        if request_data == "init":
            result = True
        else:
            result = False

        return augmentation_service_message.InitEngineResponse(response=result)

    def Augment(self, request, context):
        print(request)
        return augmentation_service_message.AugmentResponse(response=False, error_status="NotAugmentLogic")
        

    def Validate(self, request, context):
        prototype_validation_algorithm = PrototypeValidationAlgorithm("test")
        result_data, error_status = prototype_validation_algorithm.run(request.src_sensor_profile_path,
                                                                       request.transform_config_path,
                                                                       request.src_directory_path)

        return augmentation_service_message.ValidateResponse(response=result_data, error_status=error_status)