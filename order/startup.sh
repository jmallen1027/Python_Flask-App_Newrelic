#!/bin/bash

source env/bin/activate 

flask db init
flask db upgrade
python3 app.py
exit
