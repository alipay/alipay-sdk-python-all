#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsOpenVehicleDTO(object):

    def __init__(self):
        self._vehicle_brand = None
        self._vehicle_frame_no = None
        self._vehicle_no = None
        self._vehicle_registration = None
        self._vehicle_type = None

    @property
    def vehicle_brand(self):
        return self._vehicle_brand

    @vehicle_brand.setter
    def vehicle_brand(self, value):
        self._vehicle_brand = value
    @property
    def vehicle_frame_no(self):
        return self._vehicle_frame_no

    @vehicle_frame_no.setter
    def vehicle_frame_no(self, value):
        self._vehicle_frame_no = value
    @property
    def vehicle_no(self):
        return self._vehicle_no

    @vehicle_no.setter
    def vehicle_no(self, value):
        self._vehicle_no = value
    @property
    def vehicle_registration(self):
        return self._vehicle_registration

    @vehicle_registration.setter
    def vehicle_registration(self, value):
        self._vehicle_registration = value
    @property
    def vehicle_type(self):
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value):
        self._vehicle_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.vehicle_brand:
            if hasattr(self.vehicle_brand, 'to_alipay_dict'):
                params['vehicle_brand'] = self.vehicle_brand.to_alipay_dict()
            else:
                params['vehicle_brand'] = self.vehicle_brand
        if self.vehicle_frame_no:
            if hasattr(self.vehicle_frame_no, 'to_alipay_dict'):
                params['vehicle_frame_no'] = self.vehicle_frame_no.to_alipay_dict()
            else:
                params['vehicle_frame_no'] = self.vehicle_frame_no
        if self.vehicle_no:
            if hasattr(self.vehicle_no, 'to_alipay_dict'):
                params['vehicle_no'] = self.vehicle_no.to_alipay_dict()
            else:
                params['vehicle_no'] = self.vehicle_no
        if self.vehicle_registration:
            if hasattr(self.vehicle_registration, 'to_alipay_dict'):
                params['vehicle_registration'] = self.vehicle_registration.to_alipay_dict()
            else:
                params['vehicle_registration'] = self.vehicle_registration
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
        o = InsOpenVehicleDTO()
        if 'vehicle_brand' in d:
            o.vehicle_brand = d['vehicle_brand']
        if 'vehicle_frame_no' in d:
            o.vehicle_frame_no = d['vehicle_frame_no']
        if 'vehicle_no' in d:
            o.vehicle_no = d['vehicle_no']
        if 'vehicle_registration' in d:
            o.vehicle_registration = d['vehicle_registration']
        if 'vehicle_type' in d:
            o.vehicle_type = d['vehicle_type']
        return o


