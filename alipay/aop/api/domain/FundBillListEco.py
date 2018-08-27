#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FundBillListEco(object):

    def __init__(self):
        self._amount = None
        self._fund_channel = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def fund_channel(self):
        return self._fund_channel

    @fund_channel.setter
    def fund_channel(self, value):
        self._fund_channel = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.fund_channel:
            if hasattr(self.fund_channel, 'to_alipay_dict'):
                params['fund_channel'] = self.fund_channel.to_alipay_dict()
            else:
                params['fund_channel'] = self.fund_channel
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FundBillListEco()
        if 'amount' in d:
            o.amount = d['amount']
        if 'fund_channel' in d:
            o.fund_channel = d['fund_channel']
        return o


