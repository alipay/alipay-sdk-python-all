#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommercePropertyDeviceDeleteModel(object):

    def __init__(self):
        self._device_id = None
        self._out_device_id = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def out_device_id(self):
        return self._out_device_id

    @out_device_id.setter
    def out_device_id(self, value):
        self._out_device_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.out_device_id:
            if hasattr(self.out_device_id, 'to_alipay_dict'):
                params['out_device_id'] = self.out_device_id.to_alipay_dict()
            else:
                params['out_device_id'] = self.out_device_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommercePropertyDeviceDeleteModel()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'out_device_id' in d:
            o.out_device_id = d['out_device_id']
        return o


