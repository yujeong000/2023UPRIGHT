import cv2
import json
import pickle
import os

def get_files(path, extension):
    list_files = []
    
    for root, subdirs, files in os.walk(path):
        if len(files) > 0:
            for f in files:
                fullpath = os.path.join(root, f)
                if f.lower().endswith(extension):
                    list_files.append(fullpath)

    return list_files

if __name__ == '__main__':

    json_file_path = r"F:\2023_2\CapstoneProject\mmaction2\project\dataset\gesture_jpg_dataset\A007\json\A00_S01_F_C_01_029_01_MO_B07_1.json"
    pkl_file_path = r"F:\2023_2\CapstoneProject\mmaction2\project\dataset\1122_gesture_pkl_dataset\A007\A007_0.pkl"
    image_file_path = r"F:\2023_2\CapstoneProject\mmaction2\project\dataset\gesture_jpg_dataset\A007\A00_S01_F_C_01_029_01_MO_B07_1_0.jpg"
    output_file = r"F:\2023_2\CapstoneProject\mmaction2\project\vis\B01_.jpg"

    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    img = cv2.imread(image_file_path, cv2.IMREAD_UNCHANGED)
    index = 0
    cv2.putText(img, 'json', [50,50], cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 5)
    for row in data['annotation'][0]['keypoints']:
        point1 = [int(row[0]), int(row[1])]
        cv2.circle(img, point1, 3, (0, 255, 0), 1)
        cv2.putText(img, str(index), point1, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        index += 1
        
    with open(pkl_file_path,"rb") as fr:
        data = pickle.load(fr)

    index = 0
    cv2.putText(img, 'pkl', [50,100], cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 5)
    for row in data['keypoint'][0][0]:
        point1 = [int(row[0]), int(row[1])]
        cv2.circle(img, point1, 3, (0, 0, 255), 1)
        cv2.putText(img, str(index), point1, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        index += 1
        
    cv2.imwrite(output_file, img)
        



