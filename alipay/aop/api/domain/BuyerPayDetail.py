#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BuyerPayDetail(object):

    def __init__(self):
        self._amount = None
        self._pay_channel = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def pay_channel(self):
        return self._pay_channel

    @pay_channel.setter
    def pay_channel(self, value):
        self._pay_channel = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.pay_channel:
            if hasattr(self.pay_channel, 'to_alipay_dict'):
                params['pay_channel'] = self.pay_channel.to_alipay_dict()
            else:
                params['pay_channel'] = self.pay_channel
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BuyerPayDetail()
        if 'amount' in d:
            o.amount = d['amount']
        if 'pay_channel' in d:
            o.pay_channel = d['pay_channel']
        return o


