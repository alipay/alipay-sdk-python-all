#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarViolationCityPushModel(object):

    def __init__(self):
        self._city_code = None
        self._push_type = None
        self._service_status = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def push_type(self):
        return self._push_type

    @push_type.setter
    def push_type(self, value):
        self._push_type = value
    @property
    def service_status(self):
        return self._service_status

    @service_status.setter
    def service_status(self, value):
        self._service_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.push_type:
            if hasattr(self.push_type, 'to_alipay_dict'):
                params['push_type'] = self.push_type.to_alipay_dict()
            else:
                params['push_type'] = self.push_type
        if self.service_status:
            if hasattr(self.service_status, 'to_alipay_dict'):
                params['service_status'] = self.service_status.to_alipay_dict()
            else:
                params['service_status'] = self.service_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarViolationCityPushModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'push_type' in d:
            o.push_type = d['push_type']
        if 'service_status' in d:
            o.service_status = d['service_status']
        return o


