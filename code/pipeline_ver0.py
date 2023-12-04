import cv2
import tempfile
import os
from tqdm import tqdm
from Utils import get_files, get_last_directory_name, make_dir, get_subdirectories
from jpg2mp4 import convert_images_to_videos

if __name__ == '__main__':
    ### Load video
    MP4_path = r'F:\2023_2\CapstoneProject\mmaction2\project\dataset\ISEGYE_IDOL_KIDDING_Official_MV.mp4'
    ### extract frame
    Frame_dir_path = r'F:\2023_2\CapstoneProject\mmaction2\project\dataset\pipeline_extract_frame'
    make_dir(Frame_dir_path)
    ### jpg2mp4
    split_MP4_dir_path = r'F:\2023_2\CapstoneProject\mmaction2\project\dataset\pipeling_split_MP4'
    make_dir(split_MP4_dir_path)
    JPG_per_second = 5          # extract n fps
    frame_overlap_range = 1     # jpg 2 MP4 생성시 겹치는 프레임 범위
    
    
    # ###============================================================
    # ### Load video
    # video = cv2.VideoCapture(MP4_path)
    # if not video.isOpened():
    #     print("Could not Open :", MP4_path)
    #     exit(0)
        
    # ### extract frame
    # make_dir(Frame_dir_path)
    
    # count = 0
    
    # fps = video.get(cv2.CAP_PROP_FPS)
    # fps = fps/JPG_per_second
    # fps = round(fps)

    # while(video.isOpened()):
    #     ret, image = video.read()
    #     if not ret:
    #         break  # 더 이상 프레임을 읽을 수 없으면 루프 탈출
    #     if(int(video.get(1)) % fps == 0): #앞서 불러온 fps 값을 사용하여 1초마다 추출
    #         cv2.imwrite(rf"{Frame_dir_path}/{count:05d}.jpg", image)
    #         # print('Saved frame number :', str(int(video.get(1))))
    #         count += 1

    # video.release()
    # print("JPG 개수: " + str(count))
    
    # ### jpg2mp4
    # converter = convert_images_to_videos(input_folder=Frame_dir_path,
    #                                   output_folder=split_MP4_dir_path,
    #                                   fps=10,
    #                                   batch_size=10,
    #                                   frame_overlap_range = frame_overlap_range)
    
    
    ### 
    