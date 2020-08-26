#!/bin/bash
pip uninstall -y pycrypto
rm -rf /usr/lib64/python2.6/site-packages/Crypto/
rm -rf /usr/lib64/python2.6/site-packages/pycrypto-2.6.1-py2.6-linux-x86_64.egg
pip install pycrypto==2.4.1