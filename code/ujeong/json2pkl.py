import json
import numpy as np
import pickle

def process_and_save_json(json_file_path, output_path, _frame_dir = 'sss', _label = 0 , num_frames=10, num_keypoints=17):
    # Load JSON file
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Process keypoints
    all_keypoints = []
    for annotation in data["annotation"]:
        keypoints = annotation["keypoints"]
        transformed_keypoints = [[float(x), float(y)] for x, y, _ in keypoints]
        transformed_keypoints.pop(5)
        
        all_keypoints.append(np.array(transformed_keypoints, dtype=np.float32))
        
    
    all_keypoints[:].pop(5)
    # print(all_keypoints[0])
    # print(np.array([all_keypoints], dtype=np.float32).shape)
    
    all_keypoints_array = np.array([all_keypoints], dtype=np.float32)

    # Add keypoint scores
    new_keypoint_scores = np.ones((1, num_frames, num_keypoints), dtype=np.float32)

    # Assign keypoints and remove unnecessary data
    data["keypoint"] = all_keypoints_array
    data["keypoint_score"] = new_keypoint_scores
    data["frame_dir"] = _frame_dir

    resolution = data["dataset"]["resolution"].split('x')
    data["img_shape"] = (int(resolution[1]), int(resolution[0]))
    data["original_shape"] = (int(resolution[1]), int(resolution[0]))
    
    duration = data["dataset"]["duration"]
    data["duration"] = float(duration)

    data.pop("class", None)
    data.pop("metadata", None)
    data.pop("dataset", None)
    data.pop("annotation", None)

    data["total_frames"] = num_frames
    data["label"] = _label

    # Save the modified data to a pickle file
    with open(output_path, 'wb') as f:
        pickle.dump(data, f)

    return data


if __name__ == '__main__':
# Example usage
    json_file_path = r"F:\2023_2\CapstoneProject\mmaction2\project\dataset\gesture_jpg_dataset\A001\json\A00_S01_F_C_01_029_01_MO_B01_1.json"
    output_path = r"F:\2023_2\CapstoneProject\mmaction2\project\dataset\test.pkl"
    loaded_data = process_and_save_json(json_file_path, output_path)
    # print(loaded_data)
