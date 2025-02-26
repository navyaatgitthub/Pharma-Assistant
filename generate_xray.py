import cv2
import numpy as np

# Create a blank grayscale image (mimicking an X-ray)
xray_image = np.zeros((500, 500), dtype=np.uint8)

# Draw a simple structure that looks like a bone
cv2.rectangle(xray_image, (150, 100), (350, 400), 255, -1)

# Save the dummy X-ray image
cv2.imwrite("xray.jpg", xray_image)

print("✅ Dummy X-ray image 'xray.jpg' created successfully in the pharma-assistant folder.")
