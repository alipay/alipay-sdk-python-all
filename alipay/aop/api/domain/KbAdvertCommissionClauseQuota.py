#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbAdvertCommissionClauseQuota(object):

    def __init__(self):
        self._quota_amount_end = None
        self._quota_amount_start = None

    @property
    def quota_amount_end(self):
        return self._quota_amount_end

    @quota_amount_end.setter
    def quota_amount_end(self, value):
        self._quota_amount_end = value
    @property
    def quota_amount_start(self):
        return self._quota_amount_start

    @quota_amount_start.setter
    def quota_amount_start(self, value):
        self._quota_amount_start = value


    def to_alipay_dict(self):
        params = dict()
        if self.quota_amount_end:
            if hasattr(self.quota_amount_end, 'to_alipay_dict'):
                params['quota_amount_end'] = self.quota_amount_end.to_alipay_dict()
            else:
                params['quota_amount_end'] = self.quota_amount_end
        if self.quota_amount_start:
            if hasattr(self.quota_amount_start, 'to_alipay_dict'):
                params['quota_amount_start'] = self.quota_amount_start.to_alipay_dict()
            else:
                params['quota_amount_start'] = self.quota_amount_start
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertCommissionClauseQuota()
        if 'quota_amount_end' in d:
            o.quota_amount_end = d['quota_amount_end']
        if 'quota_amount_start' in d:
            o.quota_amount_start = d['quota_amount_start']
        return o


