#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderTax(object):

    def __init__(self):
        self._tax_amount = None
        self._tax_project_code = None
        self._tax_project_name = None

    @property
    def tax_amount(self):
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, value):
        self._tax_amount = value
    @property
    def tax_project_code(self):
        return self._tax_project_code

    @tax_project_code.setter
    def tax_project_code(self, value):
        self._tax_project_code = value
    @property
    def tax_project_name(self):
        return self._tax_project_name

    @tax_project_name.setter
    def tax_project_name(self, value):
        self._tax_project_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.tax_amount:
            if hasattr(self.tax_amount, 'to_alipay_dict'):
                params['tax_amount'] = self.tax_amount.to_alipay_dict()
            else:
                params['tax_amount'] = self.tax_amount
        if self.tax_project_code:
            if hasattr(self.tax_project_code, 'to_alipay_dict'):
                params['tax_project_code'] = self.tax_project_code.to_alipay_dict()
            else:
                params['tax_project_code'] = self.tax_project_code
        if self.tax_project_name:
            if hasattr(self.tax_project_name, 'to_alipay_dict'):
                params['tax_project_name'] = self.tax_project_name.to_alipay_dict()
            else:
                params['tax_project_name'] = self.tax_project_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderTax()
        if 'tax_amount' in d:
            o.tax_amount = d['tax_amount']
        if 'tax_project_code' in d:
            o.tax_project_code = d['tax_project_code']
        if 'tax_project_name' in d:
            o.tax_project_name = d['tax_project_name']
        return o


