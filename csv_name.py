import csv
import pathlib

mylist = []


for file_name in pathlib.Path("2020-11-06/31/crop_image").glob("*.jpg"):

    file_name = str(file_name).split("/")[3].split("_")[0]
    mylist.append(file_name)
mylist = list(set(mylist))

for file_name in pathlib.Path("2020-11-06/13/crop_image").glob("*.jpg"):

    file_name = str(file_name).split("/")[3].split("_")[0]
    mylist.append(file_name)
mylist = list(set(mylist))


with open('list.csv', mode='w') as file:
    list_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for file_name in mylist:
        list_writer.writerow([file_name])
