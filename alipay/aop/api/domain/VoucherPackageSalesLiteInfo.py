#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherPackageSalesLiteInfo(object):

    def __init__(self):
        self._budget = None
        self._sale_price = None

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        self._budget = value
    @property
    def sale_price(self):
        return self._sale_price

    @sale_price.setter
    def sale_price(self, value):
        self._sale_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.budget:
            if hasattr(self.budget, 'to_alipay_dict'):
                params['budget'] = self.budget.to_alipay_dict()
            else:
                params['budget'] = self.budget
        if self.sale_price:
            if hasattr(self.sale_price, 'to_alipay_dict'):
                params['sale_price'] = self.sale_price.to_alipay_dict()
            else:
                params['sale_price'] = self.sale_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherPackageSalesLiteInfo()
        if 'budget' in d:
            o.budget = d['budget']
        if 'sale_price' in d:
            o.sale_price = d['sale_price']
        return o


