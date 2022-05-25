#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryAvailableCityCode import DeliveryAvailableCityCode


class DeliveryAvailableScope(object):

    def __init__(self):
        self._delivery_available_city_code = None
        self._delivery_available_scope_type = None

    @property
    def delivery_available_city_code(self):
        return self._delivery_available_city_code

    @delivery_available_city_code.setter
    def delivery_available_city_code(self, value):
        if isinstance(value, DeliveryAvailableCityCode):
            self._delivery_available_city_code = value
        else:
            self._delivery_available_city_code = DeliveryAvailableCityCode.from_alipay_dict(value)
    @property
    def delivery_available_scope_type(self):
        return self._delivery_available_scope_type

    @delivery_available_scope_type.setter
    def delivery_available_scope_type(self, value):
        self._delivery_available_scope_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_available_city_code:
            if hasattr(self.delivery_available_city_code, 'to_alipay_dict'):
                params['delivery_available_city_code'] = self.delivery_available_city_code.to_alipay_dict()
            else:
                params['delivery_available_city_code'] = self.delivery_available_city_code
        if self.delivery_available_scope_type:
            if hasattr(self.delivery_available_scope_type, 'to_alipay_dict'):
                params['delivery_available_scope_type'] = self.delivery_available_scope_type.to_alipay_dict()
            else:
                params['delivery_available_scope_type'] = self.delivery_available_scope_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryAvailableScope()
        if 'delivery_available_city_code' in d:
            o.delivery_available_city_code = d['delivery_available_city_code']
        if 'delivery_available_scope_type' in d:
            o.delivery_available_scope_type = d['delivery_available_scope_type']
        return o


