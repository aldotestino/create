import os
import sys
import requests
import subprocess
from time import sleep

url = 'https://api.github.com/user/repos'
token = 'your git hub access token'
gitHubUsername = 'your git hub username'
username = 'your Windows account username'

try:
    pName = sys.argv[1]
    os.chdir(f"C:/Users/{username}/Desktop")
    os.mkdir(pName)
    os.chdir(pName)
    readme = open('README.md', 'w')
    readme.write(f"# {pName}")
    readme.close()
except IndexError:
    print('No arguments found, exiting...')
    exit(1)
except FileExistsError:
    print('The project already exist on the desktop, exiting...')
    exit(1)

req = requests.post(url, json={"name": pName}, headers={
    'Authorization': f"token {token}", 'content-type': 'application/json'})

if req.status_code == 422:
    print('Repository already exist, exiting')
    exit(1)
else:
    print('⚡Repository created, initializing...')
    subprocess.run('git init')
    sleep(1)
    subprocess.run('git add .')
    sleep(1)
    subprocess.run('git commit -m "first commit"')
    sleep(1)
    subprocess.run(
        f"git remote add origin https://github.com/{gitHubUsername}/{pName}.git")
    sleep(1)
    subprocess.run('git push -u origin master')
    exit(0)
