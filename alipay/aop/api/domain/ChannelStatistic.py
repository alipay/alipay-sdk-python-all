#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ChannelStatistic(object):

    def __init__(self):
        self._pay_channel = None
        self._refund_amount = None
        self._settle_amount = None
        self._trade_amount = None
        self._trade_count = None

    @property
    def pay_channel(self):
        return self._pay_channel

    @pay_channel.setter
    def pay_channel(self, value):
        self._pay_channel = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def settle_amount(self):
        return self._settle_amount

    @settle_amount.setter
    def settle_amount(self, value):
        self._settle_amount = value
    @property
    def trade_amount(self):
        return self._trade_amount

    @trade_amount.setter
    def trade_amount(self, value):
        self._trade_amount = value
    @property
    def trade_count(self):
        return self._trade_count

    @trade_count.setter
    def trade_count(self, value):
        self._trade_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.pay_channel:
            if hasattr(self.pay_channel, 'to_alipay_dict'):
                params['pay_channel'] = self.pay_channel.to_alipay_dict()
            else:
                params['pay_channel'] = self.pay_channel
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.settle_amount:
            if hasattr(self.settle_amount, 'to_alipay_dict'):
                params['settle_amount'] = self.settle_amount.to_alipay_dict()
            else:
                params['settle_amount'] = self.settle_amount
        if self.trade_amount:
            if hasattr(self.trade_amount, 'to_alipay_dict'):
                params['trade_amount'] = self.trade_amount.to_alipay_dict()
            else:
                params['trade_amount'] = self.trade_amount
        if self.trade_count:
            if hasattr(self.trade_count, 'to_alipay_dict'):
                params['trade_count'] = self.trade_count.to_alipay_dict()
            else:
                params['trade_count'] = self.trade_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChannelStatistic()
        if 'pay_channel' in d:
            o.pay_channel = d['pay_channel']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'settle_amount' in d:
            o.settle_amount = d['settle_amount']
        if 'trade_amount' in d:
            o.trade_amount = d['trade_amount']
        if 'trade_count' in d:
            o.trade_count = d['trade_count']
        return o


