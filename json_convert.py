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
    filename = X["filename"]
    path = X["path"]
    full_path = path+filename
    # print(full_path)
    width = str(X["resolution"][:1])[1:-1]
    height = str(X["resolution"][1:])[1:-1]
    x = X["annotations"]
    # print(x)
    res = x[0]
    name = res["class_name"]
    name_list = name.split("/")
    # print(name_list[0])
    if name_list[0] == "이동객체":
        name = "이동객"
    else:
        if name_list[1] == "배전함체":
            name = "배전함"
        elif name_list[1] == "가판대":
            name = "가판대"
        else:
            name = "전봇대"
    bndbox = res["coord_xy"]
    # print(bndbox)
    # bndbox = bndbox.strip('][').split(', ')
    xmin = str(bndbox[0][0])
    xmax = str(bndbox[0][1])
    ymin = str(bndbox[1][0])
    ymax = str(bndbox[1][1])


    #convert to xml format
    data = ET.Element("annotations")

    element1 = ET.SubElement(data,"folder")
    element1.text = 'images'
    element2 = ET.SubElement(data,"filename")
    element2.text = filename
    element3 = ET.SubElement(data,"path")
    element3.text = full_path

    element4 = ET.SubElement(data,"source")
    s_elem1 = ET.SubElement(element4,"database")
    s_elem1.text ="Unknown"

    element5 = ET.SubElement(data,"size")
    s_elem1 = ET.SubElement(element5,"width")
    s_elem1.text = width
    s_elem2 = ET.SubElement(element5,"height")
    s_elem2.text = height
    s_elem3 = ET.SubElement(element5,"depth")
    s_elem3.text = "3"

    element6 = ET.SubElement(data,"segmented")
    element6.text = "0"
    element7 = ET.SubElement(data,"object")
    s_elem1 = ET.SubElement(element7,"name")
    s_elem1.text = name
    s_elem2 = ET.SubElement(element7,"pose")
    s_elem2.text = "Unspecified"
    s_elem3 = ET.SubElement(element7,"truncated")
    s_elem3.text = "0"
    s_elem4 = ET.SubElement(element7,"difficult")
    s_elem4.text = "0"
    s_elem5 = ET.SubElement(element7,"bndbox")
    s_s_elem1 = ET.SubElement(s_elem5,"xmin")
    s_s_elem1.text = xmin
    s_s_elem2 = ET.SubElement(s_elem5,"ymin")
    s_s_elem2.text = ymin
    s_s_elem3 = ET.SubElement(s_elem5,"xmax")
    s_s_elem3.text = xmax
    s_s_elem4 = ET.SubElement(s_elem5,"ymax")
    s_s_elem4.text = ymax


    b_xml = ET.tostring(data)
    print(filename)
    with open("Annotation/images/xml_test/"+filename.split(".")[0]+".xml", "wb") as f:
        f.write(b_xml)


for file in pathlib.Path("Annotation/images/json_test/").glob("*.json"):
    convert(file)

