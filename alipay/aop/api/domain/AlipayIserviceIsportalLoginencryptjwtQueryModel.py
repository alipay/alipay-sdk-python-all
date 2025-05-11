#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIsportalLoginencryptjwtQueryModel(object):

    def __init__(self):
        self._expiry_time = None
        self._login_token = None

    @property
    def expiry_time(self):
        return self._expiry_time

    @expiry_time.setter
    def expiry_time(self, value):
        self._expiry_time = value
    @property
    def login_token(self):
        return self._login_token

    @login_token.setter
    def login_token(self, value):
        self._login_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.expiry_time:
            if hasattr(self.expiry_time, 'to_alipay_dict'):
                params['expiry_time'] = self.expiry_time.to_alipay_dict()
            else:
                params['expiry_time'] = self.expiry_time
        if self.login_token:
            if hasattr(self.login_token, 'to_alipay_dict'):
                params['login_token'] = self.login_token.to_alipay_dict()
            else:
                params['login_token'] = self.login_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceIsportalLoginencryptjwtQueryModel()
        if 'expiry_time' in d:
            o.expiry_time = d['expiry_time']
        if 'login_token' in d:
            o.login_token = d['login_token']
        return o


