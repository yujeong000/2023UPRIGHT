import pickle

# data_path = r'F:\2023_2\CapstoneProject\mmaction2\project\dataset\gesture_pkl_dataset\A001\A001_0.pkl'
# data_path = r'F:\2023_2\CapstoneProject\mmaction2\project\dataset\ntu60_2d.pkl'
data_path = r'F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\1_gesture_pkl_dataset\A002\A00_S03_F_A_03_006_01_MO_B02_1.pkl'
data_path = r'F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\gesture_FrameAug10.pkl'
data_path = r'F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\gesture_FlipAug.pkl'
data_path = r'F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\gesture_Flip_fineAug.pkl'

with open(data_path,"rb") as fr:
    data = pickle.load(fr)
    
# print(data.keys())

# print(data['split'].keys())

print(len(data['split']['train']))

print(len(data['split']['val']))

print(len(data['split']['test']))
# print(data['split']['test'])

print('======================= annotations ===========================')

print(len(data['annotations']))
num = 3
print(data['annotations'][num].keys())

print(data['annotations'][num]['keypoint'])

print(data['annotations'][num]['keypoint_score'].shape)

print(data['annotations'][num]['frame_dir'])  # A001_0: 그대로

print(data['annotations'][num]['img_shape'])  # (1080, 1920): 그대로

print(data['annotations'][num]['original_shape']) # (1080, 1920): 그대로

print(data['annotations'][num]['total_frames']) # 10: 증강된 숫자로 변경

print(data['annotations'][num]['label']) # 0: 그대로

# print('======================= One pkl file ===========================')
# print(data.keys())
# print(data['keypoint'])
# total_frame = int(data['duration']*10)
# add_frame_num = round((total_frame - 10) // 9)
# frame_num = 10
# score_shape_2 = int(frame_num + (add_frame_num * (frame_num - 1)))
# print(add_frame_num)
# print(score_shape_2)
# # print(data)
# print(data['duration'])
# print(data['total_frames'])