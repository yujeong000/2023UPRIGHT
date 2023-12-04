# from jpg2mp4 import ImageToVideoConverter
from FrameAugmentation import frame_augment_data
from json2pkl import process_and_save_json
from pkl2anno import pkl2annotation
import os
from tqdm import tqdm

from Utils import get_files, get_last_directory_name, make_dir, get_subdirectories


if __name__ == '__main__':
    # converter = ImageToVideoConverter(input_folder=r'F:\2023_2\CapstoneProject\mmaction2\project\dataset\gesture_jpg_dataset',
    #                                   output_folder=r'F:\2023_2\CapstoneProject\mmaction2\project\dataset\gesture_video2_dataset')
    # converter.convert_images_to_videos()
    
    
    ### json2pkl
    #입력 데이터셋 폴더
    data_dir_list = get_subdirectories(r'F:\2023_2\CapstoneProject\mmaction2\project\dataset\gesture_jpg_dataset')
    # print(data_dir_list)
    
    #출력 데이터셋 폴더
    result_folder = r'F:\2023_2\CapstoneProject\mmaction2\project\dataset\gesture_pkl_dataset'
    make_dir(result_folder)
    
    # for data_dir in tqdm(data_dir_list, desc="json to pkl"):
    #     last_dir = get_last_directory_name(data_dir)
    #     result_subdirectory = os.path.join(result_folder, last_dir)
    #     make_dir(result_subdirectory)
        
    #     label = int(last_dir.split('A')[1][:3]) - 1
    #     json_file_list = get_files(data_dir, '.json')
    #     for json_file in json_file_list:
    #         frame_dir = get_last_directory_name(json_file)[:-5]
    #         output_path = rf'{result_subdirectory}/{frame_dir}'
    #         result_data = process_and_save_json(json_file, output_path + '.pkl', frame_dir, label)
        
    
    ####Data augmentation
    
    #입력 데이터셋 폴더
    data_dir_list = get_subdirectories(result_folder)  
    # data_dir_list = get_subdirectories(r'project/dataset/1122_gesture_pkl_dataset')  
    
    #출력 데이터셋 폴더
    result_folder = r'F:\2023_2\CapstoneProject\mmaction2\project\dataset\gesture_pkl_FrameAugmentation'
    make_dir(result_folder)
    
    for data_dir in tqdm(data_dir_list, desc="Data augmentation"):
        result_subdirectory = os.path.join(result_folder, get_last_directory_name(data_dir))
        make_dir(result_subdirectory)
        pkl_file_list = get_files(data_dir, '.pkl')
        for pkl_file in pkl_file_list:
            output_path = rf'{result_subdirectory}/{get_last_directory_name(pkl_file)}'
            augmented_data = frame_augment_data(pkl_file, output_path, 30)
            
    # ###pkl2annotations
    # input_path = result_folder
    # output_path = r'F:\2023_2\CapstoneProject\mmaction2\project\dataset\1128_gesture_aug15.pkl'
    # pkl2annotation(input_path, output_path)