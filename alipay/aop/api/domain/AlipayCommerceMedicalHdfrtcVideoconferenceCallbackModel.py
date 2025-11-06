#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHdfrtcVideoconferenceCallbackModel(object):

    def __init__(self):
        self._event_data = None
        self._event_id = None
        self._event_type = None
        self._notify_time = None

    @property
    def event_data(self):
        return self._event_data

    @event_data.setter
    def event_data(self, value):
        self._event_data = value
    @property
    def event_id(self):
        return self._event_id

    @event_id.setter
    def event_id(self, value):
        self._event_id = value
    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def notify_time(self):
        return self._notify_time

    @notify_time.setter
    def notify_time(self, value):
        self._notify_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.event_data:
            if hasattr(self.event_data, 'to_alipay_dict'):
                params['event_data'] = self.event_data.to_alipay_dict()
            else:
                params['event_data'] = self.event_data
        if self.event_id:
            if hasattr(self.event_id, 'to_alipay_dict'):
                params['event_id'] = self.event_id.to_alipay_dict()
            else:
                params['event_id'] = self.event_id
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        if self.notify_time:
            if hasattr(self.notify_time, 'to_alipay_dict'):
                params['notify_time'] = self.notify_time.to_alipay_dict()
            else:
                params['notify_time'] = self.notify_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHdfrtcVideoconferenceCallbackModel()
        if 'event_data' in d:
            o.event_data = d['event_data']
        if 'event_id' in d:
            o.event_id = d['event_id']
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'notify_time' in d:
            o.notify_time = d['notify_time']
        return o


