import numpy as np
import math


def get_angle(a, b, c):
    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(cosine_angle)

    return np.degrees(angle)


# angles of interest
# L body  - thigh: 11 23 25
# L thigh -   leg: 23 25 27
# L leg   -  foot: 25 27 31

# R body  - thigh: 12 24 26
# R thigh -   leg: 24 26 28
# R leg   -  foot: 26 28 32

def get_angles_of_interest(pose):
    angles = [
        get_angle(pose[11], pose[23], pose[25]),
        get_angle(pose[23], pose[25], pose[27]),
        get_angle(pose[25], pose[27], pose[31]),

        get_angle(pose[12], pose[24], pose[26]),
        get_angle(pose[24], pose[26], pose[28]),
        get_angle(pose[26], pose[28], pose[32])
    ]

    return angles
