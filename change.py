import json

with open("datasets/obj/annotations/instances_objval.json","r") as openfile:
    json_object = json.load(openfile)

# Serializing json
json_object = json.dumps(json_object)

# Writing to sample.json
with open("instances_objval.json", "w") as outfile:
    outfile.write(json_object)


