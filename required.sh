#!/bin/bash

#create virtial environment
if [ ! -d ".venv" ]; then
    echo "Creating .venv..."
    python3 -m venv .venv
fi

#activate it
source .venv/bin/activate
echo "Activating .venv..."
#install required python libs
echo "installing packages..."
pip install -r requirements.txt

echo "deactivating..."
deactivate
