import grpc
import protos.augmentation_service_message_pb2 as augmentation_service_message_pb2
import protos.augmentation_service_pb2_grpc as augmentation_service_pb2_grpc

def run():

    with grpc.insecure_channel('0.0.0.0:50051') as channel:
    
        stub = augmentation_service_pb2_grpc.AugmentationStub(channel)

        request = augmentation_service_message_pb2.AugmentRequest(
            src_directory_path="/workspace/sample_data/kitti/image_02/data",
            src_GT_directory_path="/workspace/sample_data/kitti/gt_image_02/data",
            tgt_directory_path="/workspace/sample_data/kitti/test_result/image_02_transformed",
            tgt_GT_directory_path="/workspace/sample_data/kitti/test_result/gt_02_transformed",
            src_sensor_profile_path="/workspace/src/configs/calib_cam_2.yaml",
            tgt_sensor_profile_path="/workspace/sample_data/kitti/test_result/calib_cam_2.yaml",
            transform_config_path="/workspace/src/configs/camera_transform_config.yaml"
        )

        responses = stub.Augment(request)
        if responses is not None:  
            print(responses)
        else:
            print("Transfer failed")

if __name__ == "__main__":
    run()
