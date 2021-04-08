import numpy as np
import cv2
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import json


def main():
    frame = cv2.imread("./inputs/median_frame.jpg", cv2.IMREAD_COLOR)
    frame_h, frame_w, _ = frame.shape
    print("width {} height {}".format(frame_w, frame_h))

    polygon_points = []
    polygon = []
    points = []
    cv2.imshow('Frame', frame)
    while True:
        cv2.setMouseCallback('Frame', left_click_detect, [points, frame])
        # Abort and exit with 'Q'
        key = cv2.waitKey(0)
        # press 'P' to finish drawing a polygon
        if (key == ord('q')):
            print('calculating matrices...')
            break
        # press 'Q' to finish drawing and calculate matrices
        elif (key == ord('p')):
            print(points)
            polygon = [np.int32(points)]
            frame = cv2.polylines(frame, polygon, True,
                                  (0, 255, 0), thickness=5)
            polygon_points.append(points)
            points = []
            cv2.imshow('Frame', frame)

    with open('polygon_points.txt', 'w') as outfile:
        json.dump(polygon_points, outfile)
    print("wrote polygoin_points.txt...")

    contains_lists = []
    for points in polygon_points:
        contains_list = []
        polygon = Polygon(points)
        for x in range(frame_w):
            for y in range(frame_h):
                if polygon.contains(Point(x, y)):
                    contains_list.append([x, y])
        contains_lists.append(contains_list)

    with open('contains_lists.txt', 'w') as outfile:
        json.dump(contains_lists, outfile)


def left_click_detect(event, x, y, flags, data):
    if (event == cv2.EVENT_LBUTTONDOWN):
        points, frame = data
        print(f"\tClick on {x}, {y}")
        points.append([x, y])
        cv2.circle(frame, (x, y), 4, (0, 255, 0), -1)
        cv2.imshow('Frame', frame)


if __name__ == "__main__":
    main()
