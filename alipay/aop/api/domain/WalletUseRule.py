#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WalletUseRule(object):

    def __init__(self):
        self._merchant_rule = None

    @property
    def merchant_rule(self):
        return self._merchant_rule

    @merchant_rule.setter
    def merchant_rule(self, value):
        self._merchant_rule = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_rule:
            if hasattr(self.merchant_rule, 'to_alipay_dict'):
                params['merchant_rule'] = self.merchant_rule.to_alipay_dict()
            else:
                params['merchant_rule'] = self.merchant_rule
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WalletUseRule()
        if 'merchant_rule' in d:
            o.merchant_rule = d['merchant_rule']
        return o


