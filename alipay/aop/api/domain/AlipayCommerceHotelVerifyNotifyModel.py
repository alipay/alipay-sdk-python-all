#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceHotelVerifyNotifyModel(object):

    def __init__(self):
        self._device_id = None
        self._device_platform = None
        self._hotel_code = None
        self._hotel_group_code = None
        self._name = None
        self._phone = None
        self._verify_id = None

    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
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
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def verify_id(self):
        return self._verify_id

    @verify_id.setter
    def verify_id(self, value):
        self._verify_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
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
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.verify_id:
            if hasattr(self.verify_id, 'to_alipay_dict'):
                params['verify_id'] = self.verify_id.to_alipay_dict()
            else:
                params['verify_id'] = self.verify_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceHotelVerifyNotifyModel()
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_platform' in d:
            o.device_platform = d['device_platform']
        if 'hotel_code' in d:
            o.hotel_code = d['hotel_code']
        if 'hotel_group_code' in d:
            o.hotel_group_code = d['hotel_group_code']
        if 'name' in d:
            o.name = d['name']
        if 'phone' in d:
            o.phone = d['phone']
        if 'verify_id' in d:
            o.verify_id = d['verify_id']
        return o


