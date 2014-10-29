#!/bin/sh

pip install -r requirements.txt
autopep8 -ir .
flake8 --max-complexity=3 --exclude=*.txt,*.md --max-line-length=200 .
lettuce AceptanceTest
cd UnitTest
python -m unittest TestFiguras TestFiguras2
coverage run --branch TestFiguras.py
coverage report -m
coverage run --branch TestFiguras2.py
coverage report -m
