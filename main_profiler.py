""" Goal of this blackbox code : 
Get as input a file path
Change this code with profile decorators
Profile its CPU, GPU
Store useful results in a result/ subfolder (for front end)
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
    # file_path = '/home/romaissa/Documents/HerHackathon/GreenCodeEvaluator/python_code/Scrape_HackerNews.py'

    # get updated code file
    new_path = add_descriptors(file_path)

    # create directory for results
    result_path = new_path.rsplit('/', 1)[0]+"/result/"
    os.system("mkdir "+result_path)

    # 1. Check unused imports, variables and functions (Used 'vulture' package)
    print('vulture ' + file_path + " > "+result_path+"unused.txt")
    os.system('vulture ' + file_path + " > "+result_path+"unused.txt")

    # remove old mprofile and cprof results
    os.system('rm '+result_path+'mprofile*')
    os.system('rm '+result_path+"cprof.txt")

    #change directory 
    os.chdir(new_path.rsplit('/', 1)[0])

    # launch mprof commands
    os.system('mprof run '+new_path.rsplit('/', 1)[1])

    f = open(result_path+'cprof.txt', "x")
    # launch cprof commands (cpu time profiling) sorted by time 
    os.system('python -m cProfile -s time '+file_path+"> "+result_path+"cprof.txt")

    # print the first 10 lines using most CPU time
    print("----- First 10 most using CPU elements")
    with open(result_path+"cprof.txt") as myfile:
        while not 'Ordered by' in next(myfile):
            pass
        for x in range(10) : 
            head = next(myfile)
            print(head)

    os.system('mprof plot -o '+result_path+"/memory_usage.png")

    # remove file added, keep the profiles to front end 
    os.system('rm '+new_path)
    os.system('rm mprofile*')
