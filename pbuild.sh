# THIS IS A WORK IN PROGRESS.
# I want to show alternate build process (pdebuild) but I need to tweak
# the setup. Look at build.sh for an actual working example.

sudo apt-get update
# these should be on the build box or on your base build image
sudo apt-get install -y build-essential debhelper devscripts equivs git-core pbuilder

# create a chroot environment (slow, need to improve)
sudo pbuilder create --distribution trusty --debootstrapopts --variant=buildd

# this (should) create a debian in a chroot environment but it
# breaks ATM.
sudo pdebuild --debbuildopts -b

