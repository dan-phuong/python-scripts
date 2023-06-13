# Author: Dan

import os
import subprocess
import sys
import git
from subprocess import STDOUT, check_call

# Dependencies #
git_package = "git-all"
pip_package = "python3-pip"
gitPython_pip = "GitPython"

def sudo_install(package):
    print(f"Installing: {package}")
    subprocess.run(['sudo','apt','install','-y', package], check=True)
    print(f"Installed {package}\n")

def pip_install(package):
    print(f"Installing: {package}")
    subprocess.check_call([sys.executable, '-m','pip','install',package])
    print(f"Installed {package}")

sudo_install(git_package)
sudo_install(pip_package)

pip_install(gitPython_pip)

repo_url = 'https://github.com/eembc/coremark.git'
local_path = 'coremark'

print(f'Cloning Repository: {repo_url}')
git.Repo.clone_from(repo_url, local_path)
print(f'Repository Cloned at location: {local_path}')


