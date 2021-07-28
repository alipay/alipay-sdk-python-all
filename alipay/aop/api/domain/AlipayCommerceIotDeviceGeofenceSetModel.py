#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FenceEvent import FenceEvent


class AlipayCommerceIotDeviceGeofenceSetModel(object):

    def __init__(self):
        self._fence_event = None
        self._operation_type = None
        self._route_code = None

    @property
    def fence_event(self):
        return self._fence_event

    @fence_event.setter
    def fence_event(self, value):
        if isinstance(value, FenceEvent):
            self._fence_event = value
        else:
            self._fence_event = FenceEvent.from_alipay_dict(value)
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def route_code(self):
        return self._route_code

    @route_code.setter
    def route_code(self, value):
        self._route_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.fence_event:
            if hasattr(self.fence_event, 'to_alipay_dict'):
                params['fence_event'] = self.fence_event.to_alipay_dict()
            else:
                params['fence_event'] = self.fence_event
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.route_code:
            if hasattr(self.route_code, 'to_alipay_dict'):
                params['route_code'] = self.route_code.to_alipay_dict()
            else:
                params['route_code'] = self.route_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotDeviceGeofenceSetModel()
        if 'fence_event' in d:
            o.fence_event = d['fence_event']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'route_code' in d:
            o.route_code = d['route_code']
        return o


