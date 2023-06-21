Image Color Detector and Social Distance Detector

This project consists of two Python scripts: Image Color Detector and Social Distance Detector. These scripts utilize computer vision techniques to perform specific tasks.

Image Color Detector

The Image Color Detector script analyzes an image and identifies the dominant colors present in the image. It uses the K-means clustering algorithm to group pixels with similar colors and determine the most representative colors.

Usage
To use the Image Color Detector, follow these steps:

Install the required dependencies: OpenCV, NumPy, and scikit-learn.
Run the image_color_detector.py script.
Provide the path to the image file when prompted.
The script will display the image and generate a color palette with the dominant colors detected.
Social Distance Detector

The Social Distance Detector script utilizes a pre-trained deep learning model to detect humans in a video stream or webcam feed and determines if social distancing guidelines are being violated.

Usage
To use the Social Distance Detector, follow these steps:

Install the required dependencies: OpenCV, NumPy, and scipy.
Download the pre-trained model files: deploy.prototxt and res10_300x300_ssd_iter_140000.caffemodel.
Place the model files in the same directory as the social_distance_detector.py script.
Run the social_distance_detector.py script.
The script will open the webcam feed and display the real-time social distance violations, if any.
Dependencies

OpenCV
NumPy
scikit-learn
scipy
Please ensure that the required dependencies are installed before running the scripts.

Disclaimer

The Social Distance Detector script is a basic implementation for educational purposes and should not be relied upon for critical applications. It is important to note that accurate social distancing detection requires more sophisticated systems and considerations.

License

Feel free to modify and adapt the scripts according to your needs.

Please refer to the individual scripts for more detailed information and usage instructions.

For any questions or issues, please create an issue in the repository or contact Vaishnavi at maknikarvaishnavi85@gmail.com.

