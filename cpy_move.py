import pathlib
import shutil
import os

path = "imgs_aug_json/"
for file in pathlib.Path("fuc/").glob("*.json"):
    print(file)
    file = str(file)
    file_name = file.split("/")[1].split(".")[0]
    print(file_name)
    new_file = file_name+"-BlackHat.json"
    # new_file = file_name+"-saturation.json"
    print(new_file)
    os.rename(file, "json_aug/"+new_file)