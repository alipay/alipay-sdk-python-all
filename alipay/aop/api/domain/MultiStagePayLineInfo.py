#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MultiStagePayLineInfo(object):

    def __init__(self):
        self._payment_amount = None
        self._payment_idx = None

    @property
    def payment_amount(self):
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self._payment_amount = value
    @property
    def payment_idx(self):
        return self._payment_idx

    @payment_idx.setter
    def payment_idx(self, value):
        self._payment_idx = value


    def to_alipay_dict(self):
        params = dict()
        if self.payment_amount:
            if hasattr(self.payment_amount, 'to_alipay_dict'):
                params['payment_amount'] = self.payment_amount.to_alipay_dict()
            else:
                params['payment_amount'] = self.payment_amount
        if self.payment_idx:
            if hasattr(self.payment_idx, 'to_alipay_dict'):
                params['payment_idx'] = self.payment_idx.to_alipay_dict()
            else:
                params['payment_idx'] = self.payment_idx
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MultiStagePayLineInfo()
        if 'payment_amount' in d:
            o.payment_amount = d['payment_amount']
        if 'payment_idx' in d:
            o.payment_idx = d['payment_idx']
        return o


