#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InfraTemplateMoneyRuleResp(object):

    def __init__(self):
        self._decimal = None

    @property
    def decimal(self):
        return self._decimal

    @decimal.setter
    def decimal(self, value):
        self._decimal = value


    def to_alipay_dict(self):
        params = dict()
        if self.decimal:
            if hasattr(self.decimal, 'to_alipay_dict'):
                params['decimal'] = self.decimal.to_alipay_dict()
            else:
                params['decimal'] = self.decimal
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InfraTemplateMoneyRuleResp()
        if 'decimal' in d:
            o.decimal = d['decimal']
        return o


