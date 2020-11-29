## Build, upload to and install from anaconda

### Install prerequisites
```
conda install conda-build
conda install conda-verify
```

### Build kanga using conda
```
anaconda login

cd $HOME
conda skeleton pypi kanga
conda build --python 3.6 -c conda-forge kanga
```

### Upload to anaconda
```
# anaconda upload $BUILTFILE
```

### Install from anaconda
```
conda install -c papamarkou kanga
```
