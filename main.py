import json

with open("list.json") as list:
    dictionary = json.load(list)

cat_item = []
selection = []
paths = []

#####
def get_keys(input_dict):
    for key, value in input_dict.items():
        if isinstance(value, dict):
            for subkey in get_keys(value):
                yield key + '->' + subkey
        elif isinstance(value, str):
            cat_item.append((key, value))
            yield value
        else:
            yield key

def lookup_path(value):
    for item in paths:
        if item[-1] == value:
            return item

def pop_path(value):
    paths.pop(paths.index(lookup_path(value)))

#####

for key in get_keys(dictionary):
    selection.append(key)

for item in selection:
    sp = item.split("->")
    paths.append(sp)








