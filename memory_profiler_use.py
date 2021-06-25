""" Goal of this blackbox code : 
Get as input a file path
Change this code with profile decorators
Launch this modified code with mprof 
Plot the memory usage (or read the generated data file)
"""
import os

# function to change the input code with descriptors
def add_descriptors(path) :
    new_path = file_path.rsplit('.', 1)[0]+"_with_descriptors.py"
    #input file
    fin = open(path, "rt")
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
    # can also be given by the front end interface for example
    file_path = '/home/romaissa/Documents/HerHackathon/GreenCodeEvaluator/empty_bad_functions.py'

    # get updated code file
    new_path = add_descriptors(file_path)

    #change directory 
    os.chdir(new_path.rsplit('/', 1)[0])

    # launch mprof commands
    os.system('mprof run '+new_path.rsplit('/', 1)[1])
    os.system('mprof plot')