#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PropertyDeviceInfo(object):

    def __init__(self):
        self._device_id = None
        self._device_name = None
        self._device_type = None
        self._enable_status = None
        self._entrance_open_config = None
        self._entrance_open_type = None
        self._out_device_id = None
        self._support_open = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_name(self):
        return self._device_name

    @device_name.setter
    def device_name(self, value):
        self._device_name = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def enable_status(self):
        return self._enable_status

    @enable_status.setter
    def enable_status(self, value):
        self._enable_status = value
    @property
    def entrance_open_config(self):
        return self._entrance_open_config

    @entrance_open_config.setter
    def entrance_open_config(self, value):
        self._entrance_open_config = value
    @property
    def entrance_open_type(self):
        return self._entrance_open_type

    @entrance_open_type.setter
    def entrance_open_type(self, value):
        self._entrance_open_type = value
    @property
    def out_device_id(self):
        return self._out_device_id

    @out_device_id.setter
    def out_device_id(self, value):
        self._out_device_id = value
    @property
    def support_open(self):
        return self._support_open

    @support_open.setter
    def support_open(self, value):
        self._support_open = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.device_name:
            if hasattr(self.device_name, 'to_alipay_dict'):
                params['device_name'] = self.device_name.to_alipay_dict()
            else:
                params['device_name'] = self.device_name
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.enable_status:
            if hasattr(self.enable_status, 'to_alipay_dict'):
                params['enable_status'] = self.enable_status.to_alipay_dict()
            else:
                params['enable_status'] = self.enable_status
        if self.entrance_open_config:
            if hasattr(self.entrance_open_config, 'to_alipay_dict'):
                params['entrance_open_config'] = self.entrance_open_config.to_alipay_dict()
            else:
                params['entrance_open_config'] = self.entrance_open_config
        if self.entrance_open_type:
            if hasattr(self.entrance_open_type, 'to_alipay_dict'):
                params['entrance_open_type'] = self.entrance_open_type.to_alipay_dict()
            else:
                params['entrance_open_type'] = self.entrance_open_type
        if self.out_device_id:
            if hasattr(self.out_device_id, 'to_alipay_dict'):
                params['out_device_id'] = self.out_device_id.to_alipay_dict()
            else:
                params['out_device_id'] = self.out_device_id
        if self.support_open:
            if hasattr(self.support_open, 'to_alipay_dict'):
                params['support_open'] = self.support_open.to_alipay_dict()
            else:
                params['support_open'] = self.support_open
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PropertyDeviceInfo()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_name' in d:
            o.device_name = d['device_name']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'enable_status' in d:
            o.enable_status = d['enable_status']
        if 'entrance_open_config' in d:
            o.entrance_open_config = d['entrance_open_config']
        if 'entrance_open_type' in d:
            o.entrance_open_type = d['entrance_open_type']
        if 'out_device_id' in d:
            o.out_device_id = d['out_device_id']
        if 'support_open' in d:
            o.support_open = d['support_open']
        return o


