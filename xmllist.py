import pathlib
import random


file_list = []
for file in pathlib.Path("Annotation/images/xml/").glob("*.xml"):
    file_list.append(str(file))
    # list.write(str(file)+"\n")


# print(file_list)
random.shuffle(file_list)
print(len(file_list))
file_list_train = file_list[320:]
file_list = file_list[:320]
print(len(file_list))

list = open("xml_test.txt","a")

for file in file_list:
    path = str(file).split("/")
    path = path[3].split(".")
    list.write(path[0]+"\n")
    print(path[0]+"\n")


list_2 = open("xml_train.txt","a")
for file in file_list_train:
    path = str(file).split("/")
    path = path[3].split(".")
    list_2.write(path[0]+"\n")
    print(path[0]+"\n")