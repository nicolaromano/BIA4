""" This file generates a reduced version of the ISIC2020 dataset 
    The original dataset can be found at https://challenge2020.isic-archive.com/
    Here we balance the original dataset, to have 584 images from benign skin lesions 
    and 584 from malignant. We also resize the images to 256x256 pixels (for performance 
    and to reduce file size).
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import resize
from tqdm import tqdm
from multiprocessing import Pool

# Change this to your path
basedir = '/run/media/nico/Sequencing/Kaggle/ISIC2020'
images = pd.read_csv(f'{basedir}/ISIC_2020_Training_GroundTruth_v2.csv')

print(images['benign_malignant'].value_counts())

malignant = images[images['benign_malignant'] == 'malignant']
# Fix random state to ensure reproducibility
benign = images[images['benign_malignant']
                == 'benign'].sample(584, random_state=32)

images_subset = benign.append(malignant)

images_subset.to_csv(f"{basedir}/ISIC2020_Small_metadata.csv", index=False)

print(images_subset['benign_malignant'].value_counts())

image_dir = '/run/media/nico/Sequencing/Kaggle/ISIC2020/ISIC_2020_Training_JPEG/train'
image_small_dir = '/run/media/nico/Sequencing/Kaggle/ISIC2020/ISIC2020_Small'

filenames = images_subset['image_name'].values


def resize_image(im):
    input_image = f'{image_dir}/{im}.jpg'
    output_image = f'{image_small_dir}/{im}.jpg'
    img = plt.imread(input_image)
    img = resize(img, (256, 256))
    plt.imsave(fname=output_image, arr=img)


if __name__ == '__main__':
    pool = Pool(4)
    pool.map(resize_image, filenames)
    pool.close()
    pool.join()
