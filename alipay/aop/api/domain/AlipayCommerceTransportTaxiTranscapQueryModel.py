#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportTaxiTranscapQueryModel(object):

    def __init__(self):
        self._car_no = None
        self._city_code = None
        self._request_id = None
        self._request_time = None
        self._vehicle_id = None

    @property
    def car_no(self):
        return self._car_no

    @car_no.setter
    def car_no(self, value):
        self._car_no = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def request_time(self):
        return self._request_time

    @request_time.setter
    def request_time(self, value):
        self._request_time = value
    @property
    def vehicle_id(self):
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, value):
        self._vehicle_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.car_no:
            if hasattr(self.car_no, 'to_alipay_dict'):
                params['car_no'] = self.car_no.to_alipay_dict()
            else:
                params['car_no'] = self.car_no
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.request_time:
            if hasattr(self.request_time, 'to_alipay_dict'):
                params['request_time'] = self.request_time.to_alipay_dict()
            else:
                params['request_time'] = self.request_time
        if self.vehicle_id:
            if hasattr(self.vehicle_id, 'to_alipay_dict'):
                params['vehicle_id'] = self.vehicle_id.to_alipay_dict()
            else:
                params['vehicle_id'] = self.vehicle_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportTaxiTranscapQueryModel()
        if 'car_no' in d:
            o.car_no = d['car_no']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'request_time' in d:
            o.request_time = d['request_time']
        if 'vehicle_id' in d:
            o.vehicle_id = d['vehicle_id']
        return o


