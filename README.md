# PyThreadKiller
A utility to manage and kill threads in Python applications.
* ***
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/kumarmuthu/PyThreadKiller)
![GitHub License](https://img.shields.io/github/license/kumarmuthu/PyThreadKiller?style=for-the-badge)
![GitHub Forks](https://img.shields.io/github/forks/kumarmuthu/PyThreadKiller?style=for-the-badge)
![GitHub Stars](https://img.shields.io/github/stars/kumarmuthu/PyThreadKiller?style=for-the-badge)
![GitHub Contributors](https://img.shields.io/github/contributors/kumarmuthu/PyThreadKiller?style=for-the-badge)


[![Build Status](https://github.com/kumarmuthu/PyThreadKiller/actions/workflows/python-app.yml/badge.svg)](https://github.com/kumarmuthu/PyThreadKiller/actions/workflows/python-app.yml)
[![codecov](https://codecov.io/github/kumarmuthu/PyThreadKiller/graph/badge.svg?token=FOKWM0LOX5)](https://codecov.io/github/kumarmuthu/PyThreadKiller)
[![PyPI Version](https://img.shields.io/pypi/v/PyThreadKiller?label=PyPI%20Version&color=brightgreen)](https://pypi.org/project/PyThreadKiller/)
[![Test PyPI Version](https://img.shields.io/badge/dynamic/json?color=blue&label=Test%20PyPI&query=info.version&url=https://test.pypi.org/pypi/PyThreadKiller/json&cacheSeconds=0)](https://test.pypi.org/project/PyThreadKiller/)


![GitHub Image](https://avatars.githubusercontent.com/u/53684606?v=4&s=40)

* **

## Overview

`PyThreadKiller` is a utility designed to manage and kill threads in Python applications. This package provides a simple and effective way to terminate threads safely and retrieve return values from target functions.

## Directory Structure
```
PyThreadKiller/
    ├── PyThreadKiller/
    │   ├── __init__.py
    │   ├── main.py
    ├── tests/
    │   ├── TestPyThreadKiller.py
    ├── CHANGELOG.md
    ├── README.md
    ├── requirements.txt
    ├── .github/
    │   └── workflows/
    │       └── python-app.yml
    └── setup.py
```

## Installation

You can install the package using pip:

```sh
pip install PyThreadKiller
```

# Usage
* Here is an example of how to use PyThreadKiller:
```
import time
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
```

### License:
* This project is licensed under the MIT License - see the LICENSE file for details.

* This updated `README.md` includes the new project name, badges, a brief overview, the directory structure, installation instructions, usage example, changelog, and the main code for the `PyThreadKiller` class. Make sure to adjust any URLs and links to point to the correct resources for your project.

