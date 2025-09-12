#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SalesSolutionExt(object):

    def __init__(self):
        self._batch_sign_count = None
        self._price = None

    @property
    def batch_sign_count(self):
        return self._batch_sign_count

    @batch_sign_count.setter
    def batch_sign_count(self, value):
        self._batch_sign_count = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_sign_count:
            if hasattr(self.batch_sign_count, 'to_alipay_dict'):
                params['batch_sign_count'] = self.batch_sign_count.to_alipay_dict()
            else:
                params['batch_sign_count'] = self.batch_sign_count
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SalesSolutionExt()
        if 'batch_sign_count' in d:
            o.batch_sign_count = d['batch_sign_count']
        if 'price' in d:
            o.price = d['price']
        return o


