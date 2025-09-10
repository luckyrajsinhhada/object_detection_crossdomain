# Cross-Country Object Detection with YOLOv8

**Evaluating Cross-Domain Generalization of Object Detection Models in Autonomous Driving**

---

## 🔹 Project Overview
This project investigates how object detection models for autonomous driving generalize across countries. Models trained on one dataset may perform poorly when tested on a dataset from another country due to differences in traffic patterns, road infrastructure, and environmental conditions.

- **Training Dataset:** [KITTI](http://www.cvlibs.net/datasets/kitti/) (Germany)  
- **Testing Dataset:** [IDD](https://idd.insaan.iiit.ac.in/) (India)

---

## 🔹 Problem Statement
Autonomous vehicle perception systems often fail to generalize across regions. This project demonstrates how an object detection model trained in Germany performs on Indian driving data, highlighting challenges in cross-country deployment.

**Key Observation:**  
- KITTI → KITTI: **92% mAP@0.5**  
- KITTI → IDD: **12% mAP@0.5**  

The significant drop shows the **generalization gap** and the need for region-adaptive models in autonomous driving.

---

## 🔹 Approach & Methods
- Framework: **YOLOv8** (Ultralytics)
- Training:
  - Trained on KITTI dataset (bounding box annotations for vehicles, pedestrians, etc.)
  - Default YOLOv8 hyperparameters
- Testing:
  - Evaluated KITTI-trained model on IDD dataset to measure cross-domain performance
- Analysis:
  - Compared mAP@0.5 metrics between same-domain and cross-domain evaluation

---

## 🔹 Results
- KITTI → KITTI: **92% mAP@0.5** 
- KITTI → IDD: **12% mAP@0.5** 
- Demonstrates severe generalization issues for real-world deployment of autonomous vehicles.

**Sample Results:**  
![Sample Output](link_to_sample_image_or_gif)  

---

## 🔹 Insights & Takeaways
- Object detection models trained in one country do **not reliably generalize** to another country.  
- Highlights importance of **cross-domain adaptation**, data augmentation, and region-specific datasets for autonomous driving.

---

## 🔹 How to Run
```bash
# Clone the repo
git clone https://github.com/luckyrajsinhhada/object_detection_crossdomain.git
cd object_detection_crossdomain

# Install dependencies
pip install -r requirements.txt

# Train the model (optional)
python train.py --data kitti.yaml --weights yolov8n.pt

# Test on IDD dataset
python test.py --data idd.yaml --weights best.pt
