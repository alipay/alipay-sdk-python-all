#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupFundsImcomeDetails(object):

    def __init__(self):
        self._amount = None
        self._fund_distributions = None
        self._payer_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def fund_distributions(self):
        return self._fund_distributions

    @fund_distributions.setter
    def fund_distributions(self, value):
        self._fund_distributions = value
    @property
    def payer_id(self):
        return self._payer_id

    @payer_id.setter
    def payer_id(self, value):
        self._payer_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.fund_distributions:
            if hasattr(self.fund_distributions, 'to_alipay_dict'):
                params['fund_distributions'] = self.fund_distributions.to_alipay_dict()
            else:
                params['fund_distributions'] = self.fund_distributions
        if self.payer_id:
            if hasattr(self.payer_id, 'to_alipay_dict'):
                params['payer_id'] = self.payer_id.to_alipay_dict()
            else:
                params['payer_id'] = self.payer_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupFundsImcomeDetails()
        if 'amount' in d:
            o.amount = d['amount']
        if 'fund_distributions' in d:
            o.fund_distributions = d['fund_distributions']
        if 'payer_id' in d:
            o.payer_id = d['payer_id']
        return o


