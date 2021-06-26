import os
import re

import click


# function to change the input code with descriptors
def add_descriptors(file_path: str):
    new_path = file_path.rsplit('.', 1)[0]+"_with_descriptors.py"
    # input file
    fin = open(file_path, "rt")
    # output file to write the result to
    fout = open(new_path, "wt")

    # for each line in the input file
    for line in fin:
        if re.match(r"\s", line):
            leading_spaces = len(line) - len(line.lstrip())
            fout.write(line.replace("def ", "@profile\n" + " " * leading_spaces + "def "))
        else:
            fout.write(line.replace("def ", "@profile\ndef "))

    # close input and output files
    fin.close()
    fout.close()
    return new_path


@click.command(name="analyze", help="Analyzes some python code")
@click.argument("input_path", nargs=1)
@click.argument("results_directory_path", nargs=1)
def command(input_path: str, results_directory_path: str):
    """

    Args:
        input_path: a folder or file path to be analyzed
        results_directory_path: directory where results are to be saved

    """
    if not os.path.exists(results_directory_path):
        os.makedirs(results_directory_path)

    if os.path.isfile(input_path):
        new_path = add_descriptors(input_path)

        # launch mprof commands
        os.system("mprof run " + new_path)

        # launch cprof commands (cpu time profiling) sorted by time
        os.system("python -m cProfile -s time " + input_path + "> " + os.path.join(results_directory_path, "cprof.txt"))

        # print the first 10 lines using most CPU time
        print("----- First 10 most using CPU elements")
        with open(os.path.join(results_directory_path, "cprof.txt")) as f_ref:
            while "Ordered by" not in next(f_ref):
                pass
            for x in range(10):
                head = next(f_ref)
                print(head)

        os.system('mprof plot')

        # remove file added
        os.system('rm mprofile*')
        os.system('rm ' + new_path)
        os.system('rm ' + new_path.rsplit('/', 1)[0] + "/cprof.txt")
    else:
        for root, dirs, files in os.walk(input_path):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    # get updated code file
                    new_path = add_descriptors(file_path)

                    # launch mprof commands
                    os.system("mprof run " + new_path)

                    # launch cprof commands (cpu time profiling) sorted by time
                    os.system("python -m cProfile -s time " + file_path + "> " + os.path.join(results_directory_path, "cprof.txt"))

                    # print the first 10 lines using most CPU time
                    print("----- First 10 most using CPU elements")
                    with open(os.path.join(results_directory_path, "cprof.txt")) as f_ref:
                        while "Ordered by" not in next(f_ref):
                            pass
                        for x in range(10):
                            head = next(f_ref)
                            print(head)

                    os.system('mprof plot')

                    # remove file added
                    os.system('rm mprofile*')
                    os.system('rm ' + new_path)
                    os.system('rm ' + new_path.rsplit('/', 1)[0] + "/cprof.txt")


if __name__ == "__main__":
    command()
