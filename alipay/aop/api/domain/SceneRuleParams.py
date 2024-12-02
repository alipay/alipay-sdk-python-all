#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SceneRuleParams(object):

    def __init__(self):
        self._discount_period = None
        self._low_price_period = None

    @property
    def discount_period(self):
        return self._discount_period

    @discount_period.setter
    def discount_period(self, value):
        self._discount_period = value
    @property
    def low_price_period(self):
        return self._low_price_period

    @low_price_period.setter
    def low_price_period(self, value):
        self._low_price_period = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount_period:
            if hasattr(self.discount_period, 'to_alipay_dict'):
                params['discount_period'] = self.discount_period.to_alipay_dict()
            else:
                params['discount_period'] = self.discount_period
        if self.low_price_period:
            if hasattr(self.low_price_period, 'to_alipay_dict'):
                params['low_price_period'] = self.low_price_period.to_alipay_dict()
            else:
                params['low_price_period'] = self.low_price_period
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SceneRuleParams()
        if 'discount_period' in d:
            o.discount_period = d['discount_period']
        if 'low_price_period' in d:
            o.low_price_period = d['low_price_period']
        return o


