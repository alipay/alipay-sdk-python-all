#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RankCar(object):

    def __init__(self):
        self._car_id = None
        self._car_name = None
        self._data_name = None
        self._data_value = None

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
    def data_name(self):
        return self._data_name

    @data_name.setter
    def data_name(self, value):
        self._data_name = value
    @property
    def data_value(self):
        return self._data_value

    @data_value.setter
    def data_value(self, value):
        self._data_value = value


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
        if self.data_name:
            if hasattr(self.data_name, 'to_alipay_dict'):
                params['data_name'] = self.data_name.to_alipay_dict()
            else:
                params['data_name'] = self.data_name
        if self.data_value:
            if hasattr(self.data_value, 'to_alipay_dict'):
                params['data_value'] = self.data_value.to_alipay_dict()
            else:
                params['data_value'] = self.data_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RankCar()
        if 'car_id' in d:
            o.car_id = d['car_id']
        if 'car_name' in d:
            o.car_name = d['car_name']
        if 'data_name' in d:
            o.data_name = d['data_name']
        if 'data_value' in d:
            o.data_value = d['data_value']
        return o


