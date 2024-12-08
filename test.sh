#! /bin/bash

###########
# TEST.SH #
###########

pip install -e .
pip list
clear
cd test
cd asm-test
python build.py
cd ..
cd c-test
python build.py