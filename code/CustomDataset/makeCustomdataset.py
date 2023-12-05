import os
from tqdm import tqdm

from Utils import get_files, get_last_directory_name, make_dir, get_subdirectories
from FrameAugmentation import frame_augment_data
from FlippingAugmentation import flipping_Aug
from json2pkl import process_and_save_json
from pkl2anno import pkl2annotation

def json_to_pkl_files(input_dir_path, output_dir_path):
    #입력 데이터셋 폴더
    data_dir_list = get_subdirectories(input_dir_path)
    #출력 데이터셋 폴더
    make_dir(output_dir_path)
    for data_dir in tqdm(data_dir_list, desc="json to pkl"):
        last_dir = get_last_directory_name(data_dir)
        result_subdirectory = os.path.join(output_dir_path, last_dir)
        make_dir(result_subdirectory)
        
        label = int(last_dir.split('A')[1][:3]) - 1
        json_file_list = get_files(data_dir, '.json')
        for json_file in json_file_list:
            frame_dir = get_last_directory_name(json_file)[:-5]
            output_path = rf'{result_subdirectory}/{frame_dir}'
            result_data = process_and_save_json(json_file, output_path + '.pkl', frame_dir, label)
    return result_data

def pkl_FrameAug(input_dir_path, output_dir_path, fps):
    #입력 데이터셋 폴더
    data_dir_list = get_subdirectories(input_dir_path) 
    #출력 데이터셋 폴더
    result_folder = output_dir_path
    make_dir(result_folder)
    
    for data_dir in tqdm(data_dir_list, desc="Data augmentation: FrameAug"):
        result_subdirectory = os.path.join(result_folder, get_last_directory_name(data_dir))
        make_dir(result_subdirectory)
        pkl_file_list = get_files(data_dir, '.pkl')
        for pkl_file in pkl_file_list:
            output_path = rf'{result_subdirectory}/{get_last_directory_name(pkl_file)}'
            augmented_data = frame_augment_data(pkl_file, output_path, fps)
    return augmented_data

def pkl_FlippingAug(input_dir_path, output_dir_path):
    #입력 데이터셋 폴더
    data_dir_list = get_subdirectories(input_dir_path)
    #출력 데이터셋 폴더
    make_dir(output_dir_path)
    for data_dir in tqdm(data_dir_list, desc="Data augmentation: FlippingAug"):
        last_dir = get_last_directory_name(data_dir)
        result_subdirectory = os.path.join(output_dir_path, last_dir)
        make_dir(result_subdirectory)
        
        pkl_file_list = get_files(data_dir, '.pkl')
        for pkl_file in pkl_file_list:
            output_path = rf'{result_subdirectory}/{get_last_directory_name(pkl_file)}'
            augmented_data = flipping_Aug(pkl_file, output_path)
    return augmented_data

if __name__ == '__main__':
    
    jpg_dataset = r'F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\0_gesture_jpg_dataset'
    pkl_dataset = r'F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\1_gesture_pkl_dataset'
    frameAug_dataset = r'F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\2_gesture_pkl_FrameAug'
    flipAug_dataset = r'F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\3_gesture_pkl_FlipAug'
    annos_dataset = r'F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\gesture.pkl'
    
    ### json2pkl
    json_to_pkl_files(jpg_dataset, pkl_dataset)
        
    ###Data augmentation
    pkl_FrameAug(pkl_dataset, frameAug_dataset, 30)
    pkl_FlippingAug(frameAug_dataset, flipAug_dataset)
            
    ###pkl2annotations
    pkl2annotation(frameAug_dataset, annos_dataset)