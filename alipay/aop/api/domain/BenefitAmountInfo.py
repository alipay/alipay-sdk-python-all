#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Amount import Amount
from alipay.aop.api.domain.Amount import Amount


class BenefitAmountInfo(object):

    def __init__(self):
        self._benefit_available_amount = None
        self._benefit_total_amount = None

    @property
    def benefit_available_amount(self):
        return self._benefit_available_amount

    @benefit_available_amount.setter
    def benefit_available_amount(self, value):
        if isinstance(value, Amount):
            self._benefit_available_amount = value
        else:
            self._benefit_available_amount = Amount.from_alipay_dict(value)
    @property
    def benefit_total_amount(self):
        return self._benefit_total_amount

    @benefit_total_amount.setter
    def benefit_total_amount(self, value):
        if isinstance(value, Amount):
            self._benefit_total_amount = value
        else:
            self._benefit_total_amount = Amount.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_available_amount:
            if hasattr(self.benefit_available_amount, 'to_alipay_dict'):
                params['benefit_available_amount'] = self.benefit_available_amount.to_alipay_dict()
            else:
                params['benefit_available_amount'] = self.benefit_available_amount
        if self.benefit_total_amount:
            if hasattr(self.benefit_total_amount, 'to_alipay_dict'):
                params['benefit_total_amount'] = self.benefit_total_amount.to_alipay_dict()
            else:
                params['benefit_total_amount'] = self.benefit_total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitAmountInfo()
        if 'benefit_available_amount' in d:
            o.benefit_available_amount = d['benefit_available_amount']
        if 'benefit_total_amount' in d:
            o.benefit_total_amount = d['benefit_total_amount']
        return o


