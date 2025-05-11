#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIsportalLogincontextQueryModel(object):

    def __init__(self):
        self._login_token = None

    @property
    def login_token(self):
        return self._login_token

    @login_token.setter
    def login_token(self, value):
        self._login_token = value


    def to_alipay_dict(self):
        params = dict()
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
        o = AlipayIserviceIsportalLogincontextQueryModel()
        if 'login_token' in d:
            o.login_token = d['login_token']
        return o


