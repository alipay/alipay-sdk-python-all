#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GateDeviceInfo(object):

    def __init__(self):
        self._gate_supplier_code = None
        self._sys_device_id = None

    @property
    def gate_supplier_code(self):
        return self._gate_supplier_code

    @gate_supplier_code.setter
    def gate_supplier_code(self, value):
        self._gate_supplier_code = value
    @property
    def sys_device_id(self):
        return self._sys_device_id

    @sys_device_id.setter
    def sys_device_id(self, value):
        self._sys_device_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.gate_supplier_code:
            if hasattr(self.gate_supplier_code, 'to_alipay_dict'):
                params['gate_supplier_code'] = self.gate_supplier_code.to_alipay_dict()
            else:
                params['gate_supplier_code'] = self.gate_supplier_code
        if self.sys_device_id:
            if hasattr(self.sys_device_id, 'to_alipay_dict'):
                params['sys_device_id'] = self.sys_device_id.to_alipay_dict()
            else:
                params['sys_device_id'] = self.sys_device_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GateDeviceInfo()
        if 'gate_supplier_code' in d:
            o.gate_supplier_code = d['gate_supplier_code']
        if 'sys_device_id' in d:
            o.sys_device_id = d['sys_device_id']
        return o


