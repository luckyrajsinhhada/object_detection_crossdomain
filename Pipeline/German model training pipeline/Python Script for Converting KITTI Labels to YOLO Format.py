# Python Script for Converting KITTI Labels to YOLO Format

import os
class_mapping = {
"Car": 0,
"Van": 1,
"Truck": 2,
"Pedestrian": 3,
"person_sitting": 4
}
image_width = 1242
image_height = 375
def kitti_to_yolo(kitti_file, output_dir):
    with open(kitti_file, ’’) as file:
    lines = file.readlines()

    yolo_annotations = []
    for line in lines:
        parts = line.strip().split()
        if not parts:
            continue
            
    class_name = parts[0]
    if class_name not in class_mapping:
            continue
            
class_id = class_mapping[class_name]
x1, y1, x2, y2 = map(float, parts[4:8])
x_center = ((x1 + x2) / 2) / image_width
y_center = ((y1 + y2) / 2) / image_height
width = (x2 - x1) / image_width
height = (y2 - y1) / image_height

    yolo_annotations.append(f"{class_id}␣{x_center:.6f}␣{y_center:.6f}␣{width:.6f}␣{height
    :.6f}\n")

    base_name = os.path.basename(kitti_file)
    yolo_filename = os.path.join(output_dir, base_name)
    with open(yolo_filename, ’w’) as out_file:
        out_file.writelines(yolo_annotations)

kitti_files_dir = "/path/to/kitti_labels"
output_dir = "/path/to/output"
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(kitti_files_dir):
    if filename.endswith(".txt"):
        kitti_path = os.path.join(kitti_files_dir, filename)
        kitti_to_yolo(kitti_path, output_dir)