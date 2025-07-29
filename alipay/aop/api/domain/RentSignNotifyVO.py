#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentSignNotifyVO(object):

    def __init__(self):
        self._auth_no = None
        self._sign_product = None
        self._sign_time = None

    @property
    def auth_no(self):
        return self._auth_no

    @auth_no.setter
    def auth_no(self, value):
        self._auth_no = value
    @property
    def sign_product(self):
        return self._sign_product

    @sign_product.setter
    def sign_product(self, value):
        self._sign_product = value
    @property
    def sign_time(self):
        return self._sign_time

    @sign_time.setter
    def sign_time(self, value):
        self._sign_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_no:
            if hasattr(self.auth_no, 'to_alipay_dict'):
                params['auth_no'] = self.auth_no.to_alipay_dict()
            else:
                params['auth_no'] = self.auth_no
        if self.sign_product:
            if hasattr(self.sign_product, 'to_alipay_dict'):
                params['sign_product'] = self.sign_product.to_alipay_dict()
            else:
                params['sign_product'] = self.sign_product
        if self.sign_time:
            if hasattr(self.sign_time, 'to_alipay_dict'):
                params['sign_time'] = self.sign_time.to_alipay_dict()
            else:
                params['sign_time'] = self.sign_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentSignNotifyVO()
        if 'auth_no' in d:
            o.auth_no = d['auth_no']
        if 'sign_product' in d:
            o.sign_product = d['sign_product']
        if 'sign_time' in d:
            o.sign_time = d['sign_time']
        return o


