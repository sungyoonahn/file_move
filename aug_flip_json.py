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

    X = json_object["interface"]
    id = X["id"]
    filename = X["filename"]
    path = X["path"]
    full_path = path+filename
    resolution = X["resolution"]
    gps_coord_xy = X["gps_coord_xy"]
    datetime = X["datetime"]
    width = str(X["resolution"][:1])[1:-1]
    height = str(X["resolution"][1:])[1:-1]
    x = X["annotations"]
    # print(x)
    res = x[0]
    name = res["class_name"]
    NAME = name
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
    bndbox = res["coord_xy"]
    # print(bndbox)
    # bndbox = bndbox.strip('][').split(', ')
    xmin = str(bndbox[0][0])
    xmax = str(bndbox[0][1])
    ymin = str(bndbox[1][0])
    ymax = str(bndbox[1][1])
    print(bndbox)
    print(xmin,xmax, ymin, ymax)
    flip_xmin = str(1000-int(xmin))
    flip_xmax = str(1000-int(xmax))
    print(flip_xmin, flip_xmax,ymin,ymax)
    new_json = {
        "interface": {
            "id": id,
        "filename": filename,
        "path": path,
        "resolution": resolution,
        "gps_coord_xy": [
            37.574127,
            127.035846
        ],
        "datetime": datetime,
        "annotations": [{
            "annotation_id": 2995538,
            "annotation_type": "bbox",
            "class_code": "0205000300000",
                        "class_name": NAME,
                        "coord_xy": [
                            [
                                int(flip_xmin),
                                int(flip_xmax)
                            ],
                            [
                                int(ymin),
                                int(ymax)
                            ]
                    ]
                }
            ]
        }
    }


    with open("json_aug/"+filename.split(".")[0] + "-flip"+".json", "w") as f:
        json.dump(new_json, f, indent=4,ensure_ascii = False)



for file in pathlib.Path("fuc/").glob("*.json"):
    convert(file)

