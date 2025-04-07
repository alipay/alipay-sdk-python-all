#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DetectEvent import DetectEvent


class AlipayCommercePropertyRiskdetectEventSubscribeModel(object):

    def __init__(self):
        self._active_status = None
        self._out_device_id = None
        self._register_events = None

    @property
    def active_status(self):
        return self._active_status

    @active_status.setter
    def active_status(self, value):
        self._active_status = value
    @property
    def out_device_id(self):
        return self._out_device_id

    @out_device_id.setter
    def out_device_id(self, value):
        self._out_device_id = value
    @property
    def register_events(self):
        return self._register_events

    @register_events.setter
    def register_events(self, value):
        if isinstance(value, list):
            self._register_events = list()
            for i in value:
                if isinstance(i, DetectEvent):
                    self._register_events.append(i)
                else:
                    self._register_events.append(DetectEvent.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.active_status:
            if hasattr(self.active_status, 'to_alipay_dict'):
                params['active_status'] = self.active_status.to_alipay_dict()
            else:
                params['active_status'] = self.active_status
        if self.out_device_id:
            if hasattr(self.out_device_id, 'to_alipay_dict'):
                params['out_device_id'] = self.out_device_id.to_alipay_dict()
            else:
                params['out_device_id'] = self.out_device_id
        if self.register_events:
            if isinstance(self.register_events, list):
                for i in range(0, len(self.register_events)):
                    element = self.register_events[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.register_events[i] = element.to_alipay_dict()
            if hasattr(self.register_events, 'to_alipay_dict'):
                params['register_events'] = self.register_events.to_alipay_dict()
            else:
                params['register_events'] = self.register_events
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommercePropertyRiskdetectEventSubscribeModel()
        if 'active_status' in d:
            o.active_status = d['active_status']
        if 'out_device_id' in d:
            o.out_device_id = d['out_device_id']
        if 'register_events' in d:
            o.register_events = d['register_events']
        return o


