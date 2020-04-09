import os

os.system('git add -A')
commit = input('commit log:')
os.system('git commit -m "%s"'%commit)
os.system('git push -u origin master -f')
