# # Pushes the dataset to the HuggingFace Hub

from datasets import load_dataset

dataset = load_dataset('imagefolder', data_dir='../data/ImageFolder', drop_labels = True)
dataset.push_to_hub('glsukki/thumbs_up_test_2')