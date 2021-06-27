import os
import re
import logging

import click
import psutil

from green_code_evaluator.util.json_utils import (
    terminal_out_to_json,
    cprotxt_to_json,
    unused_out_to_json,
    cpuusagetxt_json
)
from green_code_evaluator.util.cli import print_message

logging.basicConfig(level = logging.INFO)


# function to change the input code with descriptors
def add_descriptors(file_path: str):

    new_path = file_path.rsplit(".", 1)[0]+"_with_descriptors.py"
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


def _purge(dir: str, pattern: str):
    for f in os.listdir(dir):
        if re.search(pattern, f):
            os.remove(os.path.join(dir, f))


def _analyze(input_path: str, results_directory_path: str):
    new_path = add_descriptors(input_path)

    print_message(f"Starting analysis for {input_path}\n")
    # write CPU usage at the beginning

    # measure cpu at beginning
    cpu_beginning = psutil.cpu_percent(1.0)
    # print(f"CPU percentage used at the beginning: {cpu_beginning}")
    with open(os.path.join(results_directory_path, "cpu_usage.txt"), "w") as f_ref:
        f_ref.write("CPU percentage used at the beginning : " + str(cpu_beginning) + '\n')

    # Check unused imports, variables and functions (Used 'vulture' package)
    os.system("vulture " + input_path + " > " + os.path.join(results_directory_path, "unused.txt"))
    unused_out_to_json(os.path.join(results_directory_path, "unused.txt"), results_directory_path)

    # Line-by-line memory usage
    os.system("python -m memory_profiler " + new_path + " > " + os.path.join(results_directory_path, "mem_prof.txt"))

    # launch mprof commands
    terminal_out = os.popen("mprof run " + new_path).read()
    terminal_out_to_json(terminal_out, results_directory_path)

    # launch cprof commands (cpu time profiling) sorted by time
    os.system("python -m cProfile -s time " + input_path + "> " + os.path.join(results_directory_path, "cprof.txt"))
    cprotxt_to_json(os.path.join(results_directory_path, "cprof.txt"), results_directory_path)

    os.system("mprof plot -o " + os.path.join(results_directory_path, "memory_usage.png"))

    end_cpu = psutil.cpu_percent()
    # print(f"CPU percentage used at the end: {end_cpu}")
    with open(os.path.join(results_directory_path, "cpu_usage.txt"), "a") as f_ref:
        f_ref.write("CPU percentage used at the end: " + str(end_cpu) + "\n")
    cpuusagetxt_json(os.path.join(results_directory_path, "cpu_usage.txt"), results_directory_path)

    print_message(f"Finished analysis for {input_path}. Results are stored in {results_directory_path} ✨\n")
    # remove file added
    _purge(".", "mprofile*")
    os.remove(new_path)
    # print(os.path.join(results_directory_path, "cprof.txt"))
    os.remove(os.path.join(results_directory_path, "cprof.txt"))
    os.remove(os.path.join(results_directory_path, "unused.txt"))
    os.remove(os.path.join(results_directory_path, "cpu_usage.txt"))

    current_path = os.getcwd()

    frontend_path = os.path.dirname(results_directory_path)
    # shutil.move(os.path.join(results_directory_path, "memory_usage.png"), os.path.join(frontend_path, "src", "img"))
    os.chdir(frontend_path)
    os.system("npm install")
    os.chdir(current_path)
    os.system(f"npm start --prefix {frontend_path}")


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
        raise NotImplemented("The capability you're trying to use is not implemented.")


if __name__ == "__main__":
    command()
