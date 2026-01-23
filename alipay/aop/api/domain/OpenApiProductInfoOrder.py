#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class OpenApiProductInfoOrder(object):

    def __init__(self):
        self._amt = None
        self._product_name = None
        self._tax_exclusive_amt = None

    @property
    def amt(self):
        return self._amt

    @amt.setter
    def amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._amt = value
        else:
            self._amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def tax_exclusive_amt(self):
        return self._tax_exclusive_amt

    @tax_exclusive_amt.setter
    def tax_exclusive_amt(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._tax_exclusive_amt = value
        else:
            self._tax_exclusive_amt = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.amt:
            if hasattr(self.amt, 'to_alipay_dict'):
                params['amt'] = self.amt.to_alipay_dict()
            else:
                params['amt'] = self.amt
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.tax_exclusive_amt:
            if hasattr(self.tax_exclusive_amt, 'to_alipay_dict'):
                params['tax_exclusive_amt'] = self.tax_exclusive_amt.to_alipay_dict()
            else:
                params['tax_exclusive_amt'] = self.tax_exclusive_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiProductInfoOrder()
        if 'amt' in d:
            o.amt = d['amt']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'tax_exclusive_amt' in d:
            o.tax_exclusive_amt = d['tax_exclusive_amt']
        return o


