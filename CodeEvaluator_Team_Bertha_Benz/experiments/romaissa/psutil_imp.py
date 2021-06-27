from time import sleep
import psutil

psutil.cpu_percent()

available_memory = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total

print('Memory percetage used:  ', available_memory)

sleep(1)
print('CPU percentage used: ', psutil.cpu_percent());

