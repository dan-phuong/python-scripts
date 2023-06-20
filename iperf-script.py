import sys
import distro
import requests
from bs4 import BeautifulSoup

print(distro.name())
print(distro.id())

def install_iperf_ubuntu():
    iperf_package = "iperf3"
    # Update Ubuntu
    subprocess.run(["sudo", "apt", "update"], check=True)
    # Install iPerf3
    subprocess.run(["sudo", "apt", "-y", "install", iperf_package], check=True)
    pass

def install_iperf_centOS():
    pass

def install_iperf_arch():
    pass

def meow():
    pass

install_iperf_ubuntu()
