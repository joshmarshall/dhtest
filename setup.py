#!/usr/bin/env python
from datetime import datetime
from setuptools import setup, find_packages
from subprocess import check_output

_LAST_TIME = check_output("git log --pretty=format:%ct -n 1", shell=True)
_LAST_HASH = check_output("git log --pretty=format:%h -n 1", shell=True)
_CURRENT_VERSION = datetime.fromtimestamp(
    int(_LAST_TIME)).strftime("%Y.%m%d") + "-" + _LAST_HASH

setup(
    name="dhtest",
    version=_CURRENT_VERSION,
    description="This is a test of the Tornado broadcasting system",
    author="Josh Marshall",
    author_email="catchjosh@gmail.com",
    packages=find_packages(),
    install_requires=["Pillow==2.6.0", "tornado==4.0.2"],
    scripts=["server.py"])
