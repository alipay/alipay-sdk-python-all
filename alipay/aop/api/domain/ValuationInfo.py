#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ValuationInfo(object):

    def __init__(self):
        self._valuate_price = None
        self._valuate_supplier = None
        self._valuate_time = None

    @property
    def valuate_price(self):
        return self._valuate_price

    @valuate_price.setter
    def valuate_price(self, value):
        self._valuate_price = value
    @property
    def valuate_supplier(self):
        return self._valuate_supplier

    @valuate_supplier.setter
    def valuate_supplier(self, value):
        self._valuate_supplier = value
    @property
    def valuate_time(self):
        return self._valuate_time

    @valuate_time.setter
    def valuate_time(self, value):
        self._valuate_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.valuate_price:
            if hasattr(self.valuate_price, 'to_alipay_dict'):
                params['valuate_price'] = self.valuate_price.to_alipay_dict()
            else:
                params['valuate_price'] = self.valuate_price
        if self.valuate_supplier:
            if hasattr(self.valuate_supplier, 'to_alipay_dict'):
                params['valuate_supplier'] = self.valuate_supplier.to_alipay_dict()
            else:
                params['valuate_supplier'] = self.valuate_supplier
        if self.valuate_time:
            if hasattr(self.valuate_time, 'to_alipay_dict'):
                params['valuate_time'] = self.valuate_time.to_alipay_dict()
            else:
                params['valuate_time'] = self.valuate_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ValuationInfo()
        if 'valuate_price' in d:
            o.valuate_price = d['valuate_price']
        if 'valuate_supplier' in d:
            o.valuate_supplier = d['valuate_supplier']
        if 'valuate_time' in d:
            o.valuate_time = d['valuate_time']
        return o


