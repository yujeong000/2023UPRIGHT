import json
import numpy as np
import pickle

def flipping_Aug(input_path, output_path):
    with open(input_path,"rb") as fr:
        data = pickle.load(fr)
    
    img_shape_2 = int(data["img_shape"][1])
    
    for i in data["keypoint"]:
        for j in i[:17]:
            for k in j[:17]:
                k[0] = img_shape_2 - k[0]
    
    # Save the modified data to a pickle file
    with open(output_path, 'wb') as f:
        pickle.dump(data, f)

    return data       

if __name__ == '__main__':
# Example usage
    json_file_path = r"C:\Users\USER\Desktop\23upright\mmaction2\23upright\dataset\pklfilezip\pkl_test.pkl"
    output_path = r"C:\Users\USER\Desktop\23upright\mmaction2\23upright\dataset\pklfilezip\pkl_fliptest.pkl"
    loaded_data = flipping_Aug(json_file_path,output_path)
    
    print(loaded_data)
    