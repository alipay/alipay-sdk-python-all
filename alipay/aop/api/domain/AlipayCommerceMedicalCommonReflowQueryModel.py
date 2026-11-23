#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalCommonReflowQueryModel(object):

    def __init__(self):
        self._channel = None
        self._mac_id = None
        self._order_id = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def mac_id(self):
        return self._mac_id

    @mac_id.setter
    def mac_id(self, value):
        self._mac_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.mac_id:
            if hasattr(self.mac_id, 'to_alipay_dict'):
                params['mac_id'] = self.mac_id.to_alipay_dict()
            else:
                params['mac_id'] = self.mac_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalCommonReflowQueryModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'mac_id' in d:
            o.mac_id = d['mac_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        return o


