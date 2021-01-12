import cv2
import pathlib
from skimage.exposure import rescale_intensity
from skimage.segmentation import slic
from skimage.util import img_as_float
from skimage import io
import numpy as np

Folder_name="imgs_aug/"
Extension=".jpg"
def flip_image(image,dir,name):
    image = cv2.flip(image, dir)
    cv2.imwrite(Folder_name + name + "-flip" + Extension, image)

for file in pathlib.Path("imgs_train").glob("*.jpg"):
    file_name = str(file).split("/")[1].split(".")[0]
    image = cv2.imread(str(file))
    flip_image(image, 1, file_name)  # vertical
    print(file)


