import pickle
import os
import numpy as np


def deserialize(file_path):
    with open(file_path, 'rb') as f:
        pose = pickle.load(f)

    return pose


def find_files(folder_dir):
    files = []
    for file in os.listdir(folder_dir):
        if file.endswith(".pose"):
            files.append(os.path.join(folder_dir, file))

    return files


def convert_to_np_array(pose):
    new_pose = []
    for point in pose:
        new_pose.append([point['x'], point['y'], point['z'], point['visibility']])

    return np.array(new_pose)


# oops
def find_and_deserialize_and_convert(folder_dir):
    files = find_files(folder_dir)
    poses = []
    for file in files:
        poses.append(convert_to_np_array(deserialize(file)))

    return poses
