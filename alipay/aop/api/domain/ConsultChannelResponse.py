#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ConsultChannelResponse(object):

    def __init__(self):
        self._channel = None
        self._channel_amount = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def channel_amount(self):
        return self._channel_amount

    @channel_amount.setter
    def channel_amount(self, value):
        self._channel_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.channel_amount:
            if hasattr(self.channel_amount, 'to_alipay_dict'):
                params['channel_amount'] = self.channel_amount.to_alipay_dict()
            else:
                params['channel_amount'] = self.channel_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsultChannelResponse()
        if 'channel' in d:
            o.channel = d['channel']
        if 'channel_amount' in d:
            o.channel_amount = d['channel_amount']
        return o


