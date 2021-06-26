import os
import json


def terminal_out_to_json(terminal_out: str, results_directory_path: str):
    """
    :param terminal_out: # terminal output in a variable as--  out = os.popen('mprof run filepath').read()
    :param results_directory_path: path where to store the json
    :return: filepath_json
    """
    list_lines = terminal_out.split("\n")  # getting outputs line by line
    out = dict(zip(range(len(list_lines)), list_lines))
    filepath_json = os.path.join(results_directory_path, "terminal_out.json")
    with open(filepath_json, "w") as outfile:
        json.dump(out, outfile, indent=4)
    return filepath_json


def cprotxt_to_json(cprotxt_path: str, results_directory_path: str):
    """
    Gives result in  the form [{'ncalls':2, 'tottime':2.003..}, {'ncalls':2, 'tottime':2.004..}, ..]
    :param cprotxt_path: cprofile txt output
    :param results_directory_path: path to where to store the json
    :return: filepath_json
    """

    filepath_json = os.path.join(results_directory_path, "cprotxt.json")

    # input file
    fin = open(cprotxt_path, "rt")
    # output file to write the result to
    out_dict = []

    reached_header = False
    # for each line in the input file
    for line in fin:
        if "ncalls" in line:
            reached_header = True
            header_list = line.split()
            continue
        if reached_header:
            vals = line.split()  # each row values
            dictionary = dict(zip(header_list, vals))
            out_dict.append(dictionary)

    fin.close()
    with open(filepath_json, "w") as fp:
        json.dump(out_dict, fp, sort_keys=True, indent=4)

    return filepath_json


def unused_out_to_json(txt_path: str, results_directory_path: str):
    """
    :param txt_path: filepath of unusedimport output text file
    :param results_directory_path: path where to store the json
    :return: filepath_json
    """

    filepath_json = os.path.join(results_directory_path, "unused.json")

    # input file
    fin = open(txt_path, "rt")

    # output file to write the result to
    out_dict = {
        "unused_import": []
    }

    reached_header = False
    # for each line in the input file
    for line in fin:
        name = line.split("import")[-1]  # each row values
        name = name.replace("'", "")
        name = name.replace("\n", "")
        out_dict["unused_import"].append(name)

    fin.close()
    with open(filepath_json, "w") as fp:
        json.dump(out_dict, fp, sort_keys=True, indent=4)

    return filepath_json
