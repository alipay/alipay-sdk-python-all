#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WelfareAuthExtReq(object):

    def __init__(self):
        self._from_channel = None

    @property
    def from_channel(self):
        return self._from_channel

    @from_channel.setter
    def from_channel(self, value):
        self._from_channel = value


    def to_alipay_dict(self):
        params = dict()
        if self.from_channel:
            if hasattr(self.from_channel, 'to_alipay_dict'):
                params['from_channel'] = self.from_channel.to_alipay_dict()
            else:
                params['from_channel'] = self.from_channel
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WelfareAuthExtReq()
        if 'from_channel' in d:
            o.from_channel = d['from_channel']
        return o


