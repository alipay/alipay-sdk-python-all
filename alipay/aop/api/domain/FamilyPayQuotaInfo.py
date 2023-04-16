#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FamilyPayQuotaInfo(object):

    def __init__(self):
        self._period = None
        self._quota = None

    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, value):
        self._period = value
    @property
    def quota(self):
        return self._quota

    @quota.setter
    def quota(self, value):
        self._quota = value


    def to_alipay_dict(self):
        params = dict()
        if self.period:
            if hasattr(self.period, 'to_alipay_dict'):
                params['period'] = self.period.to_alipay_dict()
            else:
                params['period'] = self.period
        if self.quota:
            if hasattr(self.quota, 'to_alipay_dict'):
                params['quota'] = self.quota.to_alipay_dict()
            else:
                params['quota'] = self.quota
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FamilyPayQuotaInfo()
        if 'period' in d:
            o.period = d['period']
        if 'quota' in d:
            o.quota = d['quota']
        return o


