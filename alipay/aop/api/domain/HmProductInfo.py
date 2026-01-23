#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HmProductInfo(object):

    def __init__(self):
        self._product_amount = None
        self._product_code = None
        self._product_count = None
        self._product_name = None

    @property
    def product_amount(self):
        return self._product_amount

    @product_amount.setter
    def product_amount(self, value):
        self._product_amount = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def product_count(self):
        return self._product_count

    @product_count.setter
    def product_count(self, value):
        self._product_count = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.product_amount:
            if hasattr(self.product_amount, 'to_alipay_dict'):
                params['product_amount'] = self.product_amount.to_alipay_dict()
            else:
                params['product_amount'] = self.product_amount
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.product_count:
            if hasattr(self.product_count, 'to_alipay_dict'):
                params['product_count'] = self.product_count.to_alipay_dict()
            else:
                params['product_count'] = self.product_count
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HmProductInfo()
        if 'product_amount' in d:
            o.product_amount = d['product_amount']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'product_count' in d:
            o.product_count = d['product_count']
        if 'product_name' in d:
            o.product_name = d['product_name']
        return o


