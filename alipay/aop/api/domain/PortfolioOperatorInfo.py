#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PortfolioOperatorInfo(object):

    def __init__(self):
        self._auth_code = None
        self._op_role = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def op_role(self):
        return self._op_role

    @op_role.setter
    def op_role(self, value):
        self._op_role = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.op_role:
            if hasattr(self.op_role, 'to_alipay_dict'):
                params['op_role'] = self.op_role.to_alipay_dict()
            else:
                params['op_role'] = self.op_role
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PortfolioOperatorInfo()
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'op_role' in d:
            o.op_role = d['op_role']
        return o


