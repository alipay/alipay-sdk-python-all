#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbAdvertCommissionClausePercentage(object):

    def __init__(self):
        self._commission_rate_end = None
        self._commission_rate_start = None
        self._max_limit_end = None
        self._max_limit_start = None

    @property
    def commission_rate_end(self):
        return self._commission_rate_end

    @commission_rate_end.setter
    def commission_rate_end(self, value):
        self._commission_rate_end = value
    @property
    def commission_rate_start(self):
        return self._commission_rate_start

    @commission_rate_start.setter
    def commission_rate_start(self, value):
        self._commission_rate_start = value
    @property
    def max_limit_end(self):
        return self._max_limit_end

    @max_limit_end.setter
    def max_limit_end(self, value):
        self._max_limit_end = value
    @property
    def max_limit_start(self):
        return self._max_limit_start

    @max_limit_start.setter
    def max_limit_start(self, value):
        self._max_limit_start = value


    def to_alipay_dict(self):
        params = dict()
        if self.commission_rate_end:
            if hasattr(self.commission_rate_end, 'to_alipay_dict'):
                params['commission_rate_end'] = self.commission_rate_end.to_alipay_dict()
            else:
                params['commission_rate_end'] = self.commission_rate_end
        if self.commission_rate_start:
            if hasattr(self.commission_rate_start, 'to_alipay_dict'):
                params['commission_rate_start'] = self.commission_rate_start.to_alipay_dict()
            else:
                params['commission_rate_start'] = self.commission_rate_start
        if self.max_limit_end:
            if hasattr(self.max_limit_end, 'to_alipay_dict'):
                params['max_limit_end'] = self.max_limit_end.to_alipay_dict()
            else:
                params['max_limit_end'] = self.max_limit_end
        if self.max_limit_start:
            if hasattr(self.max_limit_start, 'to_alipay_dict'):
                params['max_limit_start'] = self.max_limit_start.to_alipay_dict()
            else:
                params['max_limit_start'] = self.max_limit_start
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertCommissionClausePercentage()
        if 'commission_rate_end' in d:
            o.commission_rate_end = d['commission_rate_end']
        if 'commission_rate_start' in d:
            o.commission_rate_start = d['commission_rate_start']
        if 'max_limit_end' in d:
            o.max_limit_end = d['max_limit_end']
        if 'max_limit_start' in d:
            o.max_limit_start = d['max_limit_start']
        return o


