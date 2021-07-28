#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsurancePeriod(object):

    def __init__(self):
        self._period = None
        self._period_unit = None

    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def period_unit(self):
        return self._period_unit

    @period_unit.setter
    def period_unit(self, value):
        self._period_unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.period_unit:
            if hasattr(self.period_unit, 'to_alipay_dict'):
                params['period_unit'] = self.period_unit.to_alipay_dict()
            else:
                params['period_unit'] = self.period_unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsurancePeriod()
        if 'period' in d:
            o.period = d['period']
        if 'period_unit' in d:
            o.period_unit = d['period_unit']
        return o


