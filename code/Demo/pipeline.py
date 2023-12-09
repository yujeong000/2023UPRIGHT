# Copyright (c) OpenMMLab. All rights reserved.

##more faster version
import pickle

import argparse
import tempfile
import time
from tqdm import tqdm

import cv2
import mmcv
import mmengine
import torch
from mmengine import DictAction
from mmengine.utils import track_iter_progress

from mmaction.apis import (detection_inference, inference_skeleton,
                           init_recognizer, pose_inference)
from mmaction.registry import VISUALIZERS
from mmaction.utils import frame_extract

try:
    import moviepy.editor as mpy
except ImportError:
    raise ImportError('Please install moviepy to enable output file')

from Utils import get_files, make_dir

FONTFACE = cv2.FONT_HERSHEY_DUPLEX
FONTSCALE = 0.75
FONTCOLOR = (255, 255, 255)  # BGR, white
THICKNESS = 1
LINETYPE = 1

BASEPATH = r'F:\2023_2\CapstoneProject\mmaction2\23_CapstoneDesign_UPRIGHT\code\Demo'

def parse_args_default():
    parser = argparse.ArgumentParser(description='MMAction2 demo')
    # parser.add_argument('out_filename', help='output filename')
    parser.add_argument(
        '--det-config',
        default=BASEPATH + r'\detection\faster-rcnn_r50_fpn_2x_coco_infer.py',
        help='human detection config file path (from mmdet)')
    parser.add_argument(
        '--det-checkpoint',
        default=(BASEPATH + r'\detection\det_faster_rcnn_r50_fpn_2x_coco_bbox_mAP-0.384_20200504_210434-a5d8aa15.pth'),
        help='human detection checkpoint file/url')
    parser.add_argument(
        '--det-score-thr',
        type=float,
        default=0.9,
        help='the threshold of human detection score')
    parser.add_argument(
        '--det-cat-id',
        type=int,
        default=0,
        help='the category id for human detection')
    parser.add_argument(
        '--pose-config',
        default=BASEPATH + r'\pose_estimation\td-hm_hrnet-w32_8xb64-210e_coco-256x192_infer.py',
        help='human pose estimation config file path (from mmpose)')
    parser.add_argument(
        '--pose-checkpoint',
        default=(BASEPATH + r'\pose_estimation\pose_hrnet_w32_coco_256x192-c78dce93_20200708.pth'),
        help='human pose estimation checkpoint file/url')
    parser.add_argument(
        '--device', type=str, default='cuda:0', help='CPU/CUDA device option')
    parser.add_argument(
        '--short-side',
        type=int,
        default=None,
        help='specify the short-side length of the image')
    parser.add_argument(
        '--cfg-options',
        nargs='+',
        action=DictAction,
        default={},
        help='override some settings in the used config, the key-value pair '
        'in xxx=yyy format will be merged into config file. For example, '
        "'--cfg-options model.backbone.depth=18 model.backbone.with_cp=True'")
    args = parser.parse_args()
    return args

def parse_args(config, checkpoint, label_map):
    parser = argparse.ArgumentParser(description='MMAction2 demo')
    parser.add_argument('--config', default=config, help='skeleton model config file path')
    parser.add_argument('--checkpoint', default=checkpoint, help='skeleton model checkpoint file/url')
    parser.add_argument('--label-map', default=label_map, help='label map file')
    args = parser.parse_args()
    return args


# def visualize(args, frames, data_samples, action_label):
#     pose_config = mmengine.Config.fromfile(args.pose_config)
#     visualizer = VISUALIZERS.build(pose_config.visualizer)
#     visualizer.set_dataset_meta(data_samples[0].dataset_meta)

#     vis_frames = []
#     print('Drawing skeleton for each frame')
#     for d, f in track_iter_progress(list(zip(data_samples, frames))):
#         f = mmcv.imconvert(f, 'bgr', 'rgb')
#         visualizer.add_datasample(
#             'result',
#             f,
#             data_sample=d,
#             draw_gt=False,
#             draw_heatmap=False,
#             draw_bbox=True,
#             show=False,
#             wait_time=0,
#             out_file=None,
#             kpt_thr=0.3)
#         vis_frame = visualizer.get_image()
#         cv2.putText(vis_frame, action_label, (10, 30), FONTFACE, FONTSCALE,
#                     FONTCOLOR, THICKNESS, LINETYPE)
#         vis_frames.append(vis_frame)

