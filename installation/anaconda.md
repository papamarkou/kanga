## Build, upload to and install from anaconda

### Install prerequisites
```
conda install conda-build
conda install conda-verify
conda install anaconda-client
```

### Add conda-forge channel and login to anaconda
```
# Add conda-forge channel
# This is necessary for the installation not to fail
# See https://github.com/conda/conda-build/issues/3779
conda config --add channels conda-forge

# Login to anaconda, needed for uploading built packages
anaconda login
```

### Build kanga using conda
```
cd $HOME
conda skeleton pypi kanga
conda build --python 3.6 kanga
```

### Upload to anaconda
```
# anaconda upload $BUILTPKG
```

### Install from anaconda
```
conda install -c papamarkou kanga
```
