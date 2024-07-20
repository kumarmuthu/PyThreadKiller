__version__ = "2024.05.19.01"
__author__ = "Muthukumar Subramanian"

'''
Thread Kill with return value - When we want to stop the target function's execution immediately without any condition
Scenario: 1. Join() with return value ==> target function's actual value
OUTPUT:
    Thread is running... 0
    Thread is running... 1
    Thread is running... 2
    Thread is running... 3
    Thread is running... 4
    Return count: 5

Scenario: 2. Kill() with return value ==> self._return = None
OUTPUT:
    Thread is running... 0
    Thread is running... 1
    Thread is running... 2
    Thread killed successfully
    get_count_after_kill: None

History:
2024.05.19.01 - Initial Draft
'''

import threading
import ctypes


class PyThreadKiller(threading.Thread):
    def __init__(self, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(target=target, name=name, args=args, kwargs=kwargs, daemon=daemon)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        super().join(*args)
        return self._return

    def start(self):
        super().start()

    def kill(self):
        """
        ..codeauthor:: Muthukumar Subramanian
        :param : None
        :return: Target function's return data
        """
        if not self.is_alive():
            return

        # Get the thread ID from the ident attribute
        thread_id = self.ident
        if thread_id is None:
            print("Thread ID is None")
            return

        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
            ctypes.c_long(thread_id), ctypes.py_object(SystemExit))

        if res == 0:
            print("Invalid thread ID")
        elif res > 1:
            # If it returns a number greater than 1, we must undo our action to prevent issues
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print("PyThreadState_SetAsyncExc failed")
        else:
            print("Thread killed successfully")
        return self._return
