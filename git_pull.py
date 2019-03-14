#!/usr/bin/env python
# coding: utf-8


# https://qiita.com/tdrk/items/9b23ad6a58ac4032bb3b

import os, sys, subprocess, datetime, socket

# https://note.nkmk.me/python-os-environ-getenv/
result_env = os.getenv('SSH_ASKPASS')
if result_env != None:
    del os.environ['SSH_ASKPASS']
print('SSH_ASKPASS : ' + str(os.getenv('SSH_ASKPASS')))

cmd_pull_azu="git pull azure_ssh master"
subprocess.call( cmd_pull_azu, shell=True )

