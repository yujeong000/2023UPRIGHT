import cv2
import os
from tqdm import tqdm
from Utils import get_files, get_last_directory_name, make_dir, get_subdirectories

def divide_into_batches(image_file_list, batch_size, overlap_range):
    batches = [image_file_list[i:i+batch_size] for i in range(0, len(image_file_list) -len(image_file_list)%(batch_size-overlap_range), batch_size-overlap_range)]
    return batches

def convert_images_to_videos(input_folder, output_folder, fps, batch_size, frame_overlap_range):
    
    index = 0
    image_file_list = get_files(input_folder, '.jpg')
    batched_lists = divide_into_batches(image_file_list, batch_size, frame_overlap_range)     # [[image_file_list를 10개씩 나누어 저장],[...]]

    for image in tqdm(batched_lists, desc="Total"):
        img = cv2.imread(image[0])
        height, width, channel = img.shape
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        output_path = rf'{output_folder}/{index}.mp4'
        writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        for file in image:
            f = cv2.imread(file)
            writer.write(f)

        writer.release()
        index += 1
            