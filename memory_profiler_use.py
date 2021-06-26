""" Goal of this blackbox code : 
Get as input a file path
Change this code with profile decorators
Launch this modified code with mprof 
Plot the memory usage (or read the generated data file)
"""
import os
import platform
from jsonutils import cprotxt_to_json, terminal_out_to_json
from importresultutils import unused_out_to_json
# function to change the input code with descriptors
def add_descriptors(path) :
    # unused_out_to_json(r'result\unused.json')
    new_path = path.rsplit('.', 1)[0]+"_with_descriptors.py"
    #input file
    fin = open(new_path, "rt")
    #output file to write the result to
    fout = open(new_path, "wt")

    #for each line in the input file
    for line in fin:
        fout.write(line.replace('def ', '@profile \ndef '))

    #close input and output files
    fin.close()
    fout.close()
    return new_path

if __name__ == "__main__":
    cprotxt_to_json(r"D:\competitions\herhackathon\code\GreenCodeEvaluator\result\cprof.txt")
    # can also be given by the front end interface for example
    if platform.system() == "Windows":
        separator = '\\'
        delwith = 'del '
    else:
        separator = "/"
        delwith = 'rm '

    file_path = r'D:\competitions\herhackathon\code\GreenCodeEvaluator\empty_bad_functions.py'
    # file_path = '/home/romaissa/Documents/HerHackathon/GreenCodeEvaluator/python_code/Scrape_HackerNews.py'

    # get updated code file
    new_path = add_descriptors(file_path)

    #change directory 
    os.chdir(new_path.rsplit(separator, 1)[0])

    # launch mprof commands
    os.system('mprof run '+new_path.rsplit(separator, 1)[1])

    #convert terminal out to json
    # out = os.popen('mprof run '+new_path.rsplit('\\', 1)[1]).read()
    # terminal_out_to_json(out)

    # launch cprof commands (cpu time profiling) sorted by time 
    os.system('python -m cProfile -s time '+file_path+"> "+new_path.rsplit(separator, 1)[0]+"/cprof.txt")

    # print the first 10 lines using most CPU time
    print("----- First 10 most using CPU elements")
    with open(new_path.rsplit(separator, 1)[0]+separator+"cprof.txt") as myfile:
        while not 'Ordered by' in next(myfile):
            pass
        for x in range(10) : 
            head = next(myfile)
            print(head)

    os.system('mprof plot')

    # remove file added


    os.system(delwith + 'mprofile*')
    os.system(delwith+new_path)
    os.system(delwith+new_path.rsplit(separator, 1)[0]+separator+"cprof.txt")

    # cprotxt_to_json(r"GreenCodeEvaluator\result\cprof.txt")
