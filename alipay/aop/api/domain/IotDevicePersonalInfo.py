#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IotDevicePersonalInfo(object):

    def __init__(self):
        self._device_id = None
        self._remark = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IotDevicePersonalInfo()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'remark' in d:
            o.remark = d['remark']
        return o


