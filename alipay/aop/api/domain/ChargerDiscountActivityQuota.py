#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChargerDiscountActivityQuota(object):

    def __init__(self):
        self._period_type = None
        self._remaining_count = None
        self._total_count = None
        self._used_count = None

    @property
    def period_type(self):
        return self._period_type

    @period_type.setter
    def period_type(self, value):
        self._period_type = value
    @property
    def remaining_count(self):
        return self._remaining_count

    @remaining_count.setter
    def remaining_count(self, value):
        self._remaining_count = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def used_count(self):
        return self._used_count

    @used_count.setter
    def used_count(self, value):
        self._used_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.period_type:
            if hasattr(self.period_type, 'to_alipay_dict'):
                params['period_type'] = self.period_type.to_alipay_dict()
            else:
                params['period_type'] = self.period_type
        if self.remaining_count:
            if hasattr(self.remaining_count, 'to_alipay_dict'):
                params['remaining_count'] = self.remaining_count.to_alipay_dict()
            else:
                params['remaining_count'] = self.remaining_count
        if self.total_count:
            if hasattr(self.total_count, 'to_alipay_dict'):
                params['total_count'] = self.total_count.to_alipay_dict()
            else:
                params['total_count'] = self.total_count
        if self.used_count:
            if hasattr(self.used_count, 'to_alipay_dict'):
                params['used_count'] = self.used_count.to_alipay_dict()
            else:
                params['used_count'] = self.used_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChargerDiscountActivityQuota()
        if 'period_type' in d:
            o.period_type = d['period_type']
        if 'remaining_count' in d:
            o.remaining_count = d['remaining_count']
        if 'total_count' in d:
            o.total_count = d['total_count']
        if 'used_count' in d:
            o.used_count = d['used_count']
        return o


