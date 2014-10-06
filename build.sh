#!/bin/bash

sudo apt-get update
# these should be on the build box or on your base build image
sudo apt-get install -y build-essential debhelper devscripts equivs git-core

# the changelog can be generated every time - this script just
# extracts the last 100 lines from the git commit log
./parse_git_log.py > debian/changelog

# this line installs the build dependencies
sudo mk-build-deps -i -r -t "apt-get -y"

# dpkg-buildpackage will build the final .deb . It will place
# the file in ../ and should be run in a folder with the same
# name as the source / package name

# it doesn't have to be sudo if your build folder is in an
# owned directory
 sudo dpkg-buildpackage -b
