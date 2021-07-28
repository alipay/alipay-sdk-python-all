#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CarRentalVehicleInfo(object):

    def __init__(self):
        self._car_no = None
        self._vehicle_capacity = None
        self._vehicle_color = None
        self._vehicle_models = None
        self._vehicle_number = None
        self._vehicle_operation_type = None
        self._vehicle_seats = None
        self._vehicle_type = None

    @property
    def car_no(self):
        return self._car_no

    @car_no.setter
    def car_no(self, value):
        self._car_no = value
    @property
    def vehicle_capacity(self):
        return self._vehicle_capacity

    @vehicle_capacity.setter
    def vehicle_capacity(self, value):
        self._vehicle_capacity = value
    @property
    def vehicle_color(self):
        return self._vehicle_color

    @vehicle_color.setter
    def vehicle_color(self, value):
        self._vehicle_color = value
    @property
    def vehicle_models(self):
        return self._vehicle_models

    @vehicle_models.setter
    def vehicle_models(self, value):
        self._vehicle_models = value
    @property
    def vehicle_number(self):
        return self._vehicle_number

    @vehicle_number.setter
    def vehicle_number(self, value):
        self._vehicle_number = value
    @property
    def vehicle_operation_type(self):
        return self._vehicle_operation_type

    @vehicle_operation_type.setter
    def vehicle_operation_type(self, value):
        self._vehicle_operation_type = value
    @property
    def vehicle_seats(self):
        return self._vehicle_seats

    @vehicle_seats.setter
    def vehicle_seats(self, value):
        self._vehicle_seats = value
    @property
    def vehicle_type(self):
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value):
        self._vehicle_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.car_no:
            if hasattr(self.car_no, 'to_alipay_dict'):
                params['car_no'] = self.car_no.to_alipay_dict()
            else:
                params['car_no'] = self.car_no
        if self.vehicle_capacity:
            if hasattr(self.vehicle_capacity, 'to_alipay_dict'):
                params['vehicle_capacity'] = self.vehicle_capacity.to_alipay_dict()
            else:
                params['vehicle_capacity'] = self.vehicle_capacity
        if self.vehicle_color:
            if hasattr(self.vehicle_color, 'to_alipay_dict'):
                params['vehicle_color'] = self.vehicle_color.to_alipay_dict()
            else:
                params['vehicle_color'] = self.vehicle_color
        if self.vehicle_models:
            if hasattr(self.vehicle_models, 'to_alipay_dict'):
                params['vehicle_models'] = self.vehicle_models.to_alipay_dict()
            else:
                params['vehicle_models'] = self.vehicle_models
        if self.vehicle_number:
            if hasattr(self.vehicle_number, 'to_alipay_dict'):
                params['vehicle_number'] = self.vehicle_number.to_alipay_dict()
            else:
                params['vehicle_number'] = self.vehicle_number
        if self.vehicle_operation_type:
            if hasattr(self.vehicle_operation_type, 'to_alipay_dict'):
                params['vehicle_operation_type'] = self.vehicle_operation_type.to_alipay_dict()
            else:
                params['vehicle_operation_type'] = self.vehicle_operation_type
        if self.vehicle_seats:
            if hasattr(self.vehicle_seats, 'to_alipay_dict'):
                params['vehicle_seats'] = self.vehicle_seats.to_alipay_dict()
            else:
                params['vehicle_seats'] = self.vehicle_seats
        if self.vehicle_type:
            if hasattr(self.vehicle_type, 'to_alipay_dict'):
                params['vehicle_type'] = self.vehicle_type.to_alipay_dict()
            else:
                params['vehicle_type'] = self.vehicle_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarRentalVehicleInfo()
        if 'car_no' in d:
            o.car_no = d['car_no']
        if 'vehicle_capacity' in d:
            o.vehicle_capacity = d['vehicle_capacity']
        if 'vehicle_color' in d:
            o.vehicle_color = d['vehicle_color']
        if 'vehicle_models' in d:
            o.vehicle_models = d['vehicle_models']
        if 'vehicle_number' in d:
            o.vehicle_number = d['vehicle_number']
        if 'vehicle_operation_type' in d:
            o.vehicle_operation_type = d['vehicle_operation_type']
        if 'vehicle_seats' in d:
            o.vehicle_seats = d['vehicle_seats']
        if 'vehicle_type' in d:
            o.vehicle_type = d['vehicle_type']
        return o


