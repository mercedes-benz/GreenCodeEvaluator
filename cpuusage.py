import yappi
import code_examples.simplefor as test
import os

yappi.set_clock_type("cpu") # Use set_clock_type("wall") for wall time
yappi.start()
# os.system("python "+r"code_examples\simplefor.py")
test.a()
yappi.stop()
yappi.get_func_stats().print_all()
yappi.get_thread_stats().print_all()
