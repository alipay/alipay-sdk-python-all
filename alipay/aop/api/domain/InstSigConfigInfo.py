#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InstSigConfigInfo(object):

    def __init__(self):
        self._industry_code = None
        self._value_factor = None
        self._value_rank = None
        self._value_sig = None

    @property
    def industry_code(self):
        return self._industry_code

    @industry_code.setter
    def industry_code(self, value):
        self._industry_code = value
    @property
    def value_factor(self):
        return self._value_factor

    @value_factor.setter
    def value_factor(self, value):
        self._value_factor = value
    @property
    def value_rank(self):
        return self._value_rank

    @value_rank.setter
    def value_rank(self, value):
        self._value_rank = value
    @property
    def value_sig(self):
        return self._value_sig

    @value_sig.setter
    def value_sig(self, value):
        self._value_sig = value


    def to_alipay_dict(self):
        params = dict()
        if self.industry_code:
            if hasattr(self.industry_code, 'to_alipay_dict'):
                params['industry_code'] = self.industry_code.to_alipay_dict()
            else:
                params['industry_code'] = self.industry_code
        if self.value_factor:
            if hasattr(self.value_factor, 'to_alipay_dict'):
                params['value_factor'] = self.value_factor.to_alipay_dict()
            else:
                params['value_factor'] = self.value_factor
        if self.value_rank:
            if hasattr(self.value_rank, 'to_alipay_dict'):
                params['value_rank'] = self.value_rank.to_alipay_dict()
            else:
                params['value_rank'] = self.value_rank
        if self.value_sig:
            if hasattr(self.value_sig, 'to_alipay_dict'):
                params['value_sig'] = self.value_sig.to_alipay_dict()
            else:
                params['value_sig'] = self.value_sig
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InstSigConfigInfo()
        if 'industry_code' in d:
            o.industry_code = d['industry_code']
        if 'value_factor' in d:
            o.value_factor = d['value_factor']
        if 'value_rank' in d:
            o.value_rank = d['value_rank']
        if 'value_sig' in d:
            o.value_sig = d['value_sig']
        return o


