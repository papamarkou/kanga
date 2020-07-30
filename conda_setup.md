# Steps for setting up a conda environment for kanga

```
conda update conda

conda update --all

PYBIN="python"
PKGDIR="${HOME}/opt/python/packages"

conda create -n kanga python=3.6

conda activate kanga

conda install -c conda-forge numpy
conda install -c conda-forge scipy
conda install -c conda-forge arviz

conda install -c conda-forge matplotlib
conda install -c conda-forge seaborn

# conda install -c conda-forge spyder

cd ${PKGDIR}

git clone git@github.com:papamarkou/kanga.git
cd kanga

${PYBIN} setup.py develop --user
```
