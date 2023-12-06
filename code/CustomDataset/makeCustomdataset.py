import os
import shutil
from tqdm import tqdm


from Utils import get_files, get_last_directory_name, make_dir, get_subdirectories, remove_dir
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
            output_path = rf'{result_subdirectory}/{get_last_directory_name(pkl_file)[:-4]}_frame{fps}.pkl'
            augmented_data = frame_augment_data(pkl_file, output_path, fps)

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
            output_path = rf'{result_subdirectory}/{get_last_directory_name(pkl_file)[:-4]}_flip.pkl'
            flipping_Aug(pkl_file, output_path)
            
def move_pkl_files(source_dir, target_dir):

    # source_dir 내의 모든 파일을 대상으로 반복
    for item in os.listdir(source_dir):
        if item.endswith('.pkl'):
            # 파일의 전체 경로 생성
            source_file = os.path.join(source_dir, item)
            target_file = os.path.join(target_dir, item)

            # 파일을 새 디렉토리로 복사
            shutil.copy2(source_file, target_file)
            
def merge_dir(source1_dir, source2_dir, output_dir_path):
    make_dir(output_dir_path)
    
    data_dir1_list = get_subdirectories(source1_dir)
    for data_dir in tqdm(data_dir1_list, desc="Merge dir1: "):
        last_dir = get_last_directory_name(data_dir)
        result_subdirectory = os.path.join(output_dir_path, last_dir)
        make_dir(result_subdirectory)
        move_pkl_files(data_dir, result_subdirectory)
        
    data_dir2_list = get_subdirectories(source2_dir)
    for data_dir in tqdm(data_dir2_list, desc="Merge dir2: "):
        last_dir = get_last_directory_name(data_dir)
        result_subdirectory = os.path.join(output_dir_path, last_dir)
        make_dir(result_subdirectory)
        move_pkl_files(data_dir, result_subdirectory)
        

if __name__ == '__main__':
    _fps = 30
    
    jpg_dataset = r'F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\0_gesture_jpg_dataset'
    pkl_dataset = r'F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\1_gesture_pkl_dataset'
    remove_dir(pkl_dataset)
    temp_flipAug_dataset = r'F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\2_temp_gesture_pkl_Aug_flip'
    remove_dir(temp_flipAug_dataset)
    flipAug_dataset = r'F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\2_gesture_pkl_Aug_flip'
    remove_dir(flipAug_dataset)
    frameAug_dataset = rf'F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\3_gesture_pkl_Aug_frame{_fps}'
    remove_dir(frameAug_dataset)
    flip_frameAug_dataset = rf'F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\4_gesture_pkl_Aug_flip_frame{_fps}'
    remove_dir(flip_frameAug_dataset)
    
    ## json2pkl
    json_to_pkl_files(jpg_dataset, pkl_dataset)
    
    ###flipAug#####################################
    print('###flipAug#####################################')
    annos_dataset = r'F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\gesture_FlipAug.pkl'
        
    ## Frame augmentation
    pkl_FlippingAug(pkl_dataset, temp_flipAug_dataset)
    
    ## merge dir
    merge_dir(pkl_dataset, temp_flipAug_dataset, flipAug_dataset) 
            
    ## pkl2annotations
    pkl2annotation(flipAug_dataset, annos_dataset)
    
    ###frameAug#####################################
    print('###frameAug#####################################')
    annos_dataset = rf'F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\gesture_FrameAug{_fps}.pkl'

    ## Frame augmentation
    pkl_FrameAug(pkl_dataset, frameAug_dataset, _fps)
            
    ## pkl2annotations
    pkl2annotation(frameAug_dataset, annos_dataset)
    
    
    ###frame + flipAug#####################################
    print('###frame + flipAug#####################################')
    annos_dataset = rf'F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\gesture_Flip_frameAug{_fps}.pkl'
        
    ## Frame augmentation
    pkl_FrameAug(flipAug_dataset, flip_frameAug_dataset, _fps)
            
    ## pkl2annotations
    pkl2annotation(flip_frameAug_dataset, annos_dataset)