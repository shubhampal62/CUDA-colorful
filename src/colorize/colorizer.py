import cv2
import tensorflow as tf
import numpy as np
import os

def load_image(image_path):
    return cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

def save_image(image, save_path):
    cv2.imwrite(save_path, image)

def colorize_image(image):
    # Here we use a pre-trained deep learning model for colorization.
    # This is a placeholder for the actual model loading and inference code.
    colorized_image = cv2.applyColorMap(image, cv2.COLORMAP_JET)
    return colorized_image

def main():
    input_folder = '../../data/textures/'
    output_folder = 'bin/'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = []
    for file in os.listdir(input_folder):
        if file.endswith('.tiff') or file.endswith('.png'):
            image_files.append(file)
    


    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        save_path = os.path.join(output_folder, os.path.splitext(image_file)[0] + '.png')

        print(f'Processing {image_path}...')
        image = load_image(image_path)
        colorized_image = colorize_image(image)
        save_image(colorized_image, save_path)
        print(f'Saved colorized image to {save_path}')

if __name__ == '__main__':
    main()
