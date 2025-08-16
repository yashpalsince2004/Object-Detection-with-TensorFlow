import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import cv2
import matplotlib.pyplot as plt

print("TensorFlow:", tf.__version__)

detector = hub.load("https://tfhub.dev/tensorflow/ssd_mobilenet_v2/2")
print("✅ Model loaded")

# Image ko load karo aur resize karo
image = cv2.imread("three2.jpg")  # apni image ka path do
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
input_tensor = tf.convert_to_tensor([image_rgb], dtype=tf.uint8)

plt.imshow(image_rgb)
plt.title("Input Image")
plt.axis(False)
plt.show()

result = detector(input_tensor)

result = {key: value.numpy() for key, value in result.items()}

print("Detected Classes:", result['detection_classes'][0])
print("Detection Scores:", result['detection_scores'][0])

image_with_boxes = image_rgb.copy()
h, w, _ = image_with_boxes.shape

for i in range(len(result['detection_scores'][0])):
    if result['detection_scores'][0][i] < 0.5:
        continue
    y1, x1, y2, x2 = result['detection_boxes'][0][i]
    start_point = (int(x1*w), int(y1*h))
    end_point = (int(x2*w), int(y2*h))
    cv2.rectangle(image_with_boxes, start_point, end_point, (0,255,0), 2)

plt.imshow(image_with_boxes)
plt.title("Detected Objects")
plt.axis(False)
plt.show()

