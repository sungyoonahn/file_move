import pathlib
import shutil


import json
# import OS
import glob
import pathlib

#convert json to pascalVOC format

#get information from jsonconda
def convert(path):

    with open(path,"r") as openfile:
        json_object = json.load(openfile)
    pole_path = path
    X = json_object["interface"]
    filename = X["filename"]
    path = X["path"]

    x = X["annotations"]
    # print(x)
    res = x[0]
    name = res["class_name"]
    name_list = name.split("/")
    # print(name_list[0])대
    if name_list[0] == "이동객체":
        print(pole_path)
        shutil.move(str(pole_path), "Annotation/images/move_test/이동객체/")
    else:
        if name_list[1] == "배전함":
            print(pole_path)
            shutil.move(str(pole_path), "Annotation/images/move_test/배전함/")
        elif name_list[1] == "가판대":
            print(pole_path)
            shutil.move(str(pole_path), "Annotation/images/move_test/가판대/")
        else:
            print(pole_path)
            shutil.move(str(pole_path), "Annotation/images/move_test/전봇대/")



for file in pathlib.Path("Annotation/images/json_test/").glob("*.json"):
    convert(file)
