#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeliveryConfig(object):

    def __init__(self):
        self._activity_id = None
        self._booth_code = None
        self._channel = None

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, value):
        self._activity_id = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.activity_id:
            if hasattr(self.activity_id, 'to_alipay_dict'):
                params['activity_id'] = self.activity_id.to_alipay_dict()
            else:
                params['activity_id'] = self.activity_id
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryConfig()
        if 'activity_id' in d:
            o.activity_id = d['activity_id']
        if 'booth_code' in d:
            o.booth_code = d['booth_code']
        if 'channel' in d:
            o.channel = d['channel']
        return o


