import pathlib
import shutil


import json
# import OS
import glob
import pathlib
import xml.etree.ElementTree as ET

#convert json to pascalVOC format

#get information from jsonconda
def convert(path):

    with open(path,"r") as openfile:
        json_object = json.load(openfile)
    pole_path = path
    X = json_object["interface"]
    filename = X["filename"]
    path = X["path"]
    full_path = path+filename
    width = str(X["resolution"][:1])[1:-1]
    height = str(X["resolution"][1:])[1:-1]
    x = X["annotations"]
    # print(x)
    res = x[0]
    name = res["class_name"]
    name_list = name.split("/")
    # print(name_list[0])
    if name_list[0] == "이동객체":
        name = "Mobile_object"
    else:
        if name_list[1] == "배전함":
            name = "Distribution_box"
        elif name_list[1] == "가판대":
            name = "Stand"
        else:
            name = "Pole"
            print(pole_path)
            shutil.move(str(pole_path), "Annotation/images/pole_imgs/")



for file in pathlib.Path("Annotation/images/imgs/").glob("*.jpg"):
    convert(file)
