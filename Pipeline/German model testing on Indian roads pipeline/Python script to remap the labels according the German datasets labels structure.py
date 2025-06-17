# Python script to remap the labels according the German datasets labels structure

import os
input_dir = "/media/luh0419/Lucky_SSD/YOLO_Project/datasets/IDD/idd-detection/IDD_Detection/
dataset/train/labels"
output_dir = "/media/luh0419/Lucky_SSD/YOLO_Project/datasets/IDD/cross␣country/
labelsaccordingtogermanmodel"
os.makedirs(output_dir, exist_ok=True)
# Indian to German class mapping
# Format: indian_class_id : german_class_id
class_map = {
4: 0, # Car Car
13: 1, # Truck Truck
7: 2, # Person Pedestrian
8: 3 # Rider Cyclist
}
converted = 0
skipped = 0
for filename in os.listdir(input_dir):
if not filename.endswith(".txt"):
continue
input_path = os.path.join(input_dir, filename)
output_path = os.path.join(output_dir, filename)
with open(input_path, "r") as f_in, open(output_path, "w") as f_out:
for line in f_in:
parts = line.strip().split()
if len(parts) < 5:
continue
class_id = int(parts[0])
if class_id in class_map:
parts[0] = str(class_map[class_id])
f_out.write("␣".join(parts) + "\n")
converted += 1
else:
skipped += 1
print(f"Remapped␣and␣saved:␣{converted}␣labels")
print(f"Skipped␣(non-matching␣classes):␣{skipped}")