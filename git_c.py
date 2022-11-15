'''
Install GitPython
https://github.com/gitpython-developers/GitPython.git
Or in pycharm - "Python Packages" - gitpython
Or pip install gitpython
https://blog.finxter.com/how-to-install-gitpython-in-python/
'''


import os
from git.repo import Repo
from datetime import datetime
import git
import sys


# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d.%m.%Y_%H.%M.%S")
print("date and time =", dt_string)
commitT = dt_string
commitTs = str(dt_string)


path = 'Absolute Path' # here you have to add the path of your folder
if not os.path.exists(path):   # Check if it exists
    os.makedirs(path)          # If not make it
os.chdir(path)
repo = Repo(path)


def man_commit():
    global commitT
    commitT = input('Place your message:==> ')

    repo.git.add(A=True)
    repo.index.commit(commitT)

    origin = repo.remotes[0]
    origin.push()


def auto_commit():
    global commitT

    repo.git.add(A=True)
    repo.index.commit(commitT)

    origin = repo.remotes[0]
    origin.push()
    print('Auto git commit')


def git_clone():
    repr = input('Enter the link of the git repo you want to clone : =>  ')
    git.Repo.clone_from(repr, path, branch='main') # Here you add the repo you want to add manualy
    print('Clone', dt_string)


def auto_git_clone():
    global path
    git.Repo.clone_from('Your repo', path, branch='main')  # Here you add the repo you want to add for auto clone
    print('Clone', dt_string)


def chs():
    inp = input('Commit = cm; Auto Commit = acm; Clone = cl:==>  ; Auto Clone = acl:==>')
    if inp == 'cm':
        man_commit()
    elif inp == 'acm':
        auto_commit()
    elif inp == 'cl':
        git_clone()
    elif inp == 'acl':
        auto_git_clone()
    else:
        print('Try again')
        chs()

    y_n = input('If you want choose another type "y", if you want to exit type "n":==>  ')

    if y_n == 'y':
        chs()
    elif y_n == 'n':
        sys.exit()


if __name__ == "__main__":
    chs()
