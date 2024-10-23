#!/bin/bash

echo "#################################################"
echo "Script Started at: "
date
echo "#################################################"

source ../venv/bin/activate
pip install --upgrade pip wheel
pip install --upgrade setuptools
pip install -r freeze/2024-05-14.txt
python -m manage collectstatic --noinput

echo "#################################################"
echo "Script Finished at: "
date
echo "#################################################"