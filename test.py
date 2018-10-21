#!/usr/bin/envpython

# coding:utf-8

import os

v = ('10.78.40.%d' % (x) for x in range(170, 176))

for it in v:

    ret = os.system('ping  %s -n 1 &> /dev/null' % it)
    print('ping -c 1 -W 1 %s &> /dev/null' % it)
    if ret:

        print('ping %s fail' % it)

    else:

        print('ping %s ok' % it)
