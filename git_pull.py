#!/usr/bin/env python
# coding: utf-8


import os, sys, subprocess, datetime, socket


# https://note.nkmk.me/python-os-environ-getenv/
result_env = os.getenv('SSH_ASKPASS')
if result_env != None:
    del os.environ['SSH_ASKPASS']
print('SSH_ASKPASS : ' + str(os.getenv('SSH_ASKPASS')))


cmd_pull_org="git pull origin master"
subprocess.call( cmd_pull_org, shell=True )

