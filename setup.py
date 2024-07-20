"""
Setup file for the PyThreadkiller package.
"""

__version__ = "2024.05.19.01"
__author__ = "Muthukumar Subramanian"

import re
import os
from setuptools import setup, find_packages

# Paths to your README and change log files
readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
changelog_path = os.path.join(os.path.dirname(__file__), 'CHANGELOG.md')
requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')

# Read README file
with open(readme_path, encoding='UTF-8') as f:
    readme_content = f.read()

# Read CHANGELOG file
if os.path.exists(changelog_path):
    with open(changelog_path, encoding='UTF-8') as f:
        changelog_content = f.read()
else:
    changelog_content = ''

# Combine README and CHANGELOG content for the long description
long_description = readme_content + '\n\n' + changelog_content

# Read requirements file
requirements_file_list = []
if os.path.exists(requirements_path):
    with open(requirements_path, encoding='UTF-8') as f:
        requirements_file = f.read()
    requirements_file_list = [re.sub(r'(\w+)~.*', r'\1', i) for i in requirements_file.split('\n')]

setup(
    name='PyThreadKiller',
    version='3.0.2',
    description='A utility to manage and kill threads in Python applications',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Muthukumar Subramanian',
    url="https://github.com/kumarmuthu/PyThreadKiller/PyThreadKiller",
    author_email='kumarmuthuece5@gmail.com',
    install_requires=requirements_file_list,
    packages=find_packages('.'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.8',
    package_dir={'': '.'}
)
