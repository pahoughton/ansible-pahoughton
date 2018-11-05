#!/usr/bin/env python3
# 2018-10-24 (cc) <paul4hough@gmail.com>


def test_ssh_port(host):
    assert host.socket("tcp://0.0.0.0:22").is_listening


# server has to be manually started
# def test_xserver_port(host):
#     assert host.socket("tcp://0.0.0.0:6000").is_listening
