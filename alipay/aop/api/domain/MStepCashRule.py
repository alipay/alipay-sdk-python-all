#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MStepCashRule(object):

    def __init__(self):
        self._reduction_amount = None
        self._threshold_amount = None

    @property
    def reduction_amount(self):
        return self._reduction_amount

    @reduction_amount.setter
    def reduction_amount(self, value):
        self._reduction_amount = value
    @property
    def threshold_amount(self):
        return self._threshold_amount

    @threshold_amount.setter
    def threshold_amount(self, value):
        self._threshold_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.reduction_amount:
            if hasattr(self.reduction_amount, 'to_alipay_dict'):
                params['reduction_amount'] = self.reduction_amount.to_alipay_dict()
            else:
                params['reduction_amount'] = self.reduction_amount
        if self.threshold_amount:
            if hasattr(self.threshold_amount, 'to_alipay_dict'):
                params['threshold_amount'] = self.threshold_amount.to_alipay_dict()
            else:
                params['threshold_amount'] = self.threshold_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MStepCashRule()
        if 'reduction_amount' in d:
            o.reduction_amount = d['reduction_amount']
        if 'threshold_amount' in d:
            o.threshold_amount = d['threshold_amount']
        return o


