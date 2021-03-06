#!/bin/bash

# Start up script for setting up environment on Ubuntu 20.04 LTS

export PKGNAME='kanga'
export PYVERSION='3.7'
export CONDADIR="$HOME/opt/continuum/miniconda/miniconda3"
export CONDABIN="$CONDADIR/bin/conda"
export CONDASCRIPT='Miniconda3-latest-Linux-x86_64.sh'

sudo apt-get update

sudo apt-get install tree

wget https://repo.anaconda.com/miniconda/$CONDASCRIPT
chmod u+x $CONDASCRIPT

$SHELL $CONDASCRIPT -b -p $CONDADIR

$CONDABIN create -n $PKGNAME -y -c papamarkou -c conda-forge python=$PYVERSION $PKGNAME

$CONDABIN init $(basename $SHELL)
$CONDABIN config --set auto_activate_base false

rm $HOME/$CONDASCRIPT
