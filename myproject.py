import cv2
import urllib3
import numpy as np
from gtts import gTTS
import subprocess

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save('announcement.mp3')
    subprocess.run(['start', 'announcement.mp3'], shell=True)

# Create an instance of the urllib3 PoolManager
http = urllib3.PoolManager()

# Download the image from the internet
image_url = 'https://cdn.pixabay.com/photo/2017/07/24/12/43/schrecksee-2534484_960_720.jpg'
response = http.request('GET', image_url)
arr = np.asarray(bytearray(response.data), dtype=np.uint8)
image = cv2.imdecode(arr, -1)

# Check if the image was loaded successfully
if image is None:
    print("Failed to load the image from the internet.")
    exit(1)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a blur filter to the image
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Perform edge detection
edges = cv2.Canny(blurred_image, 50, 150)

# Create a full-screen window for the original image
cv2.namedWindow('Original Image', cv2.WINDOW_FULLSCREEN)
cv2.imshow('Original Image', image)

# Create a full-screen window for the processed image
cv2.namedWindow('Processed Image', cv2.WINDOW_FULLSCREEN)
cv2.imshow('Processed Image', edges)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
