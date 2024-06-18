### Project Description and Guide

---

# Automated OMR (Optical Mark Recognition) for Multiple Choice Answer Sheets

## Project Description

This project focuses on automating the marking process for multiple-choice answer sheets using image processing techniques. The provided image shows an answer sheet with multiple questions, each having four possible answers. The system processes the image to detect which bubble is filled for each question, and outputs the detected answers.

This system can be useful in educational institutions for grading exams, surveys, or any scenario where multiple-choice answers are used. The project leverages Python libraries such as OpenCV and NumPy to achieve accurate detection of filled bubbles.

## Features

- **Grayscale Conversion**: Converts the input image to grayscale for easier processing.
- **Grid Segmentation**: Divides the image into a grid based on the number of questions and options.
- **Bubble Detection**: Identifies the filled bubble by analyzing the average intensity of each region.
- **Answer Extraction**: Extracts and outputs the detected answers in a formatted manner.

### Important Notes

- The code currently has hardcoded values for the number of questions and options, as well as specific offsets and grid dimensions based on the provided input image. These values can be adjusted to fit different input images.
- The edge of the image and division calculations are based on the specific layout of the provided image and should be modified if the layout changes.

---

## Guide

### 1. Setup

#### Prerequisites

Ensure you have Python 3.x installed along with the necessary libraries: OpenCV, NumPy, and Matplotlib.

#### Installation

Install the required libraries using pip:

```bash
pip install opencv-python numpy matplotlib
```

### 2. Image Processing and Answer Detection

The following steps describe the process of detecting filled bubbles in the answer sheet and extracting the answers:

1. **Load the Image**: Use OpenCV to load the answer sheet image.
2. **Convert to Grayscale**: Convert the loaded image to grayscale for easier processing.
3. **Segment the Grid**: Divide the image into a grid based on the number of questions and options. This involves calculating the height of each question row and the width of each option column.
4. **Detect Filled Bubbles**: For each question, analyze the intensity of each option region. The region with the lowest average intensity (darkest area) is considered the filled bubble.
5. **Extract Answers**: Map the detected filled bubbles to their corresponding answers (A, B, C, D) and output the results.

### 3. Running the Code

The code processes the provided image, detects the filled bubbles for each question, and prints the detected answers in a formatted manner. The hardcoded values for grid segmentation and offsets are based on the specific layout of the provided image and should be adjusted for different layouts.

### Example Output

For the provided image, the output will be in the format:

```
Detected Answers: 1:A, 2:B, 3:D, 4:A, 5:D
```

---

By following this guide, you can set up, run, and evaluate the automated OMR system for multiple-choice answer sheets. This system is applicable in various scenarios such as educational assessments and surveys, where quick and accurate grading is essential. Adjust the hardcoded values as necessary to fit different input image layouts.
