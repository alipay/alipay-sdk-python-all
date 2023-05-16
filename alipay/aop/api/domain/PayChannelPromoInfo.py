#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PayChannelPromoInfo(object):

    def __init__(self):
        self._channel_balance = None
        self._channel_index = None
        self._channel_name = None

    @property
    def channel_balance(self):
        return self._channel_balance

    @channel_balance.setter
    def channel_balance(self, value):
        self._channel_balance = value
    @property
    def channel_index(self):
        return self._channel_index

    @channel_index.setter
    def channel_index(self, value):
        self._channel_index = value
    @property
    def channel_name(self):
        return self._channel_name

    @channel_name.setter
    def channel_name(self, value):
        self._channel_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_balance:
            if hasattr(self.channel_balance, 'to_alipay_dict'):
                params['channel_balance'] = self.channel_balance.to_alipay_dict()
            else:
                params['channel_balance'] = self.channel_balance
        if self.channel_index:
            if hasattr(self.channel_index, 'to_alipay_dict'):
                params['channel_index'] = self.channel_index.to_alipay_dict()
            else:
                params['channel_index'] = self.channel_index
        if self.channel_name:
            if hasattr(self.channel_name, 'to_alipay_dict'):
                params['channel_name'] = self.channel_name.to_alipay_dict()
            else:
                params['channel_name'] = self.channel_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PayChannelPromoInfo()
        if 'channel_balance' in d:
            o.channel_balance = d['channel_balance']
        if 'channel_index' in d:
            o.channel_index = d['channel_index']
        if 'channel_name' in d:
            o.channel_name = d['channel_name']
        return o


