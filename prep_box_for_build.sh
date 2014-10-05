#!/bin/bash

./parse_git_log.py > debian/changelog

sudo apt-get update
# these should be on the build box or on your base build image
sudo apt-get install -y build-essential debhelper devscripts equivs

sudo mk-build-deps -i -r -t "apt-get -y"

# doesn't have to be sudo if you checkout to an owned directory
sudo dpkg-buildpackage -b
