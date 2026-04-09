#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OutletInfo(object):

    def __init__(self):
        self._insurance_direct_payment = None
        self._outlet_address = None
        self._outlet_code = None
        self._outlet_distance = None
        self._outlet_latitude = None
        self._outlet_longitude = None
        self._outlet_name = None
        self._outlet_phone = None
        self._outlet_time = None

    @property
    def insurance_direct_payment(self):
        return self._insurance_direct_payment

    @insurance_direct_payment.setter
    def insurance_direct_payment(self, value):
        self._insurance_direct_payment = value
    @property
    def outlet_address(self):
        return self._outlet_address

    @outlet_address.setter
    def outlet_address(self, value):
        self._outlet_address = value
    @property
    def outlet_code(self):
        return self._outlet_code

    @outlet_code.setter
    def outlet_code(self, value):
        self._outlet_code = value
    @property
    def outlet_distance(self):
        return self._outlet_distance

    @outlet_distance.setter
    def outlet_distance(self, value):
        self._outlet_distance = value
    @property
    def outlet_latitude(self):
        return self._outlet_latitude

    @outlet_latitude.setter
    def outlet_latitude(self, value):
        self._outlet_latitude = value
    @property
    def outlet_longitude(self):
        return self._outlet_longitude

    @outlet_longitude.setter
    def outlet_longitude(self, value):
        self._outlet_longitude = value
    @property
    def outlet_name(self):
        return self._outlet_name

    @outlet_name.setter
    def outlet_name(self, value):
        self._outlet_name = value
    @property
    def outlet_phone(self):
        return self._outlet_phone

    @outlet_phone.setter
    def outlet_phone(self, value):
        self._outlet_phone = value
    @property
    def outlet_time(self):
        return self._outlet_time

    @outlet_time.setter
    def outlet_time(self, value):
        self._outlet_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.insurance_direct_payment:
            if hasattr(self.insurance_direct_payment, 'to_alipay_dict'):
                params['insurance_direct_payment'] = self.insurance_direct_payment.to_alipay_dict()
            else:
                params['insurance_direct_payment'] = self.insurance_direct_payment
        if self.outlet_address:
            if hasattr(self.outlet_address, 'to_alipay_dict'):
                params['outlet_address'] = self.outlet_address.to_alipay_dict()
            else:
                params['outlet_address'] = self.outlet_address
        if self.outlet_code:
            if hasattr(self.outlet_code, 'to_alipay_dict'):
                params['outlet_code'] = self.outlet_code.to_alipay_dict()
            else:
                params['outlet_code'] = self.outlet_code
        if self.outlet_distance:
            if hasattr(self.outlet_distance, 'to_alipay_dict'):
                params['outlet_distance'] = self.outlet_distance.to_alipay_dict()
            else:
                params['outlet_distance'] = self.outlet_distance
        if self.outlet_latitude:
            if hasattr(self.outlet_latitude, 'to_alipay_dict'):
                params['outlet_latitude'] = self.outlet_latitude.to_alipay_dict()
            else:
                params['outlet_latitude'] = self.outlet_latitude
        if self.outlet_longitude:
            if hasattr(self.outlet_longitude, 'to_alipay_dict'):
                params['outlet_longitude'] = self.outlet_longitude.to_alipay_dict()
            else:
                params['outlet_longitude'] = self.outlet_longitude
        if self.outlet_name:
            if hasattr(self.outlet_name, 'to_alipay_dict'):
                params['outlet_name'] = self.outlet_name.to_alipay_dict()
            else:
                params['outlet_name'] = self.outlet_name
        if self.outlet_phone:
            if hasattr(self.outlet_phone, 'to_alipay_dict'):
                params['outlet_phone'] = self.outlet_phone.to_alipay_dict()
            else:
                params['outlet_phone'] = self.outlet_phone
        if self.outlet_time:
            if hasattr(self.outlet_time, 'to_alipay_dict'):
                params['outlet_time'] = self.outlet_time.to_alipay_dict()
            else:
                params['outlet_time'] = self.outlet_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OutletInfo()
        if 'insurance_direct_payment' in d:
            o.insurance_direct_payment = d['insurance_direct_payment']
        if 'outlet_address' in d:
            o.outlet_address = d['outlet_address']
        if 'outlet_code' in d:
            o.outlet_code = d['outlet_code']
        if 'outlet_distance' in d:
            o.outlet_distance = d['outlet_distance']
        if 'outlet_latitude' in d:
            o.outlet_latitude = d['outlet_latitude']
        if 'outlet_longitude' in d:
            o.outlet_longitude = d['outlet_longitude']
        if 'outlet_name' in d:
            o.outlet_name = d['outlet_name']
        if 'outlet_phone' in d:
            o.outlet_phone = d['outlet_phone']
        if 'outlet_time' in d:
            o.outlet_time = d['outlet_time']
        return o


