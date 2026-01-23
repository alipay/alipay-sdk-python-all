#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TrafficshareCrowdUserSync(object):

    def __init__(self):
        self._add_increment_flag = None
        self._device_number = None
        self._operation_type = None
        self._phone_number = None

    @property
    def add_increment_flag(self):
        return self._add_increment_flag

    @add_increment_flag.setter
    def add_increment_flag(self, value):
        self._add_increment_flag = value
    @property
    def device_number(self):
        return self._device_number

    @device_number.setter
    def device_number(self, value):
        self._device_number = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.add_increment_flag:
            if hasattr(self.add_increment_flag, 'to_alipay_dict'):
                params['add_increment_flag'] = self.add_increment_flag.to_alipay_dict()
            else:
                params['add_increment_flag'] = self.add_increment_flag
        if self.device_number:
            if hasattr(self.device_number, 'to_alipay_dict'):
                params['device_number'] = self.device_number.to_alipay_dict()
            else:
                params['device_number'] = self.device_number
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.phone_number:
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TrafficshareCrowdUserSync()
        if 'add_increment_flag' in d:
            o.add_increment_flag = d['add_increment_flag']
        if 'device_number' in d:
            o.device_number = d['device_number']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        return o


