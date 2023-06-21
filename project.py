import cv2
import numpy as np
from sklearn.cluster import KMeans

def detect_colors(image_path, num_colors):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert the image from BGR to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Flatten the image to a 2D array of pixels
    pixels = image.reshape(-1, 3)
    
    # Apply K-means clustering to identify dominant colors
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)
    
    # Get the RGB values of the cluster centers
    colors = kmeans.cluster_centers_
    
    # Convert the RGB values to integers
    colors = colors.astype(int)
    
    return colors

# Example usage
image_path = 'path_to_your_image.jpg'
num_colors = 5
detected_colors = detect_colors(image_path, num_colors)

# Print the detected colors
for color in detected_colors:
    print(f"RGB: {color[0]}, {color[1]}, {color[2]}")
