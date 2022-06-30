#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi


class GFAOpenAPIOuterTaxInfoDetail(object):

    def __init__(self):
        self._hd_tax_amount = None
        self._tax_amount = None
        self._tax_rate = None
        self._tax_type = None

    @property
    def hd_tax_amount(self):
        return self._hd_tax_amount

    @hd_tax_amount.setter
    def hd_tax_amount(self, value):
        self._hd_tax_amount = value
    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._tax_amount = value
        else:
            self._tax_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def tax_rate(self):
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, value):
        self._tax_rate = value
    @property
    def tax_type(self):
        return self._tax_type

    @tax_type.setter
    def tax_type(self, value):
        self._tax_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.hd_tax_amount:
            if hasattr(self.hd_tax_amount, 'to_alipay_dict'):
                params['hd_tax_amount'] = self.hd_tax_amount.to_alipay_dict()
            else:
                params['hd_tax_amount'] = self.hd_tax_amount
        if self.tax_amount:
            if hasattr(self.tax_amount, 'to_alipay_dict'):
                params['tax_amount'] = self.tax_amount.to_alipay_dict()
            else:
                params['tax_amount'] = self.tax_amount
        if self.tax_rate:
            if hasattr(self.tax_rate, 'to_alipay_dict'):
                params['tax_rate'] = self.tax_rate.to_alipay_dict()
            else:
                params['tax_rate'] = self.tax_rate
        if self.tax_type:
            if hasattr(self.tax_type, 'to_alipay_dict'):
                params['tax_type'] = self.tax_type.to_alipay_dict()
            else:
                params['tax_type'] = self.tax_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GFAOpenAPIOuterTaxInfoDetail()
        if 'hd_tax_amount' in d:
            o.hd_tax_amount = d['hd_tax_amount']
        if 'tax_amount' in d:
            o.tax_amount = d['tax_amount']
        if 'tax_rate' in d:
            o.tax_rate = d['tax_rate']
        if 'tax_type' in d:
            o.tax_type = d['tax_type']
        return o


