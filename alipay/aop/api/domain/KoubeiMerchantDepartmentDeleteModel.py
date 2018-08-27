#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiMerchantDepartmentDeleteModel(object):

    def __init__(self):
        self._auth_code = None
        self._dept_id = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def dept_id(self):
        return self._dept_id

    @dept_id.setter
    def dept_id(self, value):
        self._dept_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.dept_id:
            if hasattr(self.dept_id, 'to_alipay_dict'):
                params['dept_id'] = self.dept_id.to_alipay_dict()
            else:
                params['dept_id'] = self.dept_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMerchantDepartmentDeleteModel()
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'dept_id' in d:
            o.dept_id = d['dept_id']
        return o


