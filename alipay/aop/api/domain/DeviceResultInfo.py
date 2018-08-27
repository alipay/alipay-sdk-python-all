#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DeviceResultInfo(object):

    def __init__(self):
        self._device_id = None
        self._device_label = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_label(self):
        return self._device_label

    @device_label.setter
    def device_label(self, value):
        self._device_label = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.device_label:
            if hasattr(self.device_label, 'to_alipay_dict'):
                params['device_label'] = self.device_label.to_alipay_dict()
            else:
                params['device_label'] = self.device_label
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeviceResultInfo()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_label' in d:
            o.device_label = d['device_label']
        return o