#     vid = mpy.ImageSequenceClip(vis_frames, fps=24)
#     vid.write_videofile(args.out_filename, remove_temp=True)

def divide_into_batches(input_list, batch_size, overlap_range):
    batches = [input_list[i:i+batch_size] for i in range(0, len(input_list) -len(input_list)%(batch_size-overlap_range), batch_size-overlap_range)]
    # if(len(batches[-1])<batch_size):
    #     batches.pop()
    return batches

def actionRecognition(video_file_path):
    #One time at first
    args = parse_args_default()
    
    config_file_path = BASEPATH + r'\action_recognition\stgcn_confg_flipping_fine_10fps.py'
    checkpoint_file_path = BASEPATH + r'\action_recognition\stgcn_100epoch_flipping_fine_10fps_30.pth'
    label_map_file_path = BASEPATH + r'\action_recognition\label_map.txt'
    args_gesture = parse_args(config = config_file_path, checkpoint = checkpoint_file_path, label_map = label_map_file_path)
    
    
    # video_file_path = r"F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\pipeling_split_MP4\10.mp4"
    # video_file_path = r"F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\gesture_video_dataset\A006\A006_11.mp4"
    # video_file_path = r"F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\dataset\gesture.mp4"
    

    tmp_dir = tempfile.TemporaryDirectory()
    frame_paths, frames = frame_extract(video_file_path, args.short_side,
                                        tmp_dir.name)
    print(len(frames))

    h, w, _ = frames[0].shape

    # Get Human detection results.
    det_results, _ = detection_inference(args.det_config, args.det_checkpoint,
                                         frame_paths, args.det_score_thr,
                                         args.det_cat_id, args.device)
    torch.cuda.empty_cache()
    


    # Get Pose estimation results.
    pose_results, pose_data_samples = pose_inference(args.pose_config,
                                                     args.pose_checkpoint,
                                                     frame_paths, det_results,
                                                     args.device)
    torch.cuda.empty_cache()
    
    # output_path = r"F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\pose_results.pkl"
    # make_dir(output_path)
    # with open(output_path, 'wb') as f:
    #     pickle.dump(pose_results, f)

    # print(pose_results)
    print(type(pose_results))
    batch_size= 30
    overlap_range = 20
    pose_batch_size = divide_into_batches(pose_results, batch_size, overlap_range)
    print(len(pose_batch_size))
    # print(pose_batch_size[0])
    # print(pose_batch_size[1])
    # print(pose_batch_size[2])

    config = mmengine.Config.fromfile(args_gesture.config)
    config.merge_from_dict(args.cfg_options)

    model = init_recognizer(config, args_gesture.checkpoint, args.device)
    log = []
    for i in range(len(pose_batch_size)):
        result = inference_skeleton(model, pose_batch_size[i], (h, w))
        pred_score = result.pred_score
        float_list = [float(x) for x in pred_score]
        max_pred_index = result.pred_score.argmax().item()
        # print(float_list[max_pred_index])
        # print(max_pred_index)
        index_score = float_list[max_pred_index]
        index_max_pred = max_pred_index
        # if(index_score<0.70):
        #     max_pred_index = 12
        label_map = [x.strip() for x in open(args_gesture.label_map, encoding='utf-8').readlines()]
        action_label = label_map[max_pred_index]
        
        # print(action_label)
        log_dict = {}
        # log_dict['index_score'] = index_score
        
        log_dict['total_frame'] = len(frames)
        log_dict['frame'] = i * (batch_size - overlap_range)
        log_dict['action_label'] = action_label
        # visualize(args, frames, pose_data_samples, action_label)
        log.append(log_dict)
        tmp_dir.cleanup()
    return log

def demo(MP4_path):
    log = actionRecognition(MP4_path)
    print(log)

if __name__ == '__main__':
    start_time = time.time()
    MP4_path = r'F:\2023_2\CapstoneProject\mmaction2\23_Capstone_Dataset\gesture.mp4'

    log = actionRecognition(MP4_path)
    
    end_time = time.time()
    elapsed_time  = end_time - start_time
    print("Action Recognition: " + str(elapsed_time))
    print(log)
