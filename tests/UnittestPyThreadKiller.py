import unittest
import time
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyThreadKiller import PyThreadKiller


class TestPyThreadKiller(unittest.TestCase):
    def test_thread_killer(self):
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
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
