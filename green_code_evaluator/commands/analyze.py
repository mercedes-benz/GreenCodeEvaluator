import os
import re

import click
import psutil

from green_code_evaluator.util.json_utils import terminal_out_to_json, cprotxt_to_json, unused_out_to_json


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


def _analyze(input_path: str, results_directory_path: str):
    new_path = add_descriptors(input_path)

    # write CPU usage at the beginning
    cpu_file = open(os.path.join(results_directory_path, "cpu_usage.txt"), "a")

    # measure cpu at beginning
    cpu_beginning = psutil.cpu_percent(1.0)
    print(f"CPU percentage used at the beginning: {cpu_beginning}")
    cpu_file.write("CPU percentage used at the beginning : " + str(cpu_beginning) + '\n')

    # Check unused imports, variables and functions (Used 'vulture' package)
    os.system("vulture " + input_path + " > " + os.path.join(results_directory_path, "unused.txt"))
    unused_out_to_json(os.path.join(results_directory_path, "unused.txt"), results_directory_path)

    # launch mprof commands
    terminal_out = os.popen("mprof run " + new_path).read()
    terminal_out_to_json(terminal_out, results_directory_path)

    # launch cprof commands (cpu time profiling) sorted by time
    os.system("python -m cProfile -s time " + input_path + "> " + os.path.join(results_directory_path, "cprof.txt"))
    cprotxt_to_json(os.path.join(results_directory_path, "cprof.txt"), results_directory_path)

    os.system('mprof plot -o ' + os.path.join(results_directory_path, "memory_usage.png"))

    end_cpu = psutil.cpu_percent()
    print(f"CPU percentage used at the end: {end_cpu}")
    cpu_file.write("CPU percentage used at the end: " + str(end_cpu) + "\n")

    cpu_file.close()
    # remove file added
    os.system("rm mprofile*")
    os.system("rm " + new_path)
    print(os.path.join(results_directory_path, "cprof.txt"))
    os.system("rm " + os.path.join(results_directory_path, "cprof.txt"))
    os.system("rm " + os.path.join(results_directory_path, "unused.txt"))


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
        _analyze(input_path, results_directory_path)
    else:
        for root, dirs, files in os.walk(input_path):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    _analyze(file_path, results_directory_path)


if __name__ == "__main__":
    command()
