#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StockShippingStepInfo(object):

    def __init__(self):
        self._event_address = None
        self._event_time = None
        self._ext_info = None
        self._status = None

    @property
    def event_address(self):
        return self._event_address

    @event_address.setter
    def event_address(self, value):
        self._event_address = value
    @property
    def event_time(self):
        return self._event_time

    @event_time.setter
    def event_time(self, value):
        self._event_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.event_address:
            if hasattr(self.event_address, 'to_alipay_dict'):
                params['event_address'] = self.event_address.to_alipay_dict()
            else:
                params['event_address'] = self.event_address
        if self.event_time:
            if hasattr(self.event_time, 'to_alipay_dict'):
                params['event_time'] = self.event_time.to_alipay_dict()
            else:
                params['event_time'] = self.event_time
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StockShippingStepInfo()
        if 'event_address' in d:
            o.event_address = d['event_address']
        if 'event_time' in d:
            o.event_time = d['event_time']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'status' in d:
            o.status = d['status']
        return o


