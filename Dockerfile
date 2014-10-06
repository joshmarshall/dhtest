FROM ubuntu:trusty
RUN apt-get update && apt-get install -y build-essential debhelper devscripts equivs git-core curl

COPY ./ /build/dhtest/

WORKDIR /build/dhtest
RUN ./parse_git_log.py > debian/changelog
RUN mk-build-deps -i -r -t "apt-get -y"
RUN dpkg-buildpackage -b
