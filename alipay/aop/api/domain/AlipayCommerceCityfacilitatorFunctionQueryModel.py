#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCityfacilitatorFunctionQueryModel(object):

    def __init__(self):
        self._city_code = None
        self._device_code = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def device_code(self):
        return self._device_code

    @device_code.setter
    def device_code(self, value):
        self._device_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.device_code:
            if hasattr(self.device_code, 'to_alipay_dict'):
                params['device_code'] = self.device_code.to_alipay_dict()
            else:
                params['device_code'] = self.device_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCityfacilitatorFunctionQueryModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'device_code' in d:
            o.device_code = d['device_code']
        return o


