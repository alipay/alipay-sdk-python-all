#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Amount import Amount
from alipay.aop.api.domain.Amount import Amount


class ReduceByInfoDTO(object):

    def __init__(self):
        self._amount = None
        self._floor_amount = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if isinstance(value, Amount):
            self._amount = value
        else:
            self._amount = Amount.from_alipay_dict(value)
    @property
    def floor_amount(self):
        return self._floor_amount

    @floor_amount.setter
    def floor_amount(self, value):
        if isinstance(value, Amount):
            self._floor_amount = value
        else:
            self._floor_amount = Amount.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.floor_amount:
            if hasattr(self.floor_amount, 'to_alipay_dict'):
                params['floor_amount'] = self.floor_amount.to_alipay_dict()
            else:
                params['floor_amount'] = self.floor_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReduceByInfoDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'floor_amount' in d:
            o.floor_amount = d['floor_amount']
        return o


