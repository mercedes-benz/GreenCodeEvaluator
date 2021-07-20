import numpy as np
import time 

# useless imports
import matplotlib
import os

def bad_search(data, element):
    print("start bad_search")
    for i in range(len(data)) :
        if data[i] == element :
            time.sleep(1)
            return i 
    return False 

def bad_max(data):
    print("start bad_max")
    maxi = data[0]
    for i in data:
        if data[i] > maxi :
            maxi = data[i]
    time.sleep(1)
    return maxi

if __name__ == "__main__":
    bad_search([i for i in range(10**7)], np.random.randint(2*10**9))
    time.sleep(1)
    bad_max([i for i in range(10**6)])
