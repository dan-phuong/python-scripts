# Author: Dan

# Run install.py before hand
import subprocess
import os

pwd = 'coremark'

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

