#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeliveryChannelInfo(object):

    def __init__(self):
        self._booth_code = None
        self._channel = None
        self._channel_name = None

    @property
    def booth_code(self):
        return self._booth_code

    @booth_code.setter
    def booth_code(self, value):
        self._booth_code = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def channel_name(self):
        return self._channel_name

    @channel_name.setter
    def channel_name(self, value):
        self._channel_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.booth_code:
            if hasattr(self.booth_code, 'to_alipay_dict'):
                params['booth_code'] = self.booth_code.to_alipay_dict()
            else:
                params['booth_code'] = self.booth_code
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
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
        o = DeliveryChannelInfo()
        if 'booth_code' in d:
            o.booth_code = d['booth_code']
        if 'channel' in d:
            o.channel = d['channel']
        if 'channel_name' in d:
            o.channel_name = d['channel_name']
        return o


