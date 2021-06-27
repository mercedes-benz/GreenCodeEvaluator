import time
from time import sleep
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import os
from guppy import hpy


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
        guppy_max = 0
        # initialise the heap here is okay ???
        h = hpy()
        while self.keep_measuring:
            guppy_max = max(h.heap().size, guppy_max)
            sleep(0.1)

        return guppy_max

# function that will launch the file from a path given 
def run_file(file_path):
    # check for py in front end
    # change to the dir where the file is
    os.chdir(file_path.rsplit('/', 1)[0])

    #launch the file
    os.system('python '+file_path.rsplit('/', 1)[1])


with ThreadPoolExecutor() as executor:
    monitor = MemoryMonitor()
    mem_thread = executor.submit(monitor.measure_usage)   
    t0 = time.time() 
    try:
        fn_thread = executor.submit( bad_search, [i for i in range(10**2)], np.random.randint(2*10**9)) 
        # fn_thread = executor.submit( run_file, '/home/romaissa/Documents/HerHackathon/sort/sort.py') 
        result = fn_thread.result()
    finally:
        monitor.keep_measuring = False
        guppy_max = mem_thread.result()
    t1 = time.time() - t0
    print("Time elapsed: %s seconds"%t1) # CPU seconds elapsed (floating point)
    print('Peak Memory usage: %s (Bytes) according to guppy'%str(guppy_max))

