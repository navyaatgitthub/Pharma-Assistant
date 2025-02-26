import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# Folder Path (Modify as per your dataset location)
dataset_path = "COVID-19_Radiography_Dataset/COVID/images"
image_files = sorted(os.listdir(dataset_path))

# Function to apply image processing
def process_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    edges = cv2.Canny(gray, 50, 150)  # Apply edge detection
    equalized = cv2.equalizeHist(gray)  # Apply histogram equalization
    return gray, edges, equalized

# Display images with processing
index = 0

while index < len(image_files):
    img_file = image_files[index]
    img_path = os.path.join(dataset_path, img_file)
    img = cv2.imread(img_path)

    if img is None:
        print(f"Warning: Image not found at {img_path}")
        index += 1
        continue

    gray, edges, equalized = process_image(img)

    # Display original and processed images
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 4, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original")

    plt.subplot(1, 4, 2)
    plt.imshow(gray, cmap="gray")
    plt.title("Grayscale")

    plt.subplot(1, 4, 3)
    plt.imshow(edges, cmap="gray")
    plt.title("Edge Detection")

    plt.subplot(1, 4, 4)
    plt.imshow(equalized, cmap="gray")
    plt.title("Equalized")

    plt.show(block=False)

    key = input("\n➡ Press Right Arrow for Next, Left Arrow for Previous, 'q' to Exit: ")

    plt.close()  # Close the figure before moving to the next one

    if key == "\x1b[C":  # Right Arrow Key
        index += 1
    elif key == "\x1b[D" and index > 0:  # Left Arrow Key
        index -= 1
    elif key.lower() == 'q':  # Quit if 'q' is pressed
        break
