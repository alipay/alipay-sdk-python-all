#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LeadsCarInfo(object):

    def __init__(self):
        self._car_id = None
        self._car_name = None
        self._car_type = None

    @property
    def car_id(self):
        return self._car_id

    @car_id.setter
    def car_id(self, value):
        self._car_id = value
    @property
    def car_name(self):
        return self._car_name

    @car_name.setter
    def car_name(self, value):
        self._car_name = value
    @property
    def car_type(self):
        return self._car_type

    @car_type.setter
    def car_type(self, value):
        self._car_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.car_id:
            if hasattr(self.car_id, 'to_alipay_dict'):
                params['car_id'] = self.car_id.to_alipay_dict()
            else:
                params['car_id'] = self.car_id
        if self.car_name:
            if hasattr(self.car_name, 'to_alipay_dict'):
                params['car_name'] = self.car_name.to_alipay_dict()
            else:
                params['car_name'] = self.car_name
        if self.car_type:
            if hasattr(self.car_type, 'to_alipay_dict'):
                params['car_type'] = self.car_type.to_alipay_dict()
            else:
                params['car_type'] = self.car_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LeadsCarInfo()
        if 'car_id' in d:
            o.car_id = d['car_id']
        if 'car_name' in d:
            o.car_name = d['car_name']
        if 'car_type' in d:
            o.car_type = d['car_type']
        return o


