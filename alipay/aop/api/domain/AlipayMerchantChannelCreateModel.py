#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantChannelCreateModel(object):

    def __init__(self):
        self._channel_code = None
        self._channel_name = None

    @property
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, value):
        self._channel_code = value
    @property
    def channel_name(self):
        return self._channel_name

    @channel_name.setter
    def channel_name(self, value):
        self._channel_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_code:
            if hasattr(self.channel_code, 'to_alipay_dict'):
                params['channel_code'] = self.channel_code.to_alipay_dict()
            else:
                params['channel_code'] = self.channel_code
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
        o = AlipayMerchantChannelCreateModel()
        if 'channel_code' in d:
            o.channel_code = d['channel_code']
        if 'channel_name' in d:
            o.channel_name = d['channel_name']
        return o


