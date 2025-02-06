#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleQcReportProductInfo(object):

    def __init__(self):
        self._estimated_price = None
        self._product_code = None
        self._product_name = None
        self._real_price = None

    @property
    def estimated_price(self):
        return self._estimated_price

    @estimated_price.setter
    def estimated_price(self, value):
        self._estimated_price = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def real_price(self):
        return self._real_price

    @real_price.setter
    def real_price(self, value):
        self._real_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.estimated_price:
            if hasattr(self.estimated_price, 'to_alipay_dict'):
                params['estimated_price'] = self.estimated_price.to_alipay_dict()
            else:
                params['estimated_price'] = self.estimated_price
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.real_price:
            if hasattr(self.real_price, 'to_alipay_dict'):
                params['real_price'] = self.real_price.to_alipay_dict()
            else:
                params['real_price'] = self.real_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleQcReportProductInfo()
        if 'estimated_price' in d:
            o.estimated_price = d['estimated_price']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'real_price' in d:
            o.real_price = d['real_price']
        return o


