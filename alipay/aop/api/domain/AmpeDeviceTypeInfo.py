#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AmpeDeviceTypeInfo(object):

    def __init__(self):
        self._device_type = None
        self._device_type_desc = None

    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def device_type_desc(self):
        return self._device_type_desc

    @device_type_desc.setter
    def device_type_desc(self, value):
        self._device_type_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.device_type_desc:
            if hasattr(self.device_type_desc, 'to_alipay_dict'):
                params['device_type_desc'] = self.device_type_desc.to_alipay_dict()
            else:
                params['device_type_desc'] = self.device_type_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AmpeDeviceTypeInfo()
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'device_type_desc' in d:
            o.device_type_desc = d['device_type_desc']
        return o


