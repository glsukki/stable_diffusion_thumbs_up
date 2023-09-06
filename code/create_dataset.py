# # The below script performs resizing of the input images to a 

import os
import shutil
import to_jpeg
import pandas as pd
from PIL import Image
from tqdm import tqdm

files_to_ignore = ['.DS_Store']

def resize_images(current_image_directory='../data/', new_image_directory='../data/', trigger_keyword='suk'):
    
    if not os.path.exists(new_image_directory):
        os.makedirs(new_image_directory)

    original_images = os.listdir(current_image_directory)
    original_images = [img for img in original_images if img not in files_to_ignore]
    # print('\n'.join(original_images))
    # print(len(original_images))

    for i in tqdm(range(len(original_images)), desc='Image Resize Conversion: '):
        original_image = Image.open(f'{current_image_directory}{original_images[i]}')
        # original_image.show()
        # print(original_image.size)
        reshaped_image = original_image.resize((512, 512))
        reshaped_image.save(f'{new_image_directory}{original_images[i]}')
        # reshaped_image.show()
        # print(reshaped_image.size)

    df = pd.DataFrame({'file_name': original_images, 'text': trigger_keyword})
    df.to_csv(f'{new_image_directory}metadata.csv', index = False)    

## TODO: Create Datasets

# # Create 'thumbs_up' dataset
# Specify the directories
thumbs_up_image_directory = '../data/thumbs_up/'
thumbs_up_jpeg_directory = '../data/thumbs_up_jpeg/'
thumbs_up_resized_image_directory = '../data/thumbs_up_resized/'
thumbs_up_trigger_keyword = 'thumbs up'

# # Convert the list of HEIC images to JPEG
print('Begin JPEG Conversion for Thumbs Up images')
to_jpeg.convert_to_jpeg(thumbs_up_image_directory, thumbs_up_jpeg_directory)

# # resize all the thumbs_up images to 512 x 512 dimension for training on the runwayml/stable-diffusion-v1-5 model
print('Begin resizing Thumbs Up images')
resize_images(thumbs_up_jpeg_directory, thumbs_up_resized_image_directory, thumbs_up_trigger_keyword)

# # Create dataset for the person - 'sukruth'
# Specify the directories
sukruth_image_directory = '../data/sukruth/'
sukruth_jpeg_image_directory = '../data/sukruth_jpeg/'
sukruth_resized_image_directory = '../data/sukruth_resized/'
sukruth_trigger_keyword = 'sukruth'

# Convert the list of HEIC images to JPEG
print('Begin JPEG Conversion for sukruth images')
to_jpeg.convert_to_jpeg(sukruth_image_directory, sukruth_jpeg_image_directory)

# # resize all the images to 512x512 dimension
print('Begin resizing sukruth images')
resize_images(sukruth_jpeg_image_directory, sukruth_resized_image_directory, sukruth_trigger_keyword)


# # Create a directory to store all the images together + create a metadata.csv file
all_images_directory = '../data/ImageFolder/'

if not os.path.exists(all_images_directory):
    os.mkdir(all_images_directory)

shutil.copytree(sukruth_resized_image_directory, all_images_directory, dirs_exist_ok = True)
shutil.copytree(thumbs_up_resized_image_directory, all_images_directory, dirs_exist_ok = True)

thumbs_up_df = pd.read_csv(f'{thumbs_up_resized_image_directory}metadata.csv')
sukruth_df = pd.read_csv(f'{sukruth_resized_image_directory}metadata.csv')
all_images_info_df = pd.concat([thumbs_up_df, sukruth_df], axis = 0, ignore_index=True)
all_images_info_df.to_csv(f'{all_images_directory}/metadata.csv', index=False)