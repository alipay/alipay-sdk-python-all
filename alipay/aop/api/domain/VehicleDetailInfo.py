#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VehicleDetailInfo(object):

    def __init__(self):
        self._car_code = None
        self._car_image = None
        self._car_label = None
        self._car_level = None
        self._car_model_id = None
        self._lable = None
        self._name = None
        self._vehicle_color = None
        self._vehicle_license = None
        self._vehicle_make = None

    @property
    def car_code(self):
        return self._car_code

    @car_code.setter
    def car_code(self, value):
        self._car_code = value
    @property
    def car_image(self):
        return self._car_image

    @car_image.setter
    def car_image(self, value):
        self._car_image = value
    @property
    def car_label(self):
        return self._car_label

    @car_label.setter
    def car_label(self, value):
        self._car_label = value
    @property
    def car_level(self):
        return self._car_level

    @car_level.setter
    def car_level(self, value):
        self._car_level = value
    @property
    def car_model_id(self):
        return self._car_model_id

    @car_model_id.setter
    def car_model_id(self, value):
        self._car_model_id = value
    @property
    def lable(self):
        return self._lable

    @lable.setter
    def lable(self, value):
        self._lable = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def vehicle_color(self):
        return self._vehicle_color

    @vehicle_color.setter
    def vehicle_color(self, value):
        self._vehicle_color = value
    @property
    def vehicle_license(self):
        return self._vehicle_license

    @vehicle_license.setter
    def vehicle_license(self, value):
        self._vehicle_license = value
    @property
    def vehicle_make(self):
        return self._vehicle_make

    @vehicle_make.setter
    def vehicle_make(self, value):
        self._vehicle_make = value


    def to_alipay_dict(self):
        params = dict()
        if self.car_code:
            if hasattr(self.car_code, 'to_alipay_dict'):
                params['car_code'] = self.car_code.to_alipay_dict()
            else:
                params['car_code'] = self.car_code
        if self.car_image:
            if hasattr(self.car_image, 'to_alipay_dict'):
                params['car_image'] = self.car_image.to_alipay_dict()
            else:
                params['car_image'] = self.car_image
        if self.car_label:
            if hasattr(self.car_label, 'to_alipay_dict'):
                params['car_label'] = self.car_label.to_alipay_dict()
            else:
                params['car_label'] = self.car_label
        if self.car_level:
            if hasattr(self.car_level, 'to_alipay_dict'):
                params['car_level'] = self.car_level.to_alipay_dict()
            else:
                params['car_level'] = self.car_level
        if self.car_model_id:
            if hasattr(self.car_model_id, 'to_alipay_dict'):
                params['car_model_id'] = self.car_model_id.to_alipay_dict()
            else:
                params['car_model_id'] = self.car_model_id
        if self.lable:
            if hasattr(self.lable, 'to_alipay_dict'):
                params['lable'] = self.lable.to_alipay_dict()
            else:
                params['lable'] = self.lable
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.vehicle_color:
            if hasattr(self.vehicle_color, 'to_alipay_dict'):
                params['vehicle_color'] = self.vehicle_color.to_alipay_dict()
            else:
                params['vehicle_color'] = self.vehicle_color
        if self.vehicle_license:
            if hasattr(self.vehicle_license, 'to_alipay_dict'):
                params['vehicle_license'] = self.vehicle_license.to_alipay_dict()
            else:
                params['vehicle_license'] = self.vehicle_license
        if self.vehicle_make:
            if hasattr(self.vehicle_make, 'to_alipay_dict'):
                params['vehicle_make'] = self.vehicle_make.to_alipay_dict()
            else:
                params['vehicle_make'] = self.vehicle_make
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VehicleDetailInfo()
        if 'car_code' in d:
            o.car_code = d['car_code']
        if 'car_image' in d:
            o.car_image = d['car_image']
        if 'car_label' in d:
            o.car_label = d['car_label']
        if 'car_level' in d:
            o.car_level = d['car_level']
        if 'car_model_id' in d:
            o.car_model_id = d['car_model_id']
        if 'lable' in d:
            o.lable = d['lable']
        if 'name' in d:
            o.name = d['name']
        if 'vehicle_color' in d:
            o.vehicle_color = d['vehicle_color']
        if 'vehicle_license' in d:
            o.vehicle_license = d['vehicle_license']
        if 'vehicle_make' in d:
            o.vehicle_make = d['vehicle_make']
        return o


