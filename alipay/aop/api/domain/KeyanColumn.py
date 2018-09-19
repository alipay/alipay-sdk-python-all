#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KeyanColumn(object):

    def __init__(self):
        self._password = None

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value


    def to_alipay_dict(self):
        params = dict()
        if self.password:
            if hasattr(self.password, 'to_alipay_dict'):
                params['password'] = self.password.to_alipay_dict()
            else:
                params['password'] = self.password
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KeyanColumn()
        if 'password' in d:
            o.password = d['password']
        return o


