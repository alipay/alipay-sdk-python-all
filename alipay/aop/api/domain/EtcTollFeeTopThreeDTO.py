#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EtcTollFeeTopThreeDTO(object):

    def __init__(self):
        self._amount = None
        self._ratio = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def ratio(self):
        return self._ratio

    @ratio.setter
    def ratio(self, value):
        self._ratio = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.ratio:
            if hasattr(self.ratio, 'to_alipay_dict'):
                params['ratio'] = self.ratio.to_alipay_dict()
            else:
                params['ratio'] = self.ratio
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EtcTollFeeTopThreeDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'ratio' in d:
            o.ratio = d['ratio']
        return o


