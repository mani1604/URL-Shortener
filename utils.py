import json


def write_to_json(data_dict, out_file):
    with open(out_file, "w") as outfile:
        json.dump(data_dict, outfile)


def read_json(file_name):
    with open(file_name, "r") as f:
        data = json.load(f)

    return data
