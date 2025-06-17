#  Python Script for Dataset Splitting(80/20)

import os
import random
import shutil
images_path = "path␣to␣the␣images␣folder␣to␣split"
labels_path = "path␣to␣the␣labels␣folder␣to␣split"
output_base = "desired␣output␣folder"
# Defining the output directories for training and validation
train_img_dir = os.path.join(output_base, "train", "images")
train_lbl_dir = os.path.join(output_base, "train", "labels")
val_img_dir = os.path.join(output_base, "val", "images")
val_lbl_dir = os.path.join(output_base, "val", "labels")
# output folders
for folder in [train_img_dir, train_lbl_dir, val_img_dir, val_lbl_dir]:
os.makedirs(folder, exist_ok=True)
all_images = sorted([f for f in os.listdir(images_path) if f.endswith(".png")])
random.shuffle(all_images)
split_index = int(0.8 * len(all_images))
train_images = all_images[:split_index]
val_images = all_images[split_index:]
def copy_files(image_list, image_dest, label_dest):
for image_file in image_list:
label_file = image_file.replace(".png", ".txt")
src_image = os.path.join(images_path, image_file)
src_label = os.path.join(labels_path, label_file)
if os.path.exists(src_label):
shutil.copy(src_image, image_dest)
shutil.copy(src_label, label_dest)
copy_files(train_images, train_img_dir, train_lbl_dir)
copy_files(val_images, val_img_dir, val_lbl_dir)
print(f"Split␣complete:␣{len(train_images)}␣training␣images,␣{len(val_images)}␣validation␣images
.")
print(f"Files␣saved␣to:␣{output_base}")