import numpy as np
import pickle
import random

def Finetunning_Aug(input_path, output_path):
    # 씨드를 42로 고정
    random.seed(42)

    with open(input_path,"rb") as fr:
        data = pickle.load(fr)
              
    for i in range(len(data['keypoint'][0])):
        for j in range(len(data['keypoint'][0][i])):
            for k in range(len(data['keypoint'][0][i][j])):
                npoint = data['keypoint'][0][i][j][k] - round(random.uniform(-5, 5))
                # height 0~1080
                if(k == 0 and npoint > 1080):
                    npoint = 1080
                # width 0~1920
                elif(k == 1 and npoint > 1920):
                    npoint = 1920
                elif(npoint < 0):
                    npoint = 0    
                data['keypoint'][0][i][j][k] = npoint
                                        
    data['frame_dir'] = data['frame_dir'] + "_finetunning"
    # Save the modified data to a pickle file
    with open(output_path, 'wb') as f:
        pickle.dump(data, f)

    return data       

if __name__ == '__main__':
# Example usage
    json_file_path = r"F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\0_gesture_pkl_dataset\A001\A00_S01_F_C_01_029_01_MO_B01_1.pkl"
    output_path = r"F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\testFinetunningAug.pkl"
    loaded_data = Finetunning_Aug(json_file_path,output_path)
    