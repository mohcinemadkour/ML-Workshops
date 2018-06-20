# Classification-of-PubMed-documents-using-machine-learning
This project involves building a robust classifier that classifies whether a document (from abstract content) belongs to cancer class or not.

Dataset Description
The training as well as test data contains research papers abstract in .nxml format.
Training data contains two folders
1) Cancer :- Contains document related to cancer
2) Non Cancer: - Contains document not related to cancer. It contains document related to any category
apart from cancer, spanning from music, videos to HIV and stroke.
Test data contains 100 files with names ranging 1 to 100.nxml. Output should contain labels in below format.

# Prerequisition
```
pip install bs4
pip install html2text
pip install tqdm
pip install xml
pip install nltk
pip install numpy
pip install sklearn
```
# Install xgboost
```
git clone --recursive https://github.com/dmlc/xgboost
cd xgboost
make -j4
cd python-package
python setup.py install
```
## Error(import xgboost OSError:version `GOMP_4.0' not found)
```
conda install libgcc

```
# Links

https://github.com/dmlc/xgboost/issues/1786

