#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditPricing import CreditPricing


class Credit(object):

    def __init__(self):
        self._credit_amt = None
        self._credit_pricing_list = None
        self._expire_time = None
        self._loan_type = None
        self._product_code = None

    @property
    def credit_amt(self):
        return self._credit_amt

    @credit_amt.setter
    def credit_amt(self, value):
        self._credit_amt = value
    @property
    def credit_pricing_list(self):
        return self._credit_pricing_list

    @credit_pricing_list.setter
    def credit_pricing_list(self, value):
        if isinstance(value, list):
            self._credit_pricing_list = list()
            for i in value:
                if isinstance(i, CreditPricing):
                    self._credit_pricing_list.append(i)
                else:
                    self._credit_pricing_list.append(CreditPricing.from_alipay_dict(i))
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def loan_type(self):
        return self._loan_type

    @loan_type.setter
    def loan_type(self, value):
        self._loan_type = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.credit_amt:
            if hasattr(self.credit_amt, 'to_alipay_dict'):
                params['credit_amt'] = self.credit_amt.to_alipay_dict()
            else:
                params['credit_amt'] = self.credit_amt
        if self.credit_pricing_list:
            if isinstance(self.credit_pricing_list, list):
                for i in range(0, len(self.credit_pricing_list)):
                    element = self.credit_pricing_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.credit_pricing_list[i] = element.to_alipay_dict()
            if hasattr(self.credit_pricing_list, 'to_alipay_dict'):
                params['credit_pricing_list'] = self.credit_pricing_list.to_alipay_dict()
            else:
                params['credit_pricing_list'] = self.credit_pricing_list
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.loan_type:
            if hasattr(self.loan_type, 'to_alipay_dict'):
                params['loan_type'] = self.loan_type.to_alipay_dict()
            else:
                params['loan_type'] = self.loan_type
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
        o = Credit()
        if 'credit_amt' in d:
            o.credit_amt = d['credit_amt']
        if 'credit_pricing_list' in d:
            o.credit_pricing_list = d['credit_pricing_list']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'loan_type' in d:
            o.loan_type = d['loan_type']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


