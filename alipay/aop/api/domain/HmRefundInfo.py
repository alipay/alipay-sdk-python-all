#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HmRefundInfo(object):

    def __init__(self):
        self._refund_amount = None
        self._refund_channel = None
        self._refund_time = None

    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_channel(self):
        return self._refund_channel

    @refund_channel.setter
    def refund_channel(self, value):
        self._refund_channel = value
    @property
    def refund_time(self):
        return self._refund_time

    @refund_time.setter
    def refund_time(self, value):
        self._refund_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_channel:
            if hasattr(self.refund_channel, 'to_alipay_dict'):
                params['refund_channel'] = self.refund_channel.to_alipay_dict()
            else:
                params['refund_channel'] = self.refund_channel
        if self.refund_time:
            if hasattr(self.refund_time, 'to_alipay_dict'):
                params['refund_time'] = self.refund_time.to_alipay_dict()
            else:
                params['refund_time'] = self.refund_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HmRefundInfo()
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_channel' in d:
            o.refund_channel = d['refund_channel']
        if 'refund_time' in d:
            o.refund_time = d['refund_time']
        return o


