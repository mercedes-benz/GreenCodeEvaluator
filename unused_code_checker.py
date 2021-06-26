""" Goal of this blackbox code :
1. Display unused imports, variables and functions from input code
2. Line-by-line memory usage
"""

import os

def add_profiler(file_path) :
    new_path = file_path.rsplit('.', 1)[0]+"_with_descriptors.py"
    fin = open(file_path, "r")
    fout = open(new_path, "w")

    for line in fin:
        fout.write(line.replace('def ', '@profile \ndef '))

    fin.close()
    fout.close()
    return new_path

if __name__ == "__main__":
    file_path = 'demo.py'

    # 1. Check unused imports, variables and functions (Used 'vulture' package)
    os.system('vulture ' + file_path)
    
    # 2 . Line-by-line memory usage
    new_path = add_profiler(file_path)
    os.system('python -m memory_profiler ' + new_path)
