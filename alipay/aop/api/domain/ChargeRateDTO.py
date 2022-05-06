#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChargeRateDTO(object):

    def __init__(self):
        self._biz_type = None
        self._charge_type = None
        self._fix_rate = None
        self._max_amount = None
        self._min_amount = None
        self._rate_type = None
        self._ratio = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def charge_type(self):
        return self._charge_type

    @charge_type.setter
    def charge_type(self, value):
        self._charge_type = value
    @property
    def fix_rate(self):
        return self._fix_rate

    @fix_rate.setter
    def fix_rate(self, value):
        self._fix_rate = value
    @property
    def max_amount(self):
        return self._max_amount

    @max_amount.setter
    def max_amount(self, value):
        self._max_amount = value
    @property
    def min_amount(self):
        return self._min_amount

    @min_amount.setter
    def min_amount(self, value):
        self._min_amount = value
    @property
    def rate_type(self):
        return self._rate_type

    @rate_type.setter
    def rate_type(self, value):
        self._rate_type = value
    @property
    def ratio(self):
        return self._ratio

    @ratio.setter
    def ratio(self, value):
        self._ratio = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.charge_type:
            if hasattr(self.charge_type, 'to_alipay_dict'):
                params['charge_type'] = self.charge_type.to_alipay_dict()
            else:
                params['charge_type'] = self.charge_type
        if self.fix_rate:
            if hasattr(self.fix_rate, 'to_alipay_dict'):
                params['fix_rate'] = self.fix_rate.to_alipay_dict()
            else:
                params['fix_rate'] = self.fix_rate
        if self.max_amount:
            if hasattr(self.max_amount, 'to_alipay_dict'):
                params['max_amount'] = self.max_amount.to_alipay_dict()
            else:
                params['max_amount'] = self.max_amount
        if self.min_amount:
            if hasattr(self.min_amount, 'to_alipay_dict'):
                params['min_amount'] = self.min_amount.to_alipay_dict()
            else:
                params['min_amount'] = self.min_amount
        if self.rate_type:
            if hasattr(self.rate_type, 'to_alipay_dict'):
                params['rate_type'] = self.rate_type.to_alipay_dict()
            else:
                params['rate_type'] = self.rate_type
        if self.ratio:
            if hasattr(self.ratio, 'to_alipay_dict'):
                params['ratio'] = self.ratio.to_alipay_dict()
            else:
                params['ratio'] = self.ratio
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChargeRateDTO()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'charge_type' in d:
            o.charge_type = d['charge_type']
        if 'fix_rate' in d:
            o.fix_rate = d['fix_rate']
        if 'max_amount' in d:
            o.max_amount = d['max_amount']
        if 'min_amount' in d:
            o.min_amount = d['min_amount']
        if 'rate_type' in d:
            o.rate_type = d['rate_type']
        if 'ratio' in d:
            o.ratio = d['ratio']
        return o


