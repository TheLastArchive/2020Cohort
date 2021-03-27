
#!/usr/bin/env python3
from __future__ import print_function
import subprocess
import os

"""
this IF statement checks if program is installed
"""
my_downloads = os.popen("cd\ncd Downloads\nls -a").read()
my_downloads = my_downloads.split()

path = "~/Downloads/clinic"
if 'clinic' not in my_downloads:
    print("Clinic file not found. Please make sure clinic folder is in the Downloads folder")
    exit()

my_bin = os.popen("cd\ncd bin\ncd clinic\nls -a").read()
my_bin = my_bin.split()
if 'clinic' in my_bin:
    print("already installed run \"clinic -help\" to see all options")
    exit()

"""
this TRY block checks if all essential dependencies are installed
"""
try:
    from googleapiclient.discovery import build
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
except ImportError:
    print("seems your system is missing some components")
    user = input("permission to install google-api-python-client? (y/n): ")
    if user.lower() == 'y':
        os.system("pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib")
try:
    import rich
except ImportError:
    os.system("pip3 install rich")


"""
This IF statement creates a bin folder and
copies all neccessary files to the created bin folder
and adds it to computer's environment path
"""
if os.path.exists("~/bin/clinic/clinic"):
    pass
else:
    if os.path.isdir("~/bin") == False:
        os.system("mkdir -p ~/bin")
        os.system("cp -R ~/Downloads/clinic/ ~/bin/")
        os.system("chmod +x ~/bin/clinic/clinic")
        os.system("mkdir -p ~/bin/clinic/tokens")

    if os.path.isdir("~/bin") == True and os.path.exists("~/bin/clinic") == False:
        os.system("cp -R ~/Downloads/clinic/ ~/bin/")
        os.system("chmod +x ~/bin/clinic/clinic")

# os.system("~/home")
my_list = os.popen("cd\nls -a").read()
my_list = my_list.split()
if '.zshrc' in my_list and '.bashrc' in my_list:
    print("using zsh in terminal")
    os.system("echo PATH='$PATH:~/bin/clinic' >> ~/.bashrc")
    os.system('echo PATH=\"\$PATH:\$HOME/bin/clinic\" >> ~/.zshrc')
    os.system("source ~/.zshrc")
elif '.bshrc' in my_list and '.zshrc' not in my_list:
    print("using bash in terminal")
    os.system("echo PATH='$PATH:~/bin/clinic' >> ~/.bashrc")
    os.system("source ~/.bashrc")

print("Thank you for installing Code_Clinic")

