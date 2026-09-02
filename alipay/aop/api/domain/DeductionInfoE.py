#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeductionInfoE(object):

    def __init__(self):
        self._deduction_amount = None
        self._deduction_reason = None

    @property
    def deduction_amount(self):
        return self._deduction_amount

    @deduction_amount.setter
    def deduction_amount(self, value):
        self._deduction_amount = value
    @property
    def deduction_reason(self):
        return self._deduction_reason

    @deduction_reason.setter
    def deduction_reason(self, value):
        self._deduction_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.deduction_amount:
            if hasattr(self.deduction_amount, 'to_alipay_dict'):
                params['deduction_amount'] = self.deduction_amount.to_alipay_dict()
            else:
                params['deduction_amount'] = self.deduction_amount
        if self.deduction_reason:
            if hasattr(self.deduction_reason, 'to_alipay_dict'):
                params['deduction_reason'] = self.deduction_reason.to_alipay_dict()
            else:
                params['deduction_reason'] = self.deduction_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeductionInfoE()
        if 'deduction_amount' in d:
            o.deduction_amount = d['deduction_amount']
        if 'deduction_reason' in d:
            o.deduction_reason = d['deduction_reason']
        return o


