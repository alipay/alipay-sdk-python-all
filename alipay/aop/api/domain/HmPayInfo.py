#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HmPayInfo(object):

    def __init__(self):
        self._pay_amount = None
        self._pay_channel = None
        self._pay_time = None

    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_channel(self):
        return self._pay_channel

    @pay_channel.setter
    def pay_channel(self, value):
        self._pay_channel = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pay_channel:
            if hasattr(self.pay_channel, 'to_alipay_dict'):
                params['pay_channel'] = self.pay_channel.to_alipay_dict()
            else:
                params['pay_channel'] = self.pay_channel
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HmPayInfo()
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_channel' in d:
            o.pay_channel = d['pay_channel']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        return o


