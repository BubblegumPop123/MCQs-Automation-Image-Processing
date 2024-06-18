import cv2
import numpy as np
import matplotlib.pyplot as plt

def detect_filled_bubbles(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    num_questions = 5
    num_options = 4


    grid_height = gray.shape[0] // num_questions


    col_start_offset = int(gray.shape[1] * 0.15)
    option_width = (gray.shape[1] - col_start_offset) // num_options

    answers = [''] * num_questions

    for q in range(num_questions):
        min_intensity = 255
        answer_idx = -1

        for opt in range(num_options):
            row_start = q * grid_height
            row_end = (q + 1) * grid_height
            col_start = col_start_offset + opt * option_width
            col_end = col_start_offset + (opt + 1) * option_width
            option_region = gray[row_start:row_end, col_start:col_end]



            avg_intensity = np.mean(option_region)


            if avg_intensity < min_intensity:
                min_intensity = avg_intensity
                answer_idx = opt

        if answer_idx != -1:
            answers[q] = chr(65 + answer_idx)

    return answers


image_path = 'figure4.jpg'
answers = detect_filled_bubbles(image_path)
formatted_answers = ', '.join(f'{i+1}:{ans}' for i, ans in enumerate(answers))
print('Detected Answers:', formatted_answers)
