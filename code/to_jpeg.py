# # Converts image files to a uniform format: 'JPEG'

import os
from PIL import Image
from pillow_heif import register_heif_opener
from tqdm import tqdm


files_to_ignore = ['.DS_Store']

def convert_to_jpeg(current_image_directory='../data/', new_image_directory='../data/'):

    if not os.path.exists(new_image_directory):
        os.makedirs(new_image_directory)

    original_images = os.listdir(current_image_directory)
    original_images = [img for img in original_images if img not in files_to_ignore]

    for i in tqdm(range(len(original_images)), desc='JPEG Conversion'):
        register_heif_opener()
        current_image_name = original_images[i].split('.')[0]
        current_image = Image.open(f'{current_image_directory}{original_images[i]}')
        if current_image.mode == 'RGBA':
            current_image = current_image.convert('RGB')
            # print('after conversion: ', current_image.mode)
        current_image.save(f'{new_image_directory}{current_image_name}.jpeg', format = 'jpeg')

# # Specify the directories
# sukruth_directory = '../data/sukruth/'
# sukruth_jpeg_directory = '../data/sukruth_jpeg/'

# convert_to_jpeg(sukruth_directory, sukruth_jpeg_directory)
