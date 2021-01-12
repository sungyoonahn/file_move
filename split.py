import pathlib
import shutil

path = "imgs_train/"
file = open("xml_train.txt","r")
# print(file.read())
for a in file:
    # print("imgs/"+i+".jpg")
    b = a.rstrip('\n')
    imgs = "imgs"+'/'+b+'.jpg'
    print(imgs)
    shutil.copy(imgs, path)