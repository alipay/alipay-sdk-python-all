#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserCertifyPayload(object):

    def __init__(self):
        self._auth_code = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserCertifyPayload()
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        return o


