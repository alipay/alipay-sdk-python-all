#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SignProductVO(object):

    def __init__(self):
        self._product_type = None
        self._sign_url = None

    @property
    def product_type(self):
        return self._product_type

    @product_type.setter
    def product_type(self, value):
        self._product_type = value
    @property
    def sign_url(self):
        return self._sign_url

    @sign_url.setter
    def sign_url(self, value):
        self._sign_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.product_type:
            if hasattr(self.product_type, 'to_alipay_dict'):
                params['product_type'] = self.product_type.to_alipay_dict()
            else:
                params['product_type'] = self.product_type
        if self.sign_url:
            if hasattr(self.sign_url, 'to_alipay_dict'):
                params['sign_url'] = self.sign_url.to_alipay_dict()
            else:
                params['sign_url'] = self.sign_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignProductVO()
        if 'product_type' in d:
            o.product_type = d['product_type']
        if 'sign_url' in d:
            o.sign_url = d['sign_url']
        return o


