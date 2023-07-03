import numpy as np

class CameraColorTransformAlgorithm(object):

    def __init__(self, args):
        self.args = args
        self.np_array = np.array([0, 1, 2, 3, 4])
    
    def run(self, src_directory_path,
                src_GT_directory_path,
                tgt_directory_path,
                tgt_GT_directory_path,
                src_sensor_profile_path,
                tgt_sensor_profile_path,
                transform_config_path):
        result_data = True
        error_status = ""
        return result_data, error_status
    

if __name__ == "__main__":
    prototype_algorithm = CameraColorTransformAlgorithm("test")
    src_directory_path = "/media/external_storage/2323/src_directory_path.txt"
    src_GT_directory_path = "src_GT_directory_path"
    tgt_directory_path = "tgt_directory_path"
    tgt_GT_directory_path = "tgt_GT_directory_path"
    src_sensor_profile_path = "src_sensor_profile_path"
    tgt_sensor_profile_path = "tgt_sensor_profile_path"
    transform_config_path = "transform_config_path"
    result_data, error_status = prototype_algorithm.run(src_directory_path,
                                src_GT_directory_path,
                                tgt_directory_path,
                                tgt_GT_directory_path,
                                src_sensor_profile_path,
                                tgt_sensor_profile_path,
                                transform_config_path)
    print(result_data)
    print(error_status)