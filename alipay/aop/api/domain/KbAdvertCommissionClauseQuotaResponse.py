#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbAdvertCommissionClauseQuotaResponse(object):

    def __init__(self):
        self._quota_amount = None

    @property
    def quota_amount(self):
        return self._quota_amount

    @quota_amount.setter
    def quota_amount(self, value):
        self._quota_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.quota_amount:
            if hasattr(self.quota_amount, 'to_alipay_dict'):
                params['quota_amount'] = self.quota_amount.to_alipay_dict()
            else:
                params['quota_amount'] = self.quota_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertCommissionClauseQuotaResponse()
        if 'quota_amount' in d:
            o.quota_amount = d['quota_amount']
        return o


