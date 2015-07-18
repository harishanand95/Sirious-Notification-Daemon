#!/usr/bin/python
import subprocess
import platform
try:
    import pip
except:
    print "pip package not found installing pip..."
    system = platform.linux_distribution()
    if system[0] == 'Fedora':
        subprocess.call(["sudo", "yum","install","python-pip"])
    else:
        subprocess.call(["sudo", "apt-get","install","python-pip"])
    import pip
    pass


def install(package):
    pip.main(['install', package])


if __name__ == '__main__':
    system = platform.linux_distribution()
    if system[0] == 'Fedora':
        subprocess.call(["sudo", "yum","install","xclip"])
    else:
        subprocess.call(["sudo", "apt-get","install","xclip"])
    install('bleach')
    install('Pillow')
    subprocess.call(["sudo", "cp","Sirious","/usr/bin"])