#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ParkingScene(object):

    def __init__(self):
        self._car_number = None
        self._in_time = None
        self._parking_id = None
        self._parking_name = None

    @property
    def car_number(self):
        return self._car_number

    @car_number.setter
    def car_number(self, value):
        self._car_number = value
    @property
    def in_time(self):
        return self._in_time

    @in_time.setter
    def in_time(self, value):
        self._in_time = value
    @property
    def parking_id(self):
        return self._parking_id

    @parking_id.setter
    def parking_id(self, value):
        self._parking_id = value
    @property
    def parking_name(self):
        return self._parking_name

    @parking_name.setter
    def parking_name(self, value):
        self._parking_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.car_number:
            if hasattr(self.car_number, 'to_alipay_dict'):
                params['car_number'] = self.car_number.to_alipay_dict()
            else:
                params['car_number'] = self.car_number
        if self.in_time:
            if hasattr(self.in_time, 'to_alipay_dict'):
                params['in_time'] = self.in_time.to_alipay_dict()
            else:
                params['in_time'] = self.in_time
        if self.parking_id:
            if hasattr(self.parking_id, 'to_alipay_dict'):
                params['parking_id'] = self.parking_id.to_alipay_dict()
            else:
                params['parking_id'] = self.parking_id
        if self.parking_name:
            if hasattr(self.parking_name, 'to_alipay_dict'):
                params['parking_name'] = self.parking_name.to_alipay_dict()
            else:
                params['parking_name'] = self.parking_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ParkingScene()
        if 'car_number' in d:
            o.car_number = d['car_number']
        if 'in_time' in d:
            o.in_time = d['in_time']
        if 'parking_id' in d:
            o.parking_id = d['parking_id']
        if 'parking_name' in d:
            o.parking_name = d['parking_name']
        return o


