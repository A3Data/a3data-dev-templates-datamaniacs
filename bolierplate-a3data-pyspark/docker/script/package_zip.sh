#!/usr/bin/env bash
'''
Package py dependencies and main py application into a `app.zip` folder
'''
mkdir to_upload
poetry export -f requirements.txt --output requirements.txt
pip3 -q install -r requirements.txt -t to_upload
rm -r requirements.txt
cp -r {setup.py,app} to_upload
cd to_upload
version=$(echo `python3 setup.py --version` | sed s/_/-/g)
python3 setup.py sdist --format=zip
unzip -q "dist/app-$version.zip"
cd "app-$version"
# Small hack so that main package (app) can be added to python path
touch __init__.py
zip -q -r "../../app.zip" *
cd ../../
rm -r to_upload
