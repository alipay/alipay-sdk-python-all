#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoMycarParkingVehicleQueryModel(object):

    def __init__(self):
        self._car_id = None

    @property
    def car_id(self):
        return self._car_id

    @car_id.setter
    def car_id(self, value):
        self._car_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.car_id:
            if hasattr(self.car_id, 'to_alipay_dict'):
                params['car_id'] = self.car_id.to_alipay_dict()
            else:
                params['car_id'] = self.car_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarParkingVehicleQueryModel()
        if 'car_id' in d:
            o.car_id = d['car_id']
        return o


