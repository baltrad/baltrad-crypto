#!/bin/sh

set -x

PROJECT_ROOT=$(dirname $(dirname $(readlink -f $0)))

# First setup environment
sudo apt-get update
sudo apt-get -y install git rsync python3-sphinx python3-pycryptodome python3-daemon

git config --local user.email "baltrad@users.noreply.github.com"
git config --local user.name "Baltrad GitHub Action"

pip3 install "jprops == 2.0.2"

cd "$PROJECT_ROOT/doc"

make github
