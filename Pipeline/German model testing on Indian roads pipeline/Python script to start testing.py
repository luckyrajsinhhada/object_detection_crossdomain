#  Python script to start testing

from ultralytics import YOLO
if __name__ == "__main__":
# Path to the German model
german_model_path = "/media/luh0419/Lucky_SSD/YOLO_Project/runs/detect/train6/weights/best.
pt"
# YAML file describing the Indian dataset
indian_dataset_yaml = "/media/luh0419/Lucky_SSD/YOLO_Project/datasets/IDD/cross␣country/
fileforcrosscountrytesting.yaml"
image_size = 416
compute_device = 0
output_directory = "/media/luh0419/Lucky_SSD/YOLO_Project/datasets/IDD/cross␣country/
resultfromcc"
run_name = "german_model_on_indian_data"
model = YOLO(german_model_path)
results = model.val(
data=indian_dataset_yaml,
imgsz=image_size,
device=compute_device,
project=output_directory,
name=run_name
)
print("\nValidation␣completed.␣Summary:")
print(results)
