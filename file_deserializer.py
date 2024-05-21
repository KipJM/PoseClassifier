import pickle
import os
import numpy as np
import pandas as pd

import preprocess


def deserialize(file_path):
    with open(file_path, 'rb') as f:
        pose = pickle.load(f)

    return pose


def find_files(folder_dir):
    files = []
    for file in os.listdir(folder_dir):
        if file.endswith(".pose"):
            print(f"FOUND FILE: {os.path.join(folder_dir, file)}")
            files.append(os.path.join(folder_dir, file))

    return files


def convert_to_df(pose):
    new_pose = []
    for point in pose:
        new_pose.append([point['x'], point['y'], point['z'], point['visibility']])

    return pd.DataFrame(new_pose)


# oops
def find_deserialize_preprocess(folder_dir):
    files = find_files(folder_dir)
    poses = []
    for file in files:
        poses.append(preprocess.preprocess(convert_to_df(deserialize(file))))

    return poses
