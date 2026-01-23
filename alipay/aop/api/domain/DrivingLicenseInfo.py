#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DrivingLicenseInfo(object):

    def __init__(self):
        self._address = None
        self._engine_number = None
        self._file_path = None
        self._issue_date = None
        self._license_plate_number = None
        self._registration_date = None
        self._use_character = None
        self._vehicle_brand_id = None
        self._vehicle_brand_name = None
        self._vehicle_model_id = None
        self._vehicle_model_name = None
        self._vehicle_owner = None
        self._vehicle_series_id = None
        self._vehicle_series_name = None
        self._vehicle_type = None
        self._vin_number = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def engine_number(self):
        return self._engine_number

    @engine_number.setter
    def engine_number(self, value):
        self._engine_number = value
    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        self._file_path = value
    @property
    def issue_date(self):
        return self._issue_date

    @issue_date.setter
    def issue_date(self, value):
        self._issue_date = value
    @property
    def license_plate_number(self):
        return self._license_plate_number

    @license_plate_number.setter
    def license_plate_number(self, value):
        self._license_plate_number = value
    @property
    def registration_date(self):
        return self._registration_date

    @registration_date.setter
    def registration_date(self, value):
        self._registration_date = value
    @property
    def use_character(self):
        return self._use_character

    @use_character.setter
    def use_character(self, value):
        self._use_character = value
    @property
    def vehicle_brand_id(self):
        return self._vehicle_brand_id

    @vehicle_brand_id.setter
    def vehicle_brand_id(self, value):
        self._vehicle_brand_id = value
    @property
    def vehicle_brand_name(self):
        return self._vehicle_brand_name

    @vehicle_brand_name.setter
    def vehicle_brand_name(self, value):
        self._vehicle_brand_name = value
    @property
    def vehicle_model_id(self):
        return self._vehicle_model_id

    @vehicle_model_id.setter
    def vehicle_model_id(self, value):
        self._vehicle_model_id = value
    @property
    def vehicle_model_name(self):
        return self._vehicle_model_name

    @vehicle_model_name.setter
    def vehicle_model_name(self, value):
        self._vehicle_model_name = value
    @property
    def vehicle_owner(self):
        return self._vehicle_owner

    @vehicle_owner.setter
    def vehicle_owner(self, value):
        self._vehicle_owner = value
    @property
    def vehicle_series_id(self):
        return self._vehicle_series_id

    @vehicle_series_id.setter
    def vehicle_series_id(self, value):
        self._vehicle_series_id = value
    @property
    def vehicle_series_name(self):
        return self._vehicle_series_name

    @vehicle_series_name.setter
    def vehicle_series_name(self, value):
        self._vehicle_series_name = value
    @property
    def vehicle_type(self):
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value):
        self._vehicle_type = value
    @property
    def vin_number(self):
        return self._vin_number

    @vin_number.setter
    def vin_number(self, value):
        self._vin_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.engine_number:
            if hasattr(self.engine_number, 'to_alipay_dict'):
                params['engine_number'] = self.engine_number.to_alipay_dict()
            else:
                params['engine_number'] = self.engine_number
        if self.file_path:
            if hasattr(self.file_path, 'to_alipay_dict'):
                params['file_path'] = self.file_path.to_alipay_dict()
            else:
                params['file_path'] = self.file_path
        if self.issue_date:
            if hasattr(self.issue_date, 'to_alipay_dict'):
                params['issue_date'] = self.issue_date.to_alipay_dict()
            else:
                params['issue_date'] = self.issue_date
        if self.license_plate_number:
            if hasattr(self.license_plate_number, 'to_alipay_dict'):
                params['license_plate_number'] = self.license_plate_number.to_alipay_dict()
            else:
                params['license_plate_number'] = self.license_plate_number
        if self.registration_date:
            if hasattr(self.registration_date, 'to_alipay_dict'):
                params['registration_date'] = self.registration_date.to_alipay_dict()
            else:
                params['registration_date'] = self.registration_date
        if self.use_character:
            if hasattr(self.use_character, 'to_alipay_dict'):
                params['use_character'] = self.use_character.to_alipay_dict()
            else:
                params['use_character'] = self.use_character
        if self.vehicle_brand_id:
            if hasattr(self.vehicle_brand_id, 'to_alipay_dict'):
                params['vehicle_brand_id'] = self.vehicle_brand_id.to_alipay_dict()
            else:
                params['vehicle_brand_id'] = self.vehicle_brand_id
        if self.vehicle_brand_name:
            if hasattr(self.vehicle_brand_name, 'to_alipay_dict'):
                params['vehicle_brand_name'] = self.vehicle_brand_name.to_alipay_dict()
            else:
                params['vehicle_brand_name'] = self.vehicle_brand_name
        if self.vehicle_model_id:
            if hasattr(self.vehicle_model_id, 'to_alipay_dict'):
                params['vehicle_model_id'] = self.vehicle_model_id.to_alipay_dict()
            else:
                params['vehicle_model_id'] = self.vehicle_model_id
        if self.vehicle_model_name:
            if hasattr(self.vehicle_model_name, 'to_alipay_dict'):
                params['vehicle_model_name'] = self.vehicle_model_name.to_alipay_dict()
            else:
                params['vehicle_model_name'] = self.vehicle_model_name
        if self.vehicle_owner:
            if hasattr(self.vehicle_owner, 'to_alipay_dict'):
                params['vehicle_owner'] = self.vehicle_owner.to_alipay_dict()
            else:
                params['vehicle_owner'] = self.vehicle_owner
        if self.vehicle_series_id:
            if hasattr(self.vehicle_series_id, 'to_alipay_dict'):
                params['vehicle_series_id'] = self.vehicle_series_id.to_alipay_dict()
            else:
                params['vehicle_series_id'] = self.vehicle_series_id
        if self.vehicle_series_name:
            if hasattr(self.vehicle_series_name, 'to_alipay_dict'):
                params['vehicle_series_name'] = self.vehicle_series_name.to_alipay_dict()
            else:
                params['vehicle_series_name'] = self.vehicle_series_name
        if self.vehicle_type:
            if hasattr(self.vehicle_type, 'to_alipay_dict'):
                params['vehicle_type'] = self.vehicle_type.to_alipay_dict()
            else:
                params['vehicle_type'] = self.vehicle_type
        if self.vin_number:
            if hasattr(self.vin_number, 'to_alipay_dict'):
                params['vin_number'] = self.vin_number.to_alipay_dict()
            else:
                params['vin_number'] = self.vin_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DrivingLicenseInfo()
        if 'address' in d:
            o.address = d['address']
        if 'engine_number' in d:
            o.engine_number = d['engine_number']
        if 'file_path' in d:
            o.file_path = d['file_path']
        if 'issue_date' in d:
            o.issue_date = d['issue_date']
        if 'license_plate_number' in d:
            o.license_plate_number = d['license_plate_number']
        if 'registration_date' in d:
            o.registration_date = d['registration_date']
        if 'use_character' in d:
            o.use_character = d['use_character']
        if 'vehicle_brand_id' in d:
            o.vehicle_brand_id = d['vehicle_brand_id']
        if 'vehicle_brand_name' in d:
            o.vehicle_brand_name = d['vehicle_brand_name']
        if 'vehicle_model_id' in d:
            o.vehicle_model_id = d['vehicle_model_id']
        if 'vehicle_model_name' in d:
            o.vehicle_model_name = d['vehicle_model_name']
        if 'vehicle_owner' in d:
            o.vehicle_owner = d['vehicle_owner']
        if 'vehicle_series_id' in d:
            o.vehicle_series_id = d['vehicle_series_id']
        if 'vehicle_series_name' in d:
            o.vehicle_series_name = d['vehicle_series_name']
        if 'vehicle_type' in d:
            o.vehicle_type = d['vehicle_type']
        if 'vin_number' in d:
            o.vin_number = d['vin_number']
        return o


