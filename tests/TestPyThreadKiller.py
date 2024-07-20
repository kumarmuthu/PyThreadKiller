__version__ = "2024.05.19.01"
__author__ = "Muthukumar Subramanian"

import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyThreadKiller import PyThreadKiller


def example_target():
    for i in range(5):
        print(f"Thread is running... {i}")
        time.sleep(1)
    return True


# Create an instance of PyThreadKiller
thread = PyThreadKiller(target=example_target)
thread.start()

# Allow the thread to run for 3 seconds
time.sleep(3)

# Kill the thread
result = thread.kill()
print(f"Return value after killing the thread: {result}")

# Output:
# Thread is running... 0
# Thread is running... 1
# Thread is running... 2
# Thread killed successfully
# Return value after killing the thread: None
