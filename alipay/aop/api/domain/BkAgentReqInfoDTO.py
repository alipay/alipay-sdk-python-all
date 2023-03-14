#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BkAgentReqInfoDTO(object):

    def __init__(self):
        self._acq_code = None
        self._device_type = None
        self._location = None
        self._merch_code = None
        self._serial_num = None

    @property
    def acq_code(self):
        return self._acq_code

    @acq_code.setter
    def acq_code(self, value):
        self._acq_code = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value
    @property
    def merch_code(self):
        return self._merch_code

    @merch_code.setter
    def merch_code(self, value):
        self._merch_code = value
    @property
    def serial_num(self):
        return self._serial_num

    @serial_num.setter
    def serial_num(self, value):
        self._serial_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.acq_code:
            if hasattr(self.acq_code, 'to_alipay_dict'):
                params['acq_code'] = self.acq_code.to_alipay_dict()
            else:
                params['acq_code'] = self.acq_code
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.location:
            if hasattr(self.location, 'to_alipay_dict'):
                params['location'] = self.location.to_alipay_dict()
            else:
                params['location'] = self.location
        if self.merch_code:
            if hasattr(self.merch_code, 'to_alipay_dict'):
                params['merch_code'] = self.merch_code.to_alipay_dict()
            else:
                params['merch_code'] = self.merch_code
        if self.serial_num:
            if hasattr(self.serial_num, 'to_alipay_dict'):
                params['serial_num'] = self.serial_num.to_alipay_dict()
            else:
                params['serial_num'] = self.serial_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BkAgentReqInfoDTO()
        if 'acq_code' in d:
            o.acq_code = d['acq_code']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'location' in d:
            o.location = d['location']
        if 'merch_code' in d:
            o.merch_code = d['merch_code']
        if 'serial_num' in d:
            o.serial_num = d['serial_num']
        return o


