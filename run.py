# Author: Dan

# Run install.py before hand
import subprocess
import os
import git

pwd = 'coremark'
repo_url = 'https://github.com/eembc/coremark.git'

print(f'Cloning Repository: {repo_url}')
git.Repo.clone_from(repo_url, pwd)
print(f'Repository Cloned at location: {pwd}')

def run_cmd(command):
    p1 = subprocess.call([command], cwd=pwd)
    results('coremark/run1.log')
    results('coremark/run2.log')

def results(runs):
    print("=======================================")
    print("Results:")
    file = open(runs, 'r')
    for line in file:
        print(line)

run_cmd('make')

