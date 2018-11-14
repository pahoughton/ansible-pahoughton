## ..

[![Test Build Status](https://travis-ci.org/pahoughton/...png)](https://travis-ci.org/pahoughton/..)

Paul's home deployments.

## Validate

rake test
testinfra backend://node/


## Features

validated configuration of my nodes.
see testinfra/features.txt


### notes

yed - drawing tool
https://www.yworks.com/products/yed/download

#### zuul - hpZ800 - openSuse15 Leap

* change hostname
  - /etc/hostname /etc/hosts /etc/postfix/main.cf
* visudo
* zypper ref
* zypper up
* shutdown -r now
* sudo pip install --upgrade pip
* sudo pip install ansible

http://download.opensuse.org/repositories/Cloud:/OpenStack:/Rocky/openSUSE_Leap_15.0



zypper ar http://download.opensuse.org/repositories/Cloud:/OpenStack:/Rocky/openSUSE_Leap_42.3 OBS:Cloud:OpenStack:Rocky
zypper install git-core ntp openssh python-devel sudo gcc libffi-devel libopenssl-devel



- groups:
  - phys:
    - cbed (i7x32G):
      - prometheus
      - zuul
      - kuber
      - docker
      - vagrant
      - vbox,
      - libvirt
      - lxc
      - test, build & dev tools

  - virt


promethius monitoring
zuulci workflows
molecule, tox, serverspec, rspec
perl, python, ruby, ansible, g++, gcc



NONE

## Install

Can't

## Usage

You wouldn't want to.

## Contribute

[Github pahoughton/..](https://github.com/pahoughton/..)

## Licenses

(cc) <paul4hough@gmail.com>

[![LICENSE](http://i.creativecommons.org/l/by/3.0/88x31.png)](http://creativecommons.org/licenses/by/3.0/)

[![endorse](https://api.coderwall.com/pahoughton/endorsecount.png)](https://coderwall.com/pahoughton)
