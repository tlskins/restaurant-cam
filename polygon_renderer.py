import numpy as np
import cv2
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import json


def main():
    frame = cv2.imread("./inputs/median_frame.jpg", cv2.IMREAD_COLOR)
    frame_h, frame_w, _ = frame.shape
    print("width {} height {}".format(frame_w, frame_h))
    cv2.imshow('Frame', frame)

    points_file = open('polygon_points.txt', "r")
    points_lists = json.loads(points_file.read())
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

    for i, points in enumerate(points_lists):
        polygon = [np.int32(points)]
        color = colors[i % 3]
        frame = cv2.polylines(frame, polygon, True,
                              color, thickness=5)
        cv2.imshow('Frame', frame)

    cv2.waitKey(0)


if __name__ == "__main__":
    main()
