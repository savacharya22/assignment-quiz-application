#!/bin/bash


# Check if Python is installed

(if ! command -v python3 &> /dev/null; then
    echo "Python is not installed. Please install Python 3 before running this script."
    exit 1
fi

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py)