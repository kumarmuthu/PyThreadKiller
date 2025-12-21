"""
Setup file for the PyThreadkiller package.
"""

__version__ = "3.0.8"
__author__ = "Muthukumar Subramanian"

import os
from setuptools import setup, find_packages

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Read README
with open(os.path.join(BASE_DIR, "README.md"), encoding="utf-8") as f:
    readme_content = f.read()

# Read CHANGELOG
changelog_path = os.path.join(BASE_DIR, "CHANGELOG.md")
if os.path.exists(changelog_path):
    with open(changelog_path, encoding="utf-8") as f:
        changelog_content = f.read()
else:
    changelog_content = ""

long_description = readme_content + "\n\n" + changelog_content

setup(
    name="pythreadkiller",
    version=__version__,
    description="A utility to manage and kill threads in Python applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=__author__,
    author_email="kumarmuthuece5@gmail.com",
    url="https://github.com/kumarmuthu/PyThreadKiller",
    project_urls={
        "Homepage": "https://github.com/kumarmuthu/PyThreadKiller",
        "Source": "https://github.com/kumarmuthu/PyThreadKiller",
        "Tracker": "https://github.com/kumarmuthu/PyThreadKiller/issues"
    },
    packages=find_packages(),
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
