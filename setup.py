#!/usr/bin/env python

from distutils.core import setup

setup(
    name="dhtest",
    version="0.1.0a",
    description="This is a test of the Tornado broadcasting system",
    author="Josh Marshall",
    author_email="catchjosh@gmail.com",
    packages=["dhtest"],
    install_requires=["tornado"],
    scripts=["server.py"])
