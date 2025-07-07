#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EtcDeviceMsgInfo import EtcDeviceMsgInfo


class AlipayCommerceTransportEtcDeivceinfoSendModel(object):

    def __init__(self):
        self._device_info = None
        self._event_type = None

    @property
    def device_info(self):
        return self._device_info

    @device_info.setter
    def device_info(self, value):
        if isinstance(value, EtcDeviceMsgInfo):
            self._device_info = value
        else:
            self._device_info = EtcDeviceMsgInfo.from_alipay_dict(value)
    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_info:
            if hasattr(self.device_info, 'to_alipay_dict'):
                params['device_info'] = self.device_info.to_alipay_dict()
            else:
                params['device_info'] = self.device_info
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEtcDeivceinfoSendModel()
        if 'device_info' in d:
            o.device_info = d['device_info']
        if 'event_type' in d:
            o.event_type = d['event_type']
        return o


