import numpy as np
import time 

# useless imports
import matplotlib
import os

def bad_search_10_power_2():
    print("start bad_search")
    data, element = [i for i in range(10**2)], np.random.randint(2*10**2)
    for i in range(len(data)) :
        if data[i] == element :
            time.sleep(1)
            return i 
    time.sleep(1)
    return False 

def bad_max_10_power_2():
    data = [i for i in range(10**2)]
    print("start bad_max")
    maxi = data[0]
    for i in data:
        if data[i] > maxi :
            maxi = data[i]
    time.sleep(1)
    return maxi

def bad_search_10_power_6():
    print("start bad_search")
    data, element = [i for i in range(10**6)], np.random.randint(2*10**6)
    for i in range(len(data)) :
        if data[i] == element :
            time.sleep(1)
            return i 
    time.sleep(1)
    return False 

def bad_max_10_power_6():
    data = [i for i in range(10**6)]
    print("start bad_max")
    maxi = data[0]
    for i in data:
        if data[i] > maxi :
            maxi = data[i]
    time.sleep(1)
    return maxi

def bad_search_10_power_7():
    print("start bad_search")
    data, element = [i for i in range(10**7)], np.random.randint(2*10**7)
    for i in range(len(data)) :
        if data[i] == element :
            time.sleep(1)
            return i
    time.sleep(1)
    return False 

def bad_max_10_power_7():
    data = [i for i in range(10**7)]
    print("start bad_max")
    maxi = data[0]
    for i in data:
        if data[i] > maxi :
            maxi = data[i]
    time.sleep(1)
    return maxi

if __name__ == "__main__":
    bad_search_10_power_2()
    time.sleep(1)
    bad_max_10_power_2()
    time.sleep(1)

    bad_search_10_power_6()
    time.sleep(1)
    bad_max_10_power_6()
    time.sleep(1)

    bad_search_10_power_7()
    time.sleep(1)
    bad_max_10_power_7()


