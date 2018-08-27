#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FeeValue(object):

    def __init__(self):
        self._bottom_cent = None
        self._currency_code = None
        self._fix_cent = None
        self._lower = None
        self._rate_unit = None
        self._rate_value = None
        self._top_cent = None
        self._upper = None

    @property
    def bottom_cent(self):
        return self._bottom_cent

    @bottom_cent.setter
    def bottom_cent(self, value):
        self._bottom_cent = value
    @property
    def currency_code(self):
        return self._currency_code

    @currency_code.setter
    def currency_code(self, value):
        self._currency_code = value
    @property
    def fix_cent(self):
        return self._fix_cent

    @fix_cent.setter
    def fix_cent(self, value):
        self._fix_cent = value
    @property
    def lower(self):
        return self._lower

    @lower.setter
    def lower(self, value):
        self._lower = value
    @property
    def rate_unit(self):
        return self._rate_unit

    @rate_unit.setter
    def rate_unit(self, value):
        self._rate_unit = value
    @property
    def rate_value(self):
        return self._rate_value

    @rate_value.setter
    def rate_value(self, value):
        self._rate_value = value
    @property
    def top_cent(self):
        return self._top_cent

    @top_cent.setter
    def top_cent(self, value):
        self._top_cent = value
    @property
    def upper(self):
        return self._upper

    @upper.setter
    def upper(self, value):
        self._upper = value


    def to_alipay_dict(self):
        params = dict()
        if self.bottom_cent:
            if hasattr(self.bottom_cent, 'to_alipay_dict'):
                params['bottom_cent'] = self.bottom_cent.to_alipay_dict()
            else:
                params['bottom_cent'] = self.bottom_cent
        if self.currency_code:
            if hasattr(self.currency_code, 'to_alipay_dict'):
                params['currency_code'] = self.currency_code.to_alipay_dict()
            else:
                params['currency_code'] = self.currency_code
        if self.fix_cent:
            if hasattr(self.fix_cent, 'to_alipay_dict'):
                params['fix_cent'] = self.fix_cent.to_alipay_dict()
            else:
                params['fix_cent'] = self.fix_cent
        if self.lower:
            if hasattr(self.lower, 'to_alipay_dict'):
                params['lower'] = self.lower.to_alipay_dict()
            else:
                params['lower'] = self.lower
        if self.rate_unit:
            if hasattr(self.rate_unit, 'to_alipay_dict'):
                params['rate_unit'] = self.rate_unit.to_alipay_dict()
            else:
                params['rate_unit'] = self.rate_unit
        if self.rate_value:
            if hasattr(self.rate_value, 'to_alipay_dict'):
                params['rate_value'] = self.rate_value.to_alipay_dict()
            else:
                params['rate_value'] = self.rate_value
        if self.top_cent:
            if hasattr(self.top_cent, 'to_alipay_dict'):
                params['top_cent'] = self.top_cent.to_alipay_dict()
            else:
                params['top_cent'] = self.top_cent
        if self.upper:
            if hasattr(self.upper, 'to_alipay_dict'):
                params['upper'] = self.upper.to_alipay_dict()
            else:
                params['upper'] = self.upper
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FeeValue()
        if 'bottom_cent' in d:
            o.bottom_cent = d['bottom_cent']
        if 'currency_code' in d:
            o.currency_code = d['currency_code']
        if 'fix_cent' in d:
            o.fix_cent = d['fix_cent']
        if 'lower' in d:
            o.lower = d['lower']
        if 'rate_unit' in d:
            o.rate_unit = d['rate_unit']
        if 'rate_value' in d:
            o.rate_value = d['rate_value']
        if 'top_cent' in d:
            o.top_cent = d['top_cent']
        if 'upper' in d:
            o.upper = d['upper']
        return o


