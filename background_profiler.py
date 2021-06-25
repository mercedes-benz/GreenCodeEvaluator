import resource
from time import sleep
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import os


# some bad function that looks for an element in a list
# takes memory if the list is long (10**8 is limit for my machine)
def bad_search(data, element):
    for i in range(len(data)) :
        if data[i] == element :
            return i 
    return False 

# class to monitor the ram usage each 0.1 seconds
class MemoryMonitor:
    def __init__(self):
        self.keep_measuring = True

    def measure_usage(self):
        max_usage = 0
        while self.keep_measuring:
            max_usage = max(
                max_usage,
                resource.getrusage(resource.RUSAGE_SELF).ru_maxrss #Kb 
            )
            sleep(0.1)

        return max_usage

# function that will launch the file from a path given 
def run_file(file_path):
    # change to the dir where the file is
    os.chdir(file_path.rsplit('/', 1)[0])

    #launch the file
    os.system('python '+file_path.rsplit('/', 1)[1])


with ThreadPoolExecutor() as executor:
    monitor = MemoryMonitor()
    mem_thread = executor.submit(monitor.measure_usage)
    try:
        # fn_thread = executor.submit( bad_search, [i for i in range(10**7)], np.random.randint(2*10**7)) 
        fn_thread = executor.submit( run_file, '/home/romaissa/Documents/HerHackathon/sort/sort.py') 
        result = fn_thread.result()
    finally:
        monitor.keep_measuring = False
        max_usage = mem_thread.result()
        
    print(f"Peak memory usage: {max_usage}")