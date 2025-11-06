#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InteopOpAuthProductInfo(object):

    def __init__(self):
        self._permission_codes = None
        self._product_code = None

    @property
    def permission_codes(self):
        return self._permission_codes

    @permission_codes.setter
    def permission_codes(self, value):
        if isinstance(value, list):
            self._permission_codes = list()
            for i in value:
                self._permission_codes.append(i)
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.permission_codes:
            if isinstance(self.permission_codes, list):
                for i in range(0, len(self.permission_codes)):
                    element = self.permission_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.permission_codes[i] = element.to_alipay_dict()
            if hasattr(self.permission_codes, 'to_alipay_dict'):
                params['permission_codes'] = self.permission_codes.to_alipay_dict()
            else:
                params['permission_codes'] = self.permission_codes
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InteopOpAuthProductInfo()
        if 'permission_codes' in d:
            o.permission_codes = d['permission_codes']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


