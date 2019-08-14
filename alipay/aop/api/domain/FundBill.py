#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FundBill(object):

    def __init__(self):
        self._amount = None
        self._bank_code = None
        self._fund_channel = None
        self._real_amount = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def bank_code(self):
        return self._bank_code

    @bank_code.setter
    def bank_code(self, value):
        self._bank_code = value
    @property
    def fund_channel(self):
        return self._fund_channel

    @fund_channel.setter
    def fund_channel(self, value):
        self._fund_channel = value
    @property
    def real_amount(self):
        return self._real_amount

    @real_amount.setter
    def real_amount(self, value):
        self._real_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.bank_code:
            if hasattr(self.bank_code, 'to_alipay_dict'):
                params['bank_code'] = self.bank_code.to_alipay_dict()
            else:
                params['bank_code'] = self.bank_code
        if self.fund_channel:
            if hasattr(self.fund_channel, 'to_alipay_dict'):
                params['fund_channel'] = self.fund_channel.to_alipay_dict()
            else:
                params['fund_channel'] = self.fund_channel
        if self.real_amount:
            if hasattr(self.real_amount, 'to_alipay_dict'):
                params['real_amount'] = self.real_amount.to_alipay_dict()
            else:
                params['real_amount'] = self.real_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FundBill()
        if 'amount' in d:
            o.amount = d['amount']
        if 'bank_code' in d:
            o.bank_code = d['bank_code']
        if 'fund_channel' in d:
            o.fund_channel = d['fund_channel']
        if 'real_amount' in d:
            o.real_amount = d['real_amount']
        return o


