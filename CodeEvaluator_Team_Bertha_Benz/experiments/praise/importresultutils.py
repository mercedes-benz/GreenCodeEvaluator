import json

def unused_out_to_json(txt_path, filepath_json=None):
    """

    :param txt_path: filepath of unusedimport output text file
    filepath_json: output filepath
    :return:
    """

    if filepath_json is None:
        filepath_json = '../romaissa/result/unused.json'

    #input file
    fin = open(txt_path, "rt")

    #output file to write the result to
    out_dict = {"unused_import": []}

    reached_header = False
    #for each line in the input file
    for line in fin:
        name = line.split("import")[-1]#each row values
        name = name.replace("'", "")
        name = name.replace("\n", "")
        out_dict["unused_import"].append(name)

    fin.close()
    with open(filepath_json, 'w') as fp:
        json.dump(out_dict, fp, sort_keys=True, indent=4)

    return filepath_json
