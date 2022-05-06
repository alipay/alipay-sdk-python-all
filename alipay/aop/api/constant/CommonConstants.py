#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017-12-20

@author: liuqun
'''
import re
import threading
import sys


ALIPAY_SDK_PYTHON_VERSION = "alipay-sdk-python-dynamicVersionNo"

PYTHON_VERSION_3 = True
if sys.version_info < (3, 0):
    PYTHON_VERSION_3 = False

PATTERN_RESPONSE_BEGIN = re.compile(r'(\"[a-zA-z_]+_response\"[ \t\n]*:[ \t\n]*\{)')
PATTERN_RESPONSE_SIGN_BEGIN = re.compile(r'(\}[ \t\n]*,[ \t\n]*\"sign\"[ \t\n]*:[ \t\n]*\")')

PATTERN_RESPONSE_ENCRYPT_BEGIN = re.compile(r'(\"[a-zA-z_]+_response\"[ \t\n]*:[ \t\n]*\")')
PATTERN_RESPONSE_SIGN_ENCRYPT_BEGIN = re.compile(r'(\"[ \t\n]*,[ \t\n]*\"sign\"[ \t\n]*:[ \t\n]*\")')

THREAD_LOCAL = threading.local()