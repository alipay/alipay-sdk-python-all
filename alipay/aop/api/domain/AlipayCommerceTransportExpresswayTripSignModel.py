#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportExpresswayTripSignModel(object):

    def __init__(self):
        self._car_type = None
        self._city_code = None
        self._isv_id = None
        self._mobile_no = None
        self._open_id = None
        self._out_agreement_no = None
        self._plate_color = None
        self._plate_no = None
        self._user_id = None
        self._vi_height = None
        self._vi_length = None
        self._vi_license_apc = None
        self._vi_license_brand_model = None
        self._vi_license_car_type = None
        self._vi_license_engine = None
        self._vi_license_front_file_id = None
        self._vi_license_issue_date = None
        self._vi_license_owner = None
        self._vi_license_register_date = None
        self._vi_license_unladen_mass = None
        self._vi_license_use_type = None
        self._vi_license_vice_file_id = None
        self._vi_license_vin = None
        self._vi_width = None

    @property
    def car_type(self):
        return self._car_type

    @car_type.setter
    def car_type(self, value):
        self._car_type = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def isv_id(self):
        return self._isv_id

    @isv_id.setter
    def isv_id(self, value):
        self._isv_id = value
    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_agreement_no(self):
        return self._out_agreement_no

    @out_agreement_no.setter
    def out_agreement_no(self, value):
        self._out_agreement_no = value
    @property
    def plate_color(self):
        return self._plate_color

    @plate_color.setter
    def plate_color(self, value):
        self._plate_color = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def vi_height(self):
        return self._vi_height

    @vi_height.setter
    def vi_height(self, value):
        self._vi_height = value
    @property
    def vi_length(self):
        return self._vi_length

    @vi_length.setter
    def vi_length(self, value):
        self._vi_length = value
    @property
    def vi_license_apc(self):
        return self._vi_license_apc

    @vi_license_apc.setter
    def vi_license_apc(self, value):
        self._vi_license_apc = value
    @property
    def vi_license_brand_model(self):
        return self._vi_license_brand_model

    @vi_license_brand_model.setter
    def vi_license_brand_model(self, value):
        self._vi_license_brand_model = value
    @property
    def vi_license_car_type(self):
        return self._vi_license_car_type

    @vi_license_car_type.setter
    def vi_license_car_type(self, value):
        self._vi_license_car_type = value
    @property
    def vi_license_engine(self):
        return self._vi_license_engine

    @vi_license_engine.setter
    def vi_license_engine(self, value):
        self._vi_license_engine = value
    @property
    def vi_license_front_file_id(self):
        return self._vi_license_front_file_id

    @vi_license_front_file_id.setter
    def vi_license_front_file_id(self, value):
        self._vi_license_front_file_id = value
    @property
    def vi_license_issue_date(self):
        return self._vi_license_issue_date

    @vi_license_issue_date.setter
    def vi_license_issue_date(self, value):
        self._vi_license_issue_date = value
    @property
    def vi_license_owner(self):
        return self._vi_license_owner

    @vi_license_owner.setter
    def vi_license_owner(self, value):
        self._vi_license_owner = value
    @property
    def vi_license_register_date(self):
        return self._vi_license_register_date

    @vi_license_register_date.setter
    def vi_license_register_date(self, value):
        self._vi_license_register_date = value
    @property
    def vi_license_unladen_mass(self):
        return self._vi_license_unladen_mass

    @vi_license_unladen_mass.setter
    def vi_license_unladen_mass(self, value):
        self._vi_license_unladen_mass = value
    @property
    def vi_license_use_type(self):
        return self._vi_license_use_type

    @vi_license_use_type.setter
    def vi_license_use_type(self, value):
        self._vi_license_use_type = value
    @property
    def vi_license_vice_file_id(self):
        return self._vi_license_vice_file_id

    @vi_license_vice_file_id.setter
    def vi_license_vice_file_id(self, value):
        self._vi_license_vice_file_id = value
    @property
    def vi_license_vin(self):
        return self._vi_license_vin

    @vi_license_vin.setter
    def vi_license_vin(self, value):
        self._vi_license_vin = value
    @property
    def vi_width(self):
        return self._vi_width

    @vi_width.setter
    def vi_width(self, value):
        self._vi_width = value


    def to_alipay_dict(self):
        params = dict()
        if self.car_type:
            if hasattr(self.car_type, 'to_alipay_dict'):
                params['car_type'] = self.car_type.to_alipay_dict()
            else:
                params['car_type'] = self.car_type
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.isv_id:
            if hasattr(self.isv_id, 'to_alipay_dict'):
                params['isv_id'] = self.isv_id.to_alipay_dict()
            else:
                params['isv_id'] = self.isv_id
        if self.mobile_no:
            if hasattr(self.mobile_no, 'to_alipay_dict'):
                params['mobile_no'] = self.mobile_no.to_alipay_dict()
            else:
                params['mobile_no'] = self.mobile_no
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_agreement_no:
            if hasattr(self.out_agreement_no, 'to_alipay_dict'):
                params['out_agreement_no'] = self.out_agreement_no.to_alipay_dict()
            else:
                params['out_agreement_no'] = self.out_agreement_no
        if self.plate_color:
            if hasattr(self.plate_color, 'to_alipay_dict'):
                params['plate_color'] = self.plate_color.to_alipay_dict()
            else:
                params['plate_color'] = self.plate_color
        if self.plate_no:
            if hasattr(self.plate_no, 'to_alipay_dict'):
                params['plate_no'] = self.plate_no.to_alipay_dict()
            else:
                params['plate_no'] = self.plate_no
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.vi_height:
            if hasattr(self.vi_height, 'to_alipay_dict'):
                params['vi_height'] = self.vi_height.to_alipay_dict()
            else:
                params['vi_height'] = self.vi_height
        if self.vi_length:
            if hasattr(self.vi_length, 'to_alipay_dict'):
                params['vi_length'] = self.vi_length.to_alipay_dict()
            else:
                params['vi_length'] = self.vi_length
        if self.vi_license_apc:
            if hasattr(self.vi_license_apc, 'to_alipay_dict'):
                params['vi_license_apc'] = self.vi_license_apc.to_alipay_dict()
            else:
                params['vi_license_apc'] = self.vi_license_apc
        if self.vi_license_brand_model:
            if hasattr(self.vi_license_brand_model, 'to_alipay_dict'):
                params['vi_license_brand_model'] = self.vi_license_brand_model.to_alipay_dict()
            else:
                params['vi_license_brand_model'] = self.vi_license_brand_model
        if self.vi_license_car_type:
            if hasattr(self.vi_license_car_type, 'to_alipay_dict'):
                params['vi_license_car_type'] = self.vi_license_car_type.to_alipay_dict()
            else:
                params['vi_license_car_type'] = self.vi_license_car_type
        if self.vi_license_engine:
            if hasattr(self.vi_license_engine, 'to_alipay_dict'):
                params['vi_license_engine'] = self.vi_license_engine.to_alipay_dict()
            else:
                params['vi_license_engine'] = self.vi_license_engine
        if self.vi_license_front_file_id:
            if hasattr(self.vi_license_front_file_id, 'to_alipay_dict'):
                params['vi_license_front_file_id'] = self.vi_license_front_file_id.to_alipay_dict()
            else:
                params['vi_license_front_file_id'] = self.vi_license_front_file_id
        if self.vi_license_issue_date:
            if hasattr(self.vi_license_issue_date, 'to_alipay_dict'):
                params['vi_license_issue_date'] = self.vi_license_issue_date.to_alipay_dict()
            else:
                params['vi_license_issue_date'] = self.vi_license_issue_date
        if self.vi_license_owner:
            if hasattr(self.vi_license_owner, 'to_alipay_dict'):
                params['vi_license_owner'] = self.vi_license_owner.to_alipay_dict()
            else:
                params['vi_license_owner'] = self.vi_license_owner
        if self.vi_license_register_date:
            if hasattr(self.vi_license_register_date, 'to_alipay_dict'):
                params['vi_license_register_date'] = self.vi_license_register_date.to_alipay_dict()
            else:
                params['vi_license_register_date'] = self.vi_license_register_date
        if self.vi_license_unladen_mass:
            if hasattr(self.vi_license_unladen_mass, 'to_alipay_dict'):
                params['vi_license_unladen_mass'] = self.vi_license_unladen_mass.to_alipay_dict()
            else:
                params['vi_license_unladen_mass'] = self.vi_license_unladen_mass
        if self.vi_license_use_type:
            if hasattr(self.vi_license_use_type, 'to_alipay_dict'):
                params['vi_license_use_type'] = self.vi_license_use_type.to_alipay_dict()
            else:
                params['vi_license_use_type'] = self.vi_license_use_type
        if self.vi_license_vice_file_id:
            if hasattr(self.vi_license_vice_file_id, 'to_alipay_dict'):
                params['vi_license_vice_file_id'] = self.vi_license_vice_file_id.to_alipay_dict()
            else:
                params['vi_license_vice_file_id'] = self.vi_license_vice_file_id
        if self.vi_license_vin:
            if hasattr(self.vi_license_vin, 'to_alipay_dict'):
                params['vi_license_vin'] = self.vi_license_vin.to_alipay_dict()
            else:
                params['vi_license_vin'] = self.vi_license_vin
        if self.vi_width:
            if hasattr(self.vi_width, 'to_alipay_dict'):
                params['vi_width'] = self.vi_width.to_alipay_dict()
            else:
                params['vi_width'] = self.vi_width
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportExpresswayTripSignModel()
        if 'car_type' in d:
            o.car_type = d['car_type']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'isv_id' in d:
            o.isv_id = d['isv_id']
        if 'mobile_no' in d:
            o.mobile_no = d['mobile_no']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_agreement_no' in d:
            o.out_agreement_no = d['out_agreement_no']
        if 'plate_color' in d:
            o.plate_color = d['plate_color']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'vi_height' in d:
            o.vi_height = d['vi_height']
        if 'vi_length' in d:
            o.vi_length = d['vi_length']
        if 'vi_license_apc' in d:
            o.vi_license_apc = d['vi_license_apc']
        if 'vi_license_brand_model' in d:
            o.vi_license_brand_model = d['vi_license_brand_model']
        if 'vi_license_car_type' in d:
            o.vi_license_car_type = d['vi_license_car_type']
        if 'vi_license_engine' in d:
            o.vi_license_engine = d['vi_license_engine']
        if 'vi_license_front_file_id' in d:
            o.vi_license_front_file_id = d['vi_license_front_file_id']
        if 'vi_license_issue_date' in d:
            o.vi_license_issue_date = d['vi_license_issue_date']
        if 'vi_license_owner' in d:
            o.vi_license_owner = d['vi_license_owner']
        if 'vi_license_register_date' in d:
            o.vi_license_register_date = d['vi_license_register_date']
        if 'vi_license_unladen_mass' in d:
            o.vi_license_unladen_mass = d['vi_license_unladen_mass']
        if 'vi_license_use_type' in d:
            o.vi_license_use_type = d['vi_license_use_type']
        if 'vi_license_vice_file_id' in d:
            o.vi_license_vice_file_id = d['vi_license_vice_file_id']
        if 'vi_license_vin' in d:
            o.vi_license_vin = d['vi_license_vin']
        if 'vi_width' in d:
            o.vi_width = d['vi_width']
        return o


