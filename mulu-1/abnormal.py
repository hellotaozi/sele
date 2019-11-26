#!/usr/bin/python3
# -*- coding: UTF-8 -*-

def say_hello(name=None):
    if name is None:
        raise NameError("'name' cannot be found.")
    else:
        print("hello,%s"%name)

say_hello()