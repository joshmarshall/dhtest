# dh-virtualenv example

This is just a simple example python project that uses dh-virtualenv (https://github.com/spotify/dh-virtualenv) to build a release package. The code is purposefully silly (use an async web framework to fork a background process on every request!), but shows installing a project with both python dependencies from PyPI as well as system dependencies.

The main goal is to demonstrate that building a somewhat proper debian file is actually pretty simple.

## Demo

To see this work:

    $ vagrant up
    $ vagrant ssh
    $ cd /build/dhtest
    $ ./build.sh

You'll have a debian package (something like dhtest_2014.1005-ed046c3_amd64.deb) in the /build folder of the Vagrant box. You can test it by pulling it from the vagrant system and:

    $ vagrant destroy && vagrant up
    $ cd /vagrant
    $ sudo dpkg -i dhtest_2014.1005-ed046c3_amd64.deb
    $ sudo apt-get install -f

(The last line is because dpkg doesn't install dependencies by default. Alternatively you can use a tool like `gdebi` or push the deb file to a remote repo, but that's not in the scope of this example.)

## HowTo

Since the purpose of this is to show how a project is built using dh-virtualenv, it's worth describing the steps to build this. It really comes down to these simple steps:

* Build a proper python project.
* Set up your debian folder with a few required files.
* Follow a couple of at-build-time steps.

You can see all this in `build.sh`.

First, set up the project for packaging by:

* Having a proper setup.py and / or requirements.txt. (In other words, you can install with pip alone.)
* Creating a `debian/` folder in the project.
* Creating `debian/control`, `debian/rules`, and `debian/compat` files. (See below for more information on these.)

Then, each time you build you should:

* Set up a clean build environment (vagrant, chroot, Docker, cloud magic, etc)
* Install build dependencies: `build-essential python-dev dh-virtualenv` and any others you need that aren't project specific (`git-core` for example)
* Update / create the `debian/changelog` file (I've included a dumb git log parser in this example, but you can do this however you want.)
* `mk-build-deps` to install any build requirements in the `debian/control` file
* `dpkg-buildpackage -b` to get a binary deb file at the other end.

This works best in 14.04, since dh-virtualenv is available. If done properly, this should also be able to use alternative tools to dpkg-buildpackage, such as pdebuild, cowbuilder, alien, etc.

## Why

Doesn't Docker do everything for you? Why would you want to use old, dusty debs?

Docker is great. You should use Docker. If you don't want to use Docker, or need this in addition to Docker, you know why you need it. (Giant images, build tools installed in releases, efficient images are too onerous, Docker recursion for build + release, etc.) In fact, I've included a Dockerfile that can be used to build the project (although I question that for other reasons.)

If you meet the right criteria (you use Debian / Ubuntu, you want to keep your python projects "pure", and you want a toolchain that works across all your projects), I'm just demonstrating an alternative.
