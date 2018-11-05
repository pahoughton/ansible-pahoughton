#!/usr/bin/env python3
# 2018-10-13 (cc) <paul4hough@gmail.com>

'''
pips:
  - testinfra
  - molecule
  - tox
'''


class test_role_ans_dev (object):
    ''' test_role_ans_dev useless class
    '''
    assert packages.installed(
        yaml.array( pkgs[common],
                    pkgs[os][common],
                    pkgs[os][major], )

        )

    assert pips.installed()

    assert validate.python("https://github.com/python/stuff")
