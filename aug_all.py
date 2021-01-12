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


def saturation_image(image,saturation,name):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    v = image[:, :, 2]
    v = np.where(v <= 255 - saturation, v + saturation, 255)
    image[:, :, 2] = v

    image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
    cv2.imwrite(Folder_name + name + "-saturation" + Extension, image)

def black_hat_image(image, shift,name):
    kernel = np.ones((shift, shift), np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)
    cv2.imwrite(Folder_name + name + "-Black_Hat" + Extension, image)



for file in pathlib.Path("imgs_train").glob("*.jpg"):
    file_name = str(file).split("/")[1].split(".")[0]
    image = cv2.imread(str(file))

    saturation_image(image,100,file_name)
    black_hat_image(image, 500,file_name)

    print(file)
