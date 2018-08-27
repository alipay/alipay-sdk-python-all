#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017-12-20

@author: liuqun
'''


class AopException(Exception):
    def __init__(self):
        self.code = None
        self.msg = None
        self.sub_code = None
        self.sub_msg = None

    def __str__(self, *args, **kwargs):
        sb = "code=" + self.code + \
             " msg=" + self.msg + \
             " sub_code=" + self.sub_code + \
             " sub_msg=" + self.sub_msg
        return sb


class WrongModelTypeException(Exception):
    pass


class RequestException(Exception):
    pass


class ResponseException(Exception):
    pass