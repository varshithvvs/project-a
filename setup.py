'''Project Setup'''

import os
import sys
from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

#with open('LICENSE') as f:
#     license = f.read()



install_requires = ["wheel"]
install_requires = []

setup(
    name='project-a',
    version='0.0.1',
    author='Sai Varshith VV',
    author_email='svvarsham@gmail.com',
    description=
    'Project-a',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.7, !=3.9, != 3.10',
    packages=find_packages("src"),
    package_dir={"": "src"},   # tell distutils packages are under src
    install_requires=install_requires,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: Microsoft',
        'Intended Audience :: Developers'
    ],
    license='LGPLv3')