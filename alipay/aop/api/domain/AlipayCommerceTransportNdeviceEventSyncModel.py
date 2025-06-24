#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportNdeviceEventSyncModel(object):

    def __init__(self):
        self._biz_event_identity = None
        self._biz_event_type = None
        self._channel = None
        self._sn = None

    @property
    def biz_event_identity(self):
        return self._biz_event_identity

    @biz_event_identity.setter
    def biz_event_identity(self, value):
        self._biz_event_identity = value
    @property
    def biz_event_type(self):
        return self._biz_event_type

    @biz_event_type.setter
    def biz_event_type(self, value):
        self._biz_event_type = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_event_identity:
            if hasattr(self.biz_event_identity, 'to_alipay_dict'):
                params['biz_event_identity'] = self.biz_event_identity.to_alipay_dict()
            else:
                params['biz_event_identity'] = self.biz_event_identity
        if self.biz_event_type:
            if hasattr(self.biz_event_type, 'to_alipay_dict'):
                params['biz_event_type'] = self.biz_event_type.to_alipay_dict()
            else:
                params['biz_event_type'] = self.biz_event_type
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportNdeviceEventSyncModel()
        if 'biz_event_identity' in d:
            o.biz_event_identity = d['biz_event_identity']
        if 'biz_event_type' in d:
            o.biz_event_type = d['biz_event_type']
        if 'channel' in d:
            o.channel = d['channel']
        if 'sn' in d:
            o.sn = d['sn']
        return o


