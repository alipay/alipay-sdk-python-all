#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankFinanceYulibaoAccountQueryModel(object):

    def __init__(self):
        self._fund_code = None

    @property
    def fund_code(self):
        return self._fund_code

    @fund_code.setter
    def fund_code(self, value):
        self._fund_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.fund_code:
            if hasattr(self.fund_code, 'to_alipay_dict'):
                params['fund_code'] = self.fund_code.to_alipay_dict()
            else:
                params['fund_code'] = self.fund_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankFinanceYulibaoAccountQueryModel()
        if 'fund_code' in d:
            o.fund_code = d['fund_code']
        return o


