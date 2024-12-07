#! /bin/bash

###########
# TEST.SH #
###########

pip install -e .
pip list
cd test
python test.py