#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandEcoQuantityQueryModel(object):

    def __init__(self):
        self._eco_code = None
        self._month = None

    @property
    def eco_code(self):
        return self._eco_code

    @eco_code.setter
    def eco_code(self, value):
        self._eco_code = value
    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, value):
        self._month = value


    def to_alipay_dict(self):
        params = dict()
        if self.eco_code:
            if hasattr(self.eco_code, 'to_alipay_dict'):
                params['eco_code'] = self.eco_code.to_alipay_dict()
            else:
                params['eco_code'] = self.eco_code
        if self.month:
            if hasattr(self.month, 'to_alipay_dict'):
                params['month'] = self.month.to_alipay_dict()
            else:
                params['month'] = self.month
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandEcoQuantityQueryModel()
        if 'eco_code' in d:
            o.eco_code = d['eco_code']
        if 'month' in d:
            o.month = d['month']
        return o


