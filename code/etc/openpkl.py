import pickle

# data_path = r'F:\2023_2\CapstoneProject\mmaction2\project\dataset\gesture_pkl_dataset\A001\A001_0.pkl'
# data_path = r'F:\2023_2\CapstoneProject\mmaction2\project\dataset\ntu60_2d.pkl'
data_path = r'F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\3_gesture_pkl_FlipAug\A009\A00_S01_F_C_02_032_01_MO_B09_3.pkl'

with open(data_path,"rb") as fr:
    data = pickle.load(fr)
    
# print(data.keys())

# print(data['split'].keys())

# print(len(data['split']['train']))

# print(len(data['split']['val']))

# print(len(data['split']['test']))

print('======================= annotations ===========================')

# print(len(data['annotations']))

# print(data['annotations'][0].keys())

# print(data['annotations'][0]['keypoint'])

# print(data['annotations'][0]['keypoint_score'].shape)

# print(data['annotations'][0]['frame_dir'])  # A001_0: 그대로

# print(data['annotations'][0]['img_shape'])  # (1080, 1920): 그대로

# print(data['annotations'][0]['original_shape']) # (1080, 1920): 그대로

# print(data['annotations'][0]['total_frames']) # 10: 증강된 숫자로 변경

# print(data['annotations'][0]['label']) # 0: 그대로

print('======================= One pkl file ===========================')
print(data.keys())
# print(data)
print(data['duration'])
print(data['total_frames'])
print(data['keypoint'])