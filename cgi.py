#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess
import cgi

form = cgi.FieldStorage()
x = form.getvalue('c')
x = x.lower().strip().split()
if 'not' in x or 'donot' in x or 'don\'t' in x:
    print("Okay, command will not be executed")
elif 'run' in x or 'show' in x or 'display' in x or 'tell' in x or 'execute' in x or 'launch' in x:
    
    if 'date' in x:
        out  = subprocess.getoutput('date')
        print(out[0:11])
    elif 'time' in x:
        tm = subprocess.getoutput('date')
        print(date[11:23])
    elif  'ip_address' in x or 'ip' in x:
        print(subprocess.getoutput('ifconfig enp0s3'))
    elif 'process' in x or ('background' in x and 'task' in x) :
        print( subprocess.getoutput('ps -aux'))
    elif 'calculator' in x or 'calci' in x or 'cal' in x:
        print(subprocess.getoutput('bc'))
    elif 'whoami' in x or 'username' in x or ('current' in x and 'user' in x):
        print(subprocess.getoutput('whoami'))
    elif 'pwd' in x or 'cwd' in x or (('current' in x or 'present' in x ) and 'directory' in x) :
        print(subprocess.getoutput('pwd'))
    elif 'shell' in x:
        print(subprocess.getoutput('echo $SHELL'))
    elif 'tty' in x or 'vt' in x or 'terminal' in x:
        print(subprocess.getoutput('tty'))
    elif 'calendar' in x  or 'cal' in x:
       print(subprocess.getoutput('cal'))
    else:
        print('Not Understand')
else:
    print('Plz try launch/run/execute abc format')
