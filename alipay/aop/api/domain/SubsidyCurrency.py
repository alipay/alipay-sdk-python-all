#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SubsidyCurrency(object):

    def __init__(self):
        self._currency_code = None
        self._default_fraction_digits = None
        self._numeric_code = None

    @property
    def currency_code(self):
        return self._currency_code

    @currency_code.setter
    def currency_code(self, value):
        self._currency_code = value
    @property
    def default_fraction_digits(self):
        return self._default_fraction_digits

    @default_fraction_digits.setter
    def default_fraction_digits(self, value):
        self._default_fraction_digits = value
    @property
    def numeric_code(self):
        return self._numeric_code

    @numeric_code.setter
    def numeric_code(self, value):
        self._numeric_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.currency_code:
            if hasattr(self.currency_code, 'to_alipay_dict'):
                params['currency_code'] = self.currency_code.to_alipay_dict()
            else:
                params['currency_code'] = self.currency_code
        if self.default_fraction_digits:
            if hasattr(self.default_fraction_digits, 'to_alipay_dict'):
                params['default_fraction_digits'] = self.default_fraction_digits.to_alipay_dict()
            else:
                params['default_fraction_digits'] = self.default_fraction_digits
        if self.numeric_code:
            if hasattr(self.numeric_code, 'to_alipay_dict'):
                params['numeric_code'] = self.numeric_code.to_alipay_dict()
            else:
                params['numeric_code'] = self.numeric_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SubsidyCurrency()
        if 'currency_code' in d:
            o.currency_code = d['currency_code']
        if 'default_fraction_digits' in d:
            o.default_fraction_digits = d['default_fraction_digits']
        if 'numeric_code' in d:
            o.numeric_code = d['numeric_code']
        return o


