#!/bin/bash

source env/bin/activate 
chmod 666 record.log
flask db init
flask db upgrade
python3 app.py
exit
