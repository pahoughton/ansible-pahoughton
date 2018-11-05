#!/usr/bin/env python3
# 2018-10-13 (cc) <paul4hough@gmail.com>

import sys
import os
import subprocess as sp
import yaml


def main():
    '''Application entry point
    '''

    # load vars from yml
    with open("../group_vars/all.yml", 'r') as stream:
        vars = yaml.load(stream)
    print(vars)

if __name__ == '__main__':
    main()
