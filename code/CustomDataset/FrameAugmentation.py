    # print(data)
        
    # print('======================= split ===========================')
    # print(data.keys())

    # print(data['split'].keys())

    # print(len(data['split']['train']))

    # print(len(data['split']['val']))

    # print(len(data['split']['test']))

    # print('======================= annotations ===========================')

    # 각 프레임 사이에 i장 추가

    # print(len(data['annotations']))

    # print(data['annotations'][0].keys())

    # print(data['annotations'][0]['keypoint'][0]) # shape: (1, 10, 17, 2) 프레임 10장, 키포인트 17개, 2차원(x, y) 좌표 ==> Finish

    # print(data['annotations'][0]['keypoint_score'][0][0]) # shape: (1, 10, 17), 프레임 10장, 키포인트 17개, 어떻게 할지?

    # print(data['annotations'][0]['frame_dir'])  # A001_0: 그대로

    # print(data['annotations'][0]['img_shape'])  # (1080, 1920): 그대로

    # print(data['annotations'][0]['original_shape']) # (1080, 1920): 그대로

    # print(data['annotations'][0]['total_frames']) # 10: 증강된 숫자로 변경 -> 10 + i * (10-1)

    # print(data['annotations'][0]['label']) # 0: 그대로

import pickle
import numpy as np

def frame_augment_data(data_path, output_path, fps):
    #print(data_path)
    with open(data_path,"rb") as fr:
        data = pickle.load(fr)
    #print(data['duration'])
    #print(data['total_frames'])  
    #print(data['keypoint'].shape)
    
    total_frame = int(data['duration']*fps)
    add_frame_num = round((total_frame - 10) // 9)
    if add_frame_num <0:
        add_frame_num = 0
    #print(add_frame_num)

    # print('======================= Data Augmentation ===========================')
    frame_num = data['total_frames']
    keypoint_num = 17

    # print('==================== Keypoint =======================')
    annos_keypoint = np.array(data['keypoint'][0])
    # print(data['keypoint'][0].shape)
    zero_array = np.zeros([keypoint_num,2])
    for i in range(len(annos_keypoint) - 1):
        for _ in range(add_frame_num):
            annos_keypoint = np.insert(annos_keypoint, 1 + i*(add_frame_num + 1), zero_array, axis=0)

    for i in range(frame_num):
        if i == frame_num -1:
            continue
        for k in range(keypoint_num):
            for l in range(2):
                distance = annos_keypoint[(i+1)*(add_frame_num + 1)][k][l] - annos_keypoint[i*(add_frame_num + 1)][k][l]
                per_dist = distance / (add_frame_num + 1)
                for j in range(add_frame_num):
                    index = j + 1
                    annos_keypoint[i*(add_frame_num + 1)+index][k][l] = annos_keypoint[i*(add_frame_num + 1)][k][l] + per_dist * index
        

    data['keypoint'] = np.array([annos_keypoint])
    # print(data['keypoint'])

    # print('==================== Score =======================')
    score_shape_2 = int(frame_num + (add_frame_num * (frame_num - 1)))
    # print(score_shape_2)
    # print(data['keypoint_score'])
    data['keypoint_score'] = np.ones([1, score_shape_2, keypoint_num], dtype=np.float32)
    # print(data['keypoint_score'])


    # print('==================== Total Frames =======================')
    data['total_frames'] = int(score_shape_2)
    data['frame_dir'] = data['frame_dir'] + f"_frame{fps}"
    # if data['duration'] > 1.0:
    
    #     # print(data)
    #print(data['total_frames'])
    #print(data['keypoint'].shape)
    with open(output_path, 'wb') as f:
        pickle.dump(data, f)
                
    return data

if __name__ == '__main__':
    augmented_data = frame_augment_data(r'F:\2023_2\CapstoneProject\mmaction2\project\dataset\gesture_pkl_dataset\A001\A001_0.pkl', 3)

# data_path = r'F:\2023_2\CapstoneProject\mmaction2\project\dataset\gesture_pkl_dataset\A001\A001_0.pkl'
# data_path = r'F:\2023_2\CapstoneProject\mmaction2\project\dataset\ntu60_2d.pkl
# data_path = r'F:\2023_2\CapstoneProject\mmaction2\project\dataset\1122_gesture_dataset_tvt811.pkl'