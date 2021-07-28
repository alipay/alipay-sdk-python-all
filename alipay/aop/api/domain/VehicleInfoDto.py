#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VehicleInfoDto(object):

    def __init__(self):
        self._brand_name = None
        self._cert_hash = None
        self._cert_result = None
        self._cert_type = None
        self._certification = None
        self._city_code = None
        self._city_name = None
        self._engine_no = None
        self._hash_type = None
        self._miles = None
        self._model_id = None
        self._model_name = None
        self._owner = None
        self._plate_no = None
        self._register_date = None
        self._series_name = None
        self._uid = None
        self._use_type = None
        self._vehicle_type = None
        self._vin = None

    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def cert_hash(self):
        return self._cert_hash

    @cert_hash.setter
    def cert_hash(self, value):
        self._cert_hash = value
    @property
    def cert_result(self):
        return self._cert_result

    @cert_result.setter
    def cert_result(self, value):
        self._cert_result = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def certification(self):
        return self._certification

    @certification.setter
    def certification(self, value):
        self._certification = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def engine_no(self):
        return self._engine_no

    @engine_no.setter
    def engine_no(self, value):
        self._engine_no = value
    @property
    def hash_type(self):
        return self._hash_type

    @hash_type.setter
    def hash_type(self, value):
        self._hash_type = value
    @property
    def miles(self):
        return self._miles

    @miles.setter
    def miles(self, value):
        self._miles = value
    @property
    def model_id(self):
        return self._model_id

    @model_id.setter
    def model_id(self, value):
        self._model_id = value
    @property
    def model_name(self):
        return self._model_name

    @model_name.setter
    def model_name(self, value):
        self._model_name = value
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value
    @property
    def register_date(self):
        return self._register_date

    @register_date.setter
    def register_date(self, value):
        self._register_date = value
    @property
    def series_name(self):
        return self._series_name

    @series_name.setter
    def series_name(self, value):
        self._series_name = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value
    @property
    def use_type(self):
        return self._use_type

    @use_type.setter
    def use_type(self, value):
        self._use_type = value
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
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.cert_hash:
            if hasattr(self.cert_hash, 'to_alipay_dict'):
                params['cert_hash'] = self.cert_hash.to_alipay_dict()
            else:
                params['cert_hash'] = self.cert_hash
        if self.cert_result:
            if hasattr(self.cert_result, 'to_alipay_dict'):
                params['cert_result'] = self.cert_result.to_alipay_dict()
            else:
                params['cert_result'] = self.cert_result
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.certification:
            if hasattr(self.certification, 'to_alipay_dict'):
                params['certification'] = self.certification.to_alipay_dict()
            else:
                params['certification'] = self.certification
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.engine_no:
            if hasattr(self.engine_no, 'to_alipay_dict'):
                params['engine_no'] = self.engine_no.to_alipay_dict()
            else:
                params['engine_no'] = self.engine_no
        if self.hash_type:
            if hasattr(self.hash_type, 'to_alipay_dict'):
                params['hash_type'] = self.hash_type.to_alipay_dict()
            else:
                params['hash_type'] = self.hash_type
        if self.miles:
            if hasattr(self.miles, 'to_alipay_dict'):
                params['miles'] = self.miles.to_alipay_dict()
            else:
                params['miles'] = self.miles
        if self.model_id:
            if hasattr(self.model_id, 'to_alipay_dict'):
                params['model_id'] = self.model_id.to_alipay_dict()
            else:
                params['model_id'] = self.model_id
        if self.model_name:
            if hasattr(self.model_name, 'to_alipay_dict'):
                params['model_name'] = self.model_name.to_alipay_dict()
            else:
                params['model_name'] = self.model_name
        if self.owner:
            if hasattr(self.owner, 'to_alipay_dict'):
                params['owner'] = self.owner.to_alipay_dict()
            else:
                params['owner'] = self.owner
        if self.plate_no:
            if hasattr(self.plate_no, 'to_alipay_dict'):
                params['plate_no'] = self.plate_no.to_alipay_dict()
            else:
                params['plate_no'] = self.plate_no
        if self.register_date:
            if hasattr(self.register_date, 'to_alipay_dict'):
                params['register_date'] = self.register_date.to_alipay_dict()
            else:
                params['register_date'] = self.register_date
        if self.series_name:
            if hasattr(self.series_name, 'to_alipay_dict'):
                params['series_name'] = self.series_name.to_alipay_dict()
            else:
                params['series_name'] = self.series_name
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        if self.use_type:
            if hasattr(self.use_type, 'to_alipay_dict'):
                params['use_type'] = self.use_type.to_alipay_dict()
            else:
                params['use_type'] = self.use_type
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
        o = VehicleInfoDto()
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'cert_hash' in d:
            o.cert_hash = d['cert_hash']
        if 'cert_result' in d:
            o.cert_result = d['cert_result']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'certification' in d:
            o.certification = d['certification']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'engine_no' in d:
            o.engine_no = d['engine_no']
        if 'hash_type' in d:
            o.hash_type = d['hash_type']
        if 'miles' in d:
            o.miles = d['miles']
        if 'model_id' in d:
            o.model_id = d['model_id']
        if 'model_name' in d:
            o.model_name = d['model_name']
        if 'owner' in d:
            o.owner = d['owner']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'register_date' in d:
            o.register_date = d['register_date']
        if 'series_name' in d:
            o.series_name = d['series_name']
        if 'uid' in d:
            o.uid = d['uid']
        if 'use_type' in d:
            o.use_type = d['use_type']
        if 'vehicle_type' in d:
            o.vehicle_type = d['vehicle_type']
        if 'vin' in d:
            o.vin = d['vin']
        return o


