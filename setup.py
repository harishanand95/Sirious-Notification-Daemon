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
    subprocess.call(["sudo", "chmod","+x","Sirious"])
    subprocess.call(["sudo", "cp","Sirious","/usr/local/bin/"])
    print "\033c"
    print """\nNow Sirious is a command in terminal (its Sirious not sirious) and to create a key binding for this command,
\n GNOME:
\n1. Go to System > Preferences(just Settings) > Keyboard >Keyboard Shortcuts
\n2. Click the Add button or Custom Shortcuts (a plus sign)
\n3. Choose a Name for your shortcut (can be just about anything)
\n4. Give command as Sirious 
\n5. Like other key binded provide a key by clicking on disabled and now it shows the name and its key-bind

You can use any other method to create a key-bind for Sirious command
"""
