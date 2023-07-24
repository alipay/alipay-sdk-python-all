#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Amount import Amount
from alipay.aop.api.domain.Amount import Amount


class CashBackInfoDTO(object):

    def __init__(self):
        self._amount = None
        self._origin_amount = None

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
    def origin_amount(self):
        return self._origin_amount

    @origin_amount.setter
    def origin_amount(self, value):
        if isinstance(value, Amount):
            self._origin_amount = value
        else:
            self._origin_amount = Amount.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.origin_amount:
            if hasattr(self.origin_amount, 'to_alipay_dict'):
                params['origin_amount'] = self.origin_amount.to_alipay_dict()
            else:
                params['origin_amount'] = self.origin_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CashBackInfoDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'origin_amount' in d:
            o.origin_amount = d['origin_amount']
        return o


