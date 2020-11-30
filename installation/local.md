## For installation on local machine for development, assuming that conda is available

```
PKGNAME='kanga'
PKGDIR="${HOME}/opt/python/packages"
PYBIN='python3'

conda update conda
conda update --all

conda create -n ${PKGNAME} python=3.8

conda activate ${PKGNAME}

conda install -c conda-forge numpy
conda install -c conda-forge scipy
conda install -c conda-forge statsmodels
conda install -c conda-forge matplotlib
conda install -c conda-forge seaborn

# conda install -c conda-forge spyder

cd ${PKGDIR}
git clone git@github.com:papamarkou/${PKGNAME}.git
cd ${PKGNAME}
${PYBIN} setup.py develop --user
```
