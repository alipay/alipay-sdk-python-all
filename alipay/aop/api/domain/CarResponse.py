#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CarResponse(object):

    def __init__(self):
        self._car_brand = None
        self._plate_no = None
        self._vehicle_type = None
        self._vin = None

    @property
    def car_brand(self):
        return self._car_brand

    @car_brand.setter
    def car_brand(self, value):
        self._car_brand = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value
    @property
    def vehicle_type(self):
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value):
        self._vehicle_type = value
    @property
    def vin(self):
        return self._vin

    @vin.setter
    def vin(self, value):
        self._vin = value


    def to_alipay_dict(self):
        params = dict()
        if self.car_brand:
            if hasattr(self.car_brand, 'to_alipay_dict'):
                params['car_brand'] = self.car_brand.to_alipay_dict()
            else:
                params['car_brand'] = self.car_brand
        if self.plate_no:
            if hasattr(self.plate_no, 'to_alipay_dict'):
                params['plate_no'] = self.plate_no.to_alipay_dict()
            else:
                params['plate_no'] = self.plate_no
        if self.vehicle_type:
            if hasattr(self.vehicle_type, 'to_alipay_dict'):
                params['vehicle_type'] = self.vehicle_type.to_alipay_dict()
            else:
                params['vehicle_type'] = self.vehicle_type
        if self.vin:
            if hasattr(self.vin, 'to_alipay_dict'):
                params['vin'] = self.vin.to_alipay_dict()
            else:
                params['vin'] = self.vin
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarResponse()
        if 'car_brand' in d:
            o.car_brand = d['car_brand']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'vehicle_type' in d:
            o.vehicle_type = d['vehicle_type']
        if 'vin' in d:
            o.vin = d['vin']
        return o


