import pickle
from sklearn.model_selection import train_test_split
from tqdm import tqdm

import os

def get_files(path):
    for root, subdirs, files in os.walk(path):
       
        list_files = []

        if len(files) > 0:
            for f in files:
                fullpath = root + '/' + f
                list_files.append(fullpath)

    return list_files
    
def get_filename(file_path):
    filename = os.path.basename(file_path)
    return filename

def get_subdirectories(path):
    subdirectories = [os.path.join(path, d) for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return subdirectories

def pkl2annotation(input_path, output_path):
    data_dir_list = get_subdirectories(input_path)  
    
    result_filepath = output_path
    
    
    annotations_data = []
    for data_dir in data_dir_list:
    
        data_path_list = get_files(data_dir)
        
        for data_path in data_path_list:
            with open(data_path,"rb") as fr:
                data = pickle.load(fr)
            annotations_data.append(data)
    
    train_data = []
    val_data = []
    test_data = []
    for data_dir in tqdm(data_dir_list, desc="pkl to annotations"):
        data_path_list = get_files(data_dir)
        data_filename_list = [get_filename(data_path[:-4]) for data_path in data_path_list]
        
        #train:validation:test = 8:1:1
        temp_train_data, temp_rest_data = train_test_split(data_filename_list, test_size=0.2, random_state=42)
        temp_val_data, temp_test_data = train_test_split(temp_rest_data, test_size=0.5, random_state=42)
        # train:val = 9:1
        # temp_train_data, temp_val_data = train_test_split(data_filename_list, test_size=0.1, random_state=42)
        train_data +=temp_train_data
        val_data += temp_val_data
        test_data += temp_test_data
    
    
    split_data = {"train": train_data, "val": val_data, "test": test_data}
    datas = {"split": split_data, "annotations": annotations_data}
    
    with open(result_filepath, 'wb') as f:
        pickle.dump(datas, f, pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    input_path = r'F:\2023_2\CapstoneProject\mmaction2\project\dataset\gesture_pkl_dataset'
    
    output_path = r'F:\2023_2\CapstoneProject\mmaction2\project\dataset\1127_gesture_dataset_tvt811.pkl'
    pkl2annotation(input_path, output_path)