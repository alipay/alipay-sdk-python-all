#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentMobileLeads(object):

    def __init__(self):
        self._call_duration = None
        self._call_id = None
        self._callback_url = None
        self._caller_number = None
        self._connected = None
        self._record_url = None

    @property
    def call_duration(self):
        return self._call_duration

    @call_duration.setter
    def call_duration(self, value):
        self._call_duration = value
    @property
    def call_id(self):
        return self._call_id

    @call_id.setter
    def call_id(self, value):
        self._call_id = value
    @property
    def callback_url(self):
        return self._callback_url

    @callback_url.setter
    def callback_url(self, value):
        self._callback_url = value
    @property
    def caller_number(self):
        return self._caller_number

    @caller_number.setter
    def caller_number(self, value):
        self._caller_number = value
    @property
    def connected(self):
        return self._connected

    @connected.setter
    def connected(self, value):
        self._connected = value
    @property
    def record_url(self):
        return self._record_url

    @record_url.setter
    def record_url(self, value):
        self._record_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.call_duration:
            if hasattr(self.call_duration, 'to_alipay_dict'):
                params['call_duration'] = self.call_duration.to_alipay_dict()
            else:
                params['call_duration'] = self.call_duration
        if self.call_id:
            if hasattr(self.call_id, 'to_alipay_dict'):
                params['call_id'] = self.call_id.to_alipay_dict()
            else:
                params['call_id'] = self.call_id
        if self.callback_url:
            if hasattr(self.callback_url, 'to_alipay_dict'):
                params['callback_url'] = self.callback_url.to_alipay_dict()
            else:
                params['callback_url'] = self.callback_url
        if self.caller_number:
            if hasattr(self.caller_number, 'to_alipay_dict'):
                params['caller_number'] = self.caller_number.to_alipay_dict()
            else:
                params['caller_number'] = self.caller_number
        if self.connected:
            if hasattr(self.connected, 'to_alipay_dict'):
                params['connected'] = self.connected.to_alipay_dict()
            else:
                params['connected'] = self.connected
        if self.record_url:
            if hasattr(self.record_url, 'to_alipay_dict'):
                params['record_url'] = self.record_url.to_alipay_dict()
            else:
                params['record_url'] = self.record_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentMobileLeads()
        if 'call_duration' in d:
            o.call_duration = d['call_duration']
        if 'call_id' in d:
            o.call_id = d['call_id']
        if 'callback_url' in d:
            o.callback_url = d['callback_url']
        if 'caller_number' in d:
            o.caller_number = d['caller_number']
        if 'connected' in d:
            o.connected = d['connected']
        if 'record_url' in d:
            o.record_url = d['record_url']
        return o


