# 将labelme标注的json文件转为yolo格式
import glob
import json

import cv2
import tqdm

# 物体类别

class_list = ["zhi", "ke1", "ke2", "ke3", "ke0"]
# 关键点的顺序
keypoint_list = ["1", "2"]


def json_to_yolo(img_data, json_data):
    h, w = img_data.shape[:2]
    # 步骤：
    # 1. 找出所有的矩形，记录下矩形的坐标，以及对应group_id
    # 2. 遍历所有的head和tail，记下点的坐标，以及对应group_id，加入到对应的矩形中
    # 3. 转为yolo格式
    rectangles = {}
    # 遍历初始化
    for shape in json_data["shapes"]:
        label = shape["label"]  # pen, head, tail
        group_id = shape["group_id"]  # 0, 1, 2, ...'
        points = shape["points"]  # x,y coordinates
        shape_type = shape["shape_type"]

        # 只处理矩形,读矩形
        if shape_type == "rectangle":
            if group_id not in rectangles:
                rectangles[group_id] = {
                    "label": label,
                    "rect": points[0] + points[1],  # Rectangle [x1, y1, x2, y2]
                    "keypoints_list": []
                }
    # 遍历更新，将点加入对应group_id的矩形中，读关键点，根据group_id匹配
    for keypoint in keypoint_list:
        for shape in json_data["shapes"]:
            label = shape["label"]
            group_id = shape["group_id"]
            points = shape["points"]
            # 如果匹配到了对应的keypoint
            if label == keypoint:
                rectangles[group_id]["keypoints_list"].append(points[0])
            # else:
            #   rectangles[group_id]["keypoints_list"].append([0,0])

    # 转为yolo格式
    yolo_list = []
    for id, rectangle in rectangles.items():
        result_list = []
        if rectangle['label'] not in class_list:
            continue
        label_id = class_list.index(rectangle["label"])
        # x1,y1,x2,y2
        x1, y1, x2, y2 = rectangle["rect"]
        # center_x, center_y, width, height
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2
        width = abs(x1 - x2)
        height = abs(y1 - y2)
        # normalize
        center_x /= w
        center_y /= h
        width /= w
        height /= h

        # 保留6位小数
        center_x = round(center_x, 6)
        center_y = round(center_y, 6)
        width = round(width, 6)
        height = round(height, 6)

        # 添加 label_id, center_x, center_y, width, height
        result_list = [label_id, center_x, center_y, width, height]

        # 添加 p1_x, p1_y, p1_v, p2_x, p2_y, p2_v
        for point in rectangle["keypoints_list"]:
            x, y = point
            x, y = int(x), int(y)
            x /= w
            y /= h
            # 保留6位小数
            x = round(x, 6)
            y = round(y, 6)
            result_list.extend([x, y, 2])
        # if len(rectangle["keypoints_list"]) == 4:
        #     result_list.extend([0, 0, 0])
        #     result_list.extend([0, 0, 0])
        #     result_list.extend([0, 0, 0])
        #     result_list.extend([0, 0, 0])
        #     result_list.extend([0, 0, 0])
        #
        # if len(rectangle["keypoints_list"]) == 2:
        #     result_list.extend([0, 0, 0])
        #     result_list.extend([0, 0, 0])
        #     result_list.extend([0, 0, 0])
        #     result_list.extend([0, 0, 0])
        #     result_list.extend([0, 0, 0])
        #     result_list.extend([0, 0, 0])
        #     result_list.extend([0, 0, 0])

        yolo_list.append(result_list)
    return yolo_list


# 获取所有的图片
img_list = glob.glob("C:/Users/Justinc/Desktop/yolov5-v7.0/yolov5-v7.0/yolov8/utils/dataset/train/*.jpg")
for img_path in tqdm.tqdm(img_list):

    img = cv2.imread(img_path)
    print(img_path)
    json_file = img_path.replace('jpg', 'json')
    with open(json_file) as json_file:
        json_data = json.load(json_file)

    yolo_list = json_to_yolo(img, json_data)
    yolo_txt_path = img_path.replace('jpg', 'txt')

    with open(yolo_txt_path, "w") as f:
        for yolo in yolo_list:
            for i in range(len(yolo)):
                if i == 0:
                    f.write(str(yolo[i]))
                else:
                    f.write(" " + str(yolo[i]))
            f.write("\n")
