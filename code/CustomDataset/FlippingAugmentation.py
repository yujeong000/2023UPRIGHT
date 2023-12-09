import numpy as np
import pickle

def flipping_Aug(input_path, output_path):
    with open(input_path,"rb") as fr:
        data = pickle.load(fr)
    
    img_shape_2 = int(data["img_shape"][1])
    
    idx_j=0
    for i in data["keypoint"]:
        for j in i:
            j[[1,2]] = j[[2,1]]
            j[[3,4]] = j[[4,3]]
            j[[5,6]] = j[[6,5]]
            j[[7,8]] = j[[8,7]]
            j[[9,10]] = j[[10,9]]
            j[[11,12]] = j[[12,11]]
            j[[13,14]] = j[[14,13]]
            j[[15,16]] = j[[16,15]]
            
            data["keypoint"][0][idx_j] = j
            idx_j+=1
            
    data['frame_dir'] = data['frame_dir'] + "_flip"
    # Save the modified data to a pickle file
    with open(output_path, 'wb') as f:
        pickle.dump(data, f)

    return data       

if __name__ == '__main__':
# Example usage
    json_file_path = r"F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\1_gesture_pkl_dataset\A001\A00_S01_F_C_01_029_01_MO_B01_1.pkl"
    output_path = r"F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\testFlippingAug.pkl"
    loaded_data = flipping_Aug(json_file_path,output_path)
    