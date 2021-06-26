import os
import json
def terminal_out_to_json(terminal_out, filepath_json=None):
    """

    :param out: # terminal output in a variable as--  out = os.popen('mprof run filepath').read()
    :return: filepath json
    """
    list_lines = terminal_out.split('\n')#getting outputs line by line
    out = dict(zip(range(len(list_lines)), list_lines))
    if filepath_json is None:
        filepath_json = 'result/terminalout.json'
    with open(filepath_json+'', 'w') as outfile:
        json.dump(out, outfile, indent=4)
    return filepath_json

def cprotxt_to_json(cprotxt_path, filepath_json=None):
    #gives result in  the form [{'ncalls':2, 'tottime':2.003..}, {'ncalls':2, 'tottime':2.004..}, ..]
    """

    :param cprotxt: cprofile txt output
    :param filepath_json: output file path
    :return:
    """

    if filepath_json is None:
        filepath_json = 'result/cprotxt.json'

    #input file
    fin = open(cprotxt_path, "rt")
    #output file to write the result to
    out_dict = []

    reached_header = False
    #for each line in the input file
    for line in fin:
        if 'ncalls' in line:
            reached_header = True
            header_list = line.split()
            continue
        if reached_header:
            vals = line.split()#each row values
            dictionary = dict(zip(header_list, vals))
            out_dict.append(dictionary)

    fin.close()
    with open(filepath_json, 'w') as fp:
        json.dump(out_dict, fp, sort_keys=True, indent=4)

    # for reading json
    # with open('data.json', 'r') as fp:
    #     data = json.load(fp)
    return filepath_json

def cpuusagetxt_json(cpupercenttxt, filepath_json=None):
    if filepath_json is None:
        filepath_json = 'result/cpu_usage.json'

    #input file
    fin = open(cpupercenttxt, "rt")

    #output file to write the result to
    out_dict = []

     #for each line in the input file
    for line in fin:
        out_dict.append({"detail":line.split(":")[0], "value":line.split(":")[1].replace("\n","")})

    fin.close()
    with open(filepath_json, 'w') as fp:
        json.dump(out_dict, fp, sort_keys=True, indent=4)

    return filepath_json

