#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceHotelDeviceInfoAddModel(object):

    def __init__(self):
        self._device_id = None
        self._device_open_id = None
        self._device_platform = None
        self._hotel_code = None
        self._hotel_group_code = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_open_id(self):
        return self._device_open_id

    @device_open_id.setter
    def device_open_id(self, value):
        self._device_open_id = value
    @property
    def device_platform(self):
        return self._device_platform

    @device_platform.setter
    def device_platform(self, value):
        self._device_platform = value
    @property
    def hotel_code(self):
        return self._hotel_code

    @hotel_code.setter
    def hotel_code(self, value):
        self._hotel_code = value
    @property
    def hotel_group_code(self):
        return self._hotel_group_code

    @hotel_group_code.setter
    def hotel_group_code(self, value):
        self._hotel_group_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.device_open_id:
            if hasattr(self.device_open_id, 'to_alipay_dict'):
                params['device_open_id'] = self.device_open_id.to_alipay_dict()
            else:
                params['device_open_id'] = self.device_open_id
        if self.device_platform:
            if hasattr(self.device_platform, 'to_alipay_dict'):
                params['device_platform'] = self.device_platform.to_alipay_dict()
            else:
                params['device_platform'] = self.device_platform
        if self.hotel_code:
            if hasattr(self.hotel_code, 'to_alipay_dict'):
                params['hotel_code'] = self.hotel_code.to_alipay_dict()
            else:
                params['hotel_code'] = self.hotel_code
        if self.hotel_group_code:
            if hasattr(self.hotel_group_code, 'to_alipay_dict'):
                params['hotel_group_code'] = self.hotel_group_code.to_alipay_dict()
            else:
                params['hotel_group_code'] = self.hotel_group_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceHotelDeviceInfoAddModel()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_open_id' in d:
            o.device_open_id = d['device_open_id']
        if 'device_platform' in d:
            o.device_platform = d['device_platform']
        if 'hotel_code' in d:
            o.hotel_code = d['hotel_code']
        if 'hotel_group_code' in d:
            o.hotel_group_code = d['hotel_group_code']
        return o


