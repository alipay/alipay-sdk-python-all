#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EtcDeviceCardCheckInfo(object):

    def __init__(self):
        self._error_desc = None
        self._error_handler = None
        self._error_type = None

    @property
    def error_desc(self):
        return self._error_desc

    @error_desc.setter
    def error_desc(self, value):
        self._error_desc = value
    @property
    def error_handler(self):
        return self._error_handler

    @error_handler.setter
    def error_handler(self, value):
        self._error_handler = value
    @property
    def error_type(self):
        return self._error_type

    @error_type.setter
    def error_type(self, value):
        self._error_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.error_desc:
            if hasattr(self.error_desc, 'to_alipay_dict'):
                params['error_desc'] = self.error_desc.to_alipay_dict()
            else:
                params['error_desc'] = self.error_desc
        if self.error_handler:
            if hasattr(self.error_handler, 'to_alipay_dict'):
                params['error_handler'] = self.error_handler.to_alipay_dict()
            else:
                params['error_handler'] = self.error_handler
        if self.error_type:
            if hasattr(self.error_type, 'to_alipay_dict'):
                params['error_type'] = self.error_type.to_alipay_dict()
            else:
                params['error_type'] = self.error_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EtcDeviceCardCheckInfo()
        if 'error_desc' in d:
            o.error_desc = d['error_desc']
        if 'error_handler' in d:
            o.error_handler = d['error_handler']
        if 'error_type' in d:
            o.error_type = d['error_type']
        return o


