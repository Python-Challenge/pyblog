#!/usr/bin/env python
# coding: utf-8

import os
import sys
import subprocess
import datetime
import socket
import traceback

# https://note.nkmk.me/python-os-environ-getenv/
result_env = os.getenv('SSH_ASKPASS')
if result_env != None:
    del os.environ['SSH_ASKPASS']
print('SSH_ASKPASS : ' + str(os.getenv('SSH_ASKPASS')))

args = sys.argv
argc = len(sys.argv)

now_date = datetime.datetime.now()
print(now_date)

user = os.environ.get("USER")
host_name = socket.gethostname()

if len(sys.argv) >= 2:
    comment = str(args[1:])
    print(comment)
else:
    comment = 'from:' + user + '@' + host_name

print(comment)

cmd_add = "git add -A ."
cmd_comm = "git commit -am " + comment
cmd_push_org = "git push origin master -v"
cmd_pushf_org = "git push origin master -fv"
cmd_pushf_dmake = "git push d-make master -fv"

print(cmd_comm)

try:
    subprocess.call(cmd_add, shell=True)
    subprocess.call(cmd_comm, shell=True)

    print('--------------------- to origin ------------------')
    print('comment : ' + comment)
    subprocess.call(cmd_pushf_org, shell=True)
    subprocess.call(cmd_pushf_dmake, shell=True)
except:
    traceback.print_exc()

sys.exit()
