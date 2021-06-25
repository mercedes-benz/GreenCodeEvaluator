""" Goal of this blackbox code :
1. Display unused imports, variables and functions from input code
2. Display duplicated variables
3. Determine algorithmic complexity of input code
4. Code section with high energy cost (CPU and RAM usage)
"""
import os

if __name__ == "__main__":
    file_path = 'demo.py'

    # 1. Check unused imports, variables and functions (Used 'vulture' package)
    os.system('vulture ' + file_path)