#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZmCarOwnerVehicleInfo(object):

    def __init__(self):
        self._license_plate_number = None
        self._vehicle_belong_owner = None
        self._vehicle_brand = None
        self._vehicle_engine_no = None
        self._vehicle_register_date = None
        self._vehicle_type = None
        self._vehicle_usage = None
        self._vehicle_vin = None
        self._verification_level = None

    @property
    def license_plate_number(self):
        return self._license_plate_number

    @license_plate_number.setter
    def license_plate_number(self, value):
        self._license_plate_number = value
    @property
    def vehicle_belong_owner(self):
        return self._vehicle_belong_owner

    @vehicle_belong_owner.setter
    def vehicle_belong_owner(self, value):
        self._vehicle_belong_owner = value
    @property
    def vehicle_brand(self):
        return self._vehicle_brand

    @vehicle_brand.setter
    def vehicle_brand(self, value):
        self._vehicle_brand = value
    @property
    def vehicle_engine_no(self):
        return self._vehicle_engine_no

    @vehicle_engine_no.setter
    def vehicle_engine_no(self, value):
        self._vehicle_engine_no = value
    @property
    def vehicle_register_date(self):
        return self._vehicle_register_date

    @vehicle_register_date.setter
    def vehicle_register_date(self, value):
        self._vehicle_register_date = value
    @property
    def vehicle_type(self):
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value):
        self._vehicle_type = value
    @property
    def vehicle_usage(self):
        return self._vehicle_usage

    @vehicle_usage.setter
    def vehicle_usage(self, value):
        self._vehicle_usage = value
    @property
    def vehicle_vin(self):
        return self._vehicle_vin

    @vehicle_vin.setter
    def vehicle_vin(self, value):
        self._vehicle_vin = value
    @property
    def verification_level(self):
        return self._verification_level

    @verification_level.setter
    def verification_level(self, value):
        self._verification_level = value


    def to_alipay_dict(self):
        params = dict()
        if self.license_plate_number:
            if hasattr(self.license_plate_number, 'to_alipay_dict'):
                params['license_plate_number'] = self.license_plate_number.to_alipay_dict()
            else:
                params['license_plate_number'] = self.license_plate_number
        if self.vehicle_belong_owner:
            if hasattr(self.vehicle_belong_owner, 'to_alipay_dict'):
                params['vehicle_belong_owner'] = self.vehicle_belong_owner.to_alipay_dict()
            else:
                params['vehicle_belong_owner'] = self.vehicle_belong_owner
        if self.vehicle_brand:
            if hasattr(self.vehicle_brand, 'to_alipay_dict'):
                params['vehicle_brand'] = self.vehicle_brand.to_alipay_dict()
            else:
                params['vehicle_brand'] = self.vehicle_brand
        if self.vehicle_engine_no:
            if hasattr(self.vehicle_engine_no, 'to_alipay_dict'):
                params['vehicle_engine_no'] = self.vehicle_engine_no.to_alipay_dict()
            else:
                params['vehicle_engine_no'] = self.vehicle_engine_no
        if self.vehicle_register_date:
            if hasattr(self.vehicle_register_date, 'to_alipay_dict'):
                params['vehicle_register_date'] = self.vehicle_register_date.to_alipay_dict()
            else:
                params['vehicle_register_date'] = self.vehicle_register_date
        if self.vehicle_type:
            if hasattr(self.vehicle_type, 'to_alipay_dict'):
                params['vehicle_type'] = self.vehicle_type.to_alipay_dict()
            else:
                params['vehicle_type'] = self.vehicle_type
        if self.vehicle_usage:
            if hasattr(self.vehicle_usage, 'to_alipay_dict'):
                params['vehicle_usage'] = self.vehicle_usage.to_alipay_dict()
            else:
                params['vehicle_usage'] = self.vehicle_usage
        if self.vehicle_vin:
            if hasattr(self.vehicle_vin, 'to_alipay_dict'):
                params['vehicle_vin'] = self.vehicle_vin.to_alipay_dict()
            else:
                params['vehicle_vin'] = self.vehicle_vin
        if self.verification_level:
            if hasattr(self.verification_level, 'to_alipay_dict'):
                params['verification_level'] = self.verification_level.to_alipay_dict()
            else:
                params['verification_level'] = self.verification_level
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZmCarOwnerVehicleInfo()
        if 'license_plate_number' in d:
            o.license_plate_number = d['license_plate_number']
        if 'vehicle_belong_owner' in d:
            o.vehicle_belong_owner = d['vehicle_belong_owner']
        if 'vehicle_brand' in d:
            o.vehicle_brand = d['vehicle_brand']
        if 'vehicle_engine_no' in d:
            o.vehicle_engine_no = d['vehicle_engine_no']
        if 'vehicle_register_date' in d:
            o.vehicle_register_date = d['vehicle_register_date']
        if 'vehicle_type' in d:
            o.vehicle_type = d['vehicle_type']
        if 'vehicle_usage' in d:
            o.vehicle_usage = d['vehicle_usage']
        if 'vehicle_vin' in d:
            o.vehicle_vin = d['vehicle_vin']
        if 'verification_level' in d:
            o.verification_level = d['verification_level']
        return o


