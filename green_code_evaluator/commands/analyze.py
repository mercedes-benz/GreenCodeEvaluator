import os
import click


# function to change the input code with descriptors
def add_descriptors(file_path) :
    new_path = file_path.rsplit('.', 1)[0]+"_with_descriptors.py"
    #input file
    fin = open(file_path, "rt")
    #output file to write the result to
    fout = open(new_path, "wt")

    #for each line in the input file
    for line in fin:
        fout.write(line.replace("def ", "@profile \ndef "))

    #close input and output files
    fin.close()
    fout.close()
    return new_path


@click.command(name="analyze", help="Analyzes some python code")
@click.argument("python_script_path", nargs=1)
def command(python_script_path: str):
    print(python_script_path)
    # get updated code file
    new_path = add_descriptors(python_script_path)

    # change directory
    os.chdir(new_path.rsplit('/', 1)[0])

    # launch mprof commands
    os.system('mprof run ' + new_path.rsplit('/', 1)[1])

    # launch cprof commands (cpu time profiling) sorted by time
    os.system('python -m cProfile -s time ' + python_script_path + "> " + new_path.rsplit('/', 1)[0] + "/cprof.txt")

    # print the first 10 lines using most CPU time
    print("----- First 10 most using CPU elements")
    with open(new_path.rsplit('/', 1)[0] + "/cprof.txt") as myfile:
        while not 'Ordered by' in next(myfile):
            pass
        for x in range(10):
            head = next(myfile)
            print(head)

    os.system('mprof plot')

    # remove file added
    os.system('rm mprofile*')
    os.system('rm ' + new_path)
    os.system('rm ' + new_path.rsplit('/', 1)[0] + "/cprof.txt")


if __name__ == "__main__":
    command()