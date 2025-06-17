#  Python script to remove the uncommon labels

import os
INDIAN_LABEL_DIR = # path 
OUTPUT_DIR = # path
KEEP_IDS = {2, 4, 7, 13}
os.makedirs(OUTPUT_DIR, exist_ok=True)
for fname in os.listdir(INDIAN_LABEL_DIR):
if not fname.endswith(".txt"):
continue
src_path = os.path.join(INDIAN_LABEL_DIR, fname)
dst_path = os.path.join(OUTPUT_DIR, fname)
with open(src_path, "r") as f:
lines = f.readlines()
filtered = []
for line in lines:
parts = line.strip().split()
if len(parts) == 0:
continue
try:
cls_id = int(parts[0])
except ValueError:
continue
Luckyrajsinh Hada Scientific Seminar
22
if cls_id in KEEP_IDS:
filtered.append(line)
with open(dst_path, "w") as out:
out.writelines(filtered)
print(f"Done.␣Filtered␣labels␣written␣to:\n␣␣␣␣{OUTPUT_DIR}")