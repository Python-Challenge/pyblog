#!/usr/bin/env python
# coding: utf-8

import os, sys, subprocess, datetime, socket

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
    comment = 'from:' + user + '@' + host_name + str(args[1:])
    print(comment)
else:
    comment = 'from:' + user + '@' + host_name 

cmd_add = "git add -A"
cmd_comm = "git commit -a -m " + comment
cmd_push_org = "git push origin master -v"
cmd_pushf_org = "git push origin master -fv"

subprocess.call( cmd_add, shell=True )
subprocess.call( cmd_comm, shell=True )

print('--------------------- to origin ------------------')
subprocess.call(cmd_pushf_org, shell=True)

sys.exit()

