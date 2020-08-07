@echo off
cd /d {path to the create repository that contains create.py file}
py create.py %1 && cd /d C:/Users/%username%/Desktop/%1 && code .