#!/usr/bin/env python3
# 2018-10-13 (cc) <paul4hough@gmail.com>

# import sys
# import os
# import subprocess as sp

py_dev_pkgs{ 'Ubuntu18' }[
    'python3-dev',
    'pip3',
    ]
py_dev_pips{ 'Ubuntu18' }[
    'pytest'
    ]

def test_role_py_dev ():
    ''' validate python development role
    '''

    foreach pkg in py_dev_pkgs
    assert package.installed(
    def __init__(self, *args, **kwargs):
        '''anything interesting?''''
        pass

    def method(self, *args, **kwargs):
        '''worthless method
        '''
        pass

def main():
    '''Application entry point
    '''
    print('do nothing')
    sys.exit(2)

if __name__ == '__main__':
    main()
