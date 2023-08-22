# Skin Color Detection with Python and OpenCV

This Python project utilizes OpenCV and NumPy to perform skin color detection in images or video streams. It identifies potential skin-colored regions within the specified color space thresholds.

## Project Overview

- **Objective**: Detect and highlight skin-colored regions in images or video.

- **Technologies Used**:
	- Python
	- OpenCV
	- NumPy

- **Key Features**:
	- Utilizes color space thresholds to identify skin-colored areas.
	- Demonstrates an understanding of image processing concepts.
  
## Getting Started

1. **Requirements**:
	- Python (3.6+)
	- OpenCV
	- NumPy

2. **Installation**:
   ```bash
   pip install opencv-python numpy```
   
3. **Adjustments**;
	- Modify the color space thresholds in the code to fine-tune skin color detection.
	- To use it with your own video, modify the following line in the code:
	```python
	cap = cv2.VideoCapture("test.mp4")```
	Replace "test.mp4" with the path to your video file. Alternatively, use 0 to access your camera.