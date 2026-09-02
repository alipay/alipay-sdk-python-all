#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndustryInvoiceChannelOrderInfo(object):

    def __init__(self):
        self._channel_order_amount = None
        self._channel_order_no = None

    @property
    def channel_order_amount(self):
        return self._channel_order_amount

    @channel_order_amount.setter
    def channel_order_amount(self, value):
        self._channel_order_amount = value
    @property
    def channel_order_no(self):
        return self._channel_order_no

    @channel_order_no.setter
    def channel_order_no(self, value):
        self._channel_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_order_amount:
            if hasattr(self.channel_order_amount, 'to_alipay_dict'):
                params['channel_order_amount'] = self.channel_order_amount.to_alipay_dict()
            else:
                params['channel_order_amount'] = self.channel_order_amount
        if self.channel_order_no:
            if hasattr(self.channel_order_no, 'to_alipay_dict'):
                params['channel_order_no'] = self.channel_order_no.to_alipay_dict()
            else:
                params['channel_order_no'] = self.channel_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndustryInvoiceChannelOrderInfo()
        if 'channel_order_amount' in d:
            o.channel_order_amount = d['channel_order_amount']
        if 'channel_order_no' in d:
            o.channel_order_no = d['channel_order_no']
        return o


