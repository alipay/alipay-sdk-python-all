#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbAdvertCommissionClausePercentageResponse(object):

    def __init__(self):
        self._commission_rate = None
        self._max_limit = None

    @property
    def commission_rate(self):
        return self._commission_rate

    @commission_rate.setter
    def commission_rate(self, value):
        self._commission_rate = value
    @property
    def max_limit(self):
        return self._max_limit

    @max_limit.setter
    def max_limit(self, value):
        self._max_limit = value


    def to_alipay_dict(self):
        params = dict()
        if self.commission_rate:
            if hasattr(self.commission_rate, 'to_alipay_dict'):
                params['commission_rate'] = self.commission_rate.to_alipay_dict()
            else:
                params['commission_rate'] = self.commission_rate
        if self.max_limit:
            if hasattr(self.max_limit, 'to_alipay_dict'):
                params['max_limit'] = self.max_limit.to_alipay_dict()
            else:
                params['max_limit'] = self.max_limit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertCommissionClausePercentageResponse()
        if 'commission_rate' in d:
            o.commission_rate = d['commission_rate']
        if 'max_limit' in d:
            o.max_limit = d['max_limit']
        return o


