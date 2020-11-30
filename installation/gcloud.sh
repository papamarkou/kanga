#!/bin/bash

# Start up script for setting up environment from scratch on Ubuntu 20.04 LTS

export SHELL='bash'

export DOWNLOADDIR="$HOME/downloads"
export CONDADIR="$HOME/opt/continuum/miniconda/miniconda3"

export CONDABIN="$CONDADIR/bin/conda"

export CONDASCRIPT='Miniconda3-latest-Linux-x86_64.sh'
export CONDAENV='kanga'

sudo apt-get update

sudo apt-get install tree

mkdir $DOWNLOADDIR; cd $DOWNLOADDIR
wget https://repo.anaconda.com/miniconda/$CONDASCRIPT
chmod u+x $CONDASCRIPT

$SHELL $CONDASCRIPT -b -p $CONDADIR

$CONDABIN init $SHELL
source $HOME/.bashrc
$CONDABIN deactivate base

$CONDABIN create -n $CONDAENV -y -c papamarkou -c conda-forge python=3.8 kanga
