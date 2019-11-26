#!/usr/bin/python3
# -*- coding: UTF-8 -*-


import sys
from os.path import dirname, abspath

project_path = dirname(dirname(abspath(__file__)))
sys.path.append(project_path + '/mulu-1')
from one_sele import add

c = add(2, 3)
print(c)
# print(sys.path)
