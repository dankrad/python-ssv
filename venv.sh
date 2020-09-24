#!/bin/bash
virtualenv venv -p `which python3`
. venv/bin/activate
pip install -r requirements.txt
pip install -r python_ibft/requirements.txt