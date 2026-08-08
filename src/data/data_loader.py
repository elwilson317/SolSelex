import os
import random
import matplotlib.pyplot as plt
from PIL import Image

# Path to dataset
DATASET_PATH = "dataset"

# Get all class names
classes = sorted(
    [folder for folder in os.listdir(DATASET_PATH)
     if os.path.isdir(os.path.join(DATASET_PATH, folder))]
)

print("=" * 50)
print("EUROSAT DATASET")
print("=" * 50)

total_images = 0

for cls in classes:
    class_path = os.path.join(DATASET_PATH, cls)

    if os.path.isdir(class_path):
        count = len(os.listdir(class_path))
        total_images += count
        print(f"{cls:<25} {count} images")

print("\nTotal Images:", total_images)
print("Number of Classes:", len(classes))

# -----------------------------
# Display one sample image
# -----------------------------

plt.figure(figsize=(15, 8))

for i, cls in enumerate(classes):

    class_path = os.path.join(DATASET_PATH, cls)

    image_name = random.choice(os.listdir(class_path))

    image_path = os.path.join(class_path, image_name)

    image = Image.open(image_path)

    plt.subplot(2, 5, i + 1)
    plt.imshow(image)
    plt.title(cls)
    plt.axis("off")

plt.tight_layout()
plt.show()