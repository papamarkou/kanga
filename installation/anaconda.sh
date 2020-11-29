#!/bin/bash

# It is assumed that the package is built from platform linux-64

PLATFORMS=(osx-64 win-64)
PYVERSIONS=(3.6 3.7 3.8 3.9)
BUILDDIR="${HOME}/opt/continuum/miniconda/miniconda3/envs/eeyore/conda-bld"
PKGNAME='kanga'

echo 'Setting up skeleton...'

cd ${HOME}
conda skeleton pypi ${PKGNAME}

echo 'Building package for different Python versions...'

for v in "${PYVERSIONS[@]}"
do
	echo "  Building version ${v}..."
	conda-build --python ${v} -c conda-forge ${PKGNAME}
done

echo 'Converting package versions to different OS platforms...'

find ${BUILDDIR}/linux-64 -name *.tar.bz2 | while read file
do
    echo "  Converting ${file}..."
    for platform in "${PLATFORMS[@]}"
    do
			 echo "    Converting to ${platform} platform..."
       conda convert --platform ${platform} ${file} -o ${BUILDDIR}
    done
done

echo 'Uploading packages to anaconda...'

find $HOME/conda-bld/ -name *.tar.bz2 | while read file
do
    echo $file
    anaconda upload $file
done

echo 'Building conda package done'
