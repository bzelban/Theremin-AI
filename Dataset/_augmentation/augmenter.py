"""
    1- run "pip3 install imgaug"

    This Script will Augment the photos in the 
    sake of dataset variety
"""

import numpy as np
import os
import imgaug as ia
import imgaug.augmenters as iaa
import argparse

ia.seed(1)


images = np.array(
    [ia.quokka(size=(64, 64)) for _ in range(32)],
    dtype=np.uint8


    
)

sequence = iaa.Sequential([
    iaa.Sometimes(0.5,
        iaa.GaussianBlue(sigma=(0, 0.5)),
        iaa.LinearContrast(0.75, 1.5),
        iaa.Multiply((0.8, 1.2), per_channel=0.2),

    )
], random_order=True)

images_aug = sequence(images = images)
