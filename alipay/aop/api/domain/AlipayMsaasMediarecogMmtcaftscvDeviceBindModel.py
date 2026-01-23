#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMsaasMediarecogMmtcaftscvDeviceBindModel(object):

    def __init__(self):
        self._device_id = None
        self._dynamic_device = None
        self._isv_pid = None
        self._isv_tid = None
        self._register_type = None
        self._weight_device = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def dynamic_device(self):
        return self._dynamic_device

    @dynamic_device.setter
    def dynamic_device(self, value):
        self._dynamic_device = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def isv_tid(self):
        return self._isv_tid

    @isv_tid.setter
    def isv_tid(self, value):
        self._isv_tid = value
    @property
    def register_type(self):
        return self._register_type

    @register_type.setter
    def register_type(self, value):
        self._register_type = value
    @property
    def weight_device(self):
        return self._weight_device

    @weight_device.setter
    def weight_device(self, value):
        self._weight_device = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.dynamic_device:
            if hasattr(self.dynamic_device, 'to_alipay_dict'):
                params['dynamic_device'] = self.dynamic_device.to_alipay_dict()
            else:
                params['dynamic_device'] = self.dynamic_device
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.isv_tid:
            if hasattr(self.isv_tid, 'to_alipay_dict'):
                params['isv_tid'] = self.isv_tid.to_alipay_dict()
            else:
                params['isv_tid'] = self.isv_tid
        if self.register_type:
            if hasattr(self.register_type, 'to_alipay_dict'):
                params['register_type'] = self.register_type.to_alipay_dict()
            else:
                params['register_type'] = self.register_type
        if self.weight_device:
            if hasattr(self.weight_device, 'to_alipay_dict'):
                params['weight_device'] = self.weight_device.to_alipay_dict()
            else:
                params['weight_device'] = self.weight_device
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogMmtcaftscvDeviceBindModel()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'dynamic_device' in d:
            o.dynamic_device = d['dynamic_device']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'isv_tid' in d:
            o.isv_tid = d['isv_tid']
        if 'register_type' in d:
            o.register_type = d['register_type']
        if 'weight_device' in d:
            o.weight_device = d['weight_device']
        return o


