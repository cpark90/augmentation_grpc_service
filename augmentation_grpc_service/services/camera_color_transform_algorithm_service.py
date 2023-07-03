import protos.augmentation_service_pb2_grpc as augmentation_service
import protos.augmentation_service_message_pb2 as augmentation_service_message
from augmentation_grpc_service.augmentation_algorithms.camera_color_transform import CameraColorTransformAlgorithm

class CameraColorTransformAlgorithmServicer(augmentation_service.AugmentationServicer):

    def InitEngine(self, request, context):
        metadata = dict(context.invocation_metadata())
        request_data = request.data

        if request_data == "init":
            result = True
        else:
            result = False

        return augmentation_service_message.InitEngineResponse(response=result)

    def Augment(self, request, context):
        metadata = dict(context.invocation_metadata())
        camera_color_transform_algorithm = CameraColorTransformAlgorithm("test")
        result_data, error_status = camera_color_transform_algorithm.run(request.src_directory_path,
                                request.src_GT_directory_path,
                                request.tgt_directory_path,
                                request.tgt_GT_directory_path,
                                request.src_sensor_profile_path,
                                request.tgt_sensor_profile_path,
                                request.transform_config_path)
        
        return augmentation_service_message.AugmentResponse(response=result_data, error_status=error_status)
        

    def Validate(self, request, context):
        return augmentation_service_message.ValidateResponse(response=False, error_status="NotValdiateLogic")