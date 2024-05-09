#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CardDiscountRecoverRule(object):

    def __init__(self):
        self._least_period = None
        self._recover_rule = None

    @property
    def least_period(self):
        return self._least_period

    @least_period.setter
    def least_period(self, value):
        self._least_period = value
    @property
    def recover_rule(self):
        return self._recover_rule

    @recover_rule.setter
    def recover_rule(self, value):
        self._recover_rule = value


    def to_alipay_dict(self):
        params = dict()
        if self.least_period:
            if hasattr(self.least_period, 'to_alipay_dict'):
                params['least_period'] = self.least_period.to_alipay_dict()
            else:
                params['least_period'] = self.least_period
        if self.recover_rule:
            if hasattr(self.recover_rule, 'to_alipay_dict'):
                params['recover_rule'] = self.recover_rule.to_alipay_dict()
            else:
                params['recover_rule'] = self.recover_rule
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CardDiscountRecoverRule()
        if 'least_period' in d:
            o.least_period = d['least_period']
        if 'recover_rule' in d:
            o.recover_rule = d['recover_rule']
        return o


