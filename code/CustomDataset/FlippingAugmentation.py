import numpy as np
import pickle

def flipping_Aug(input_path, output_path):
    with open(input_path,"rb") as fr:
        data = pickle.load(fr)
    
    img_shape_2 = int(data["img_shape"][1])
    
    for i in data["keypoint"]:
        for j in i:
            # print(j)
            for k in j:
                k[0] = img_shape_2 - k[0]
    
    # Save the modified data to a pickle file
    with open(output_path, 'wb') as f:
        pickle.dump(data, f)

    return data       

if __name__ == '__main__':
# Example usage
    json_file_path = r"F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\1_gesture_pkl_dataset\A001\A00_S01_F_C_01_029_01_MO_B01_1.pkl"
    output_path = r"F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\testFlippingAug.pkl"
    loaded_data = flipping_Aug(json_file_path,output_path)
    