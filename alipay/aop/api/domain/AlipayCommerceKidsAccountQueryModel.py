#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceKidsAccountQueryModel(object):

    def __init__(self):
        self._login_name = None
        self._product_code = None

    @property
    def login_name(self):
        return self._login_name

    @login_name.setter
    def login_name(self, value):
        self._login_name = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.login_name:
            if hasattr(self.login_name, 'to_alipay_dict'):
                params['login_name'] = self.login_name.to_alipay_dict()
            else:
                params['login_name'] = self.login_name
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
        o = AlipayCommerceKidsAccountQueryModel()
        if 'login_name' in d:
            o.login_name = d['login_name']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


