#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EtcVehicleInfo(object):

    def __init__(self):
        self._engine_no = None
        self._plate_color = None
        self._plate_no = None
        self._vi_ac = None
        self._vi_grant_date = None
        self._vi_gross_mass = None
        self._vi_height = None
        self._vi_length = None
        self._vi_model_name = None
        self._vi_owner_name = None
        self._vi_register_date = None
        self._vi_type = None
        self._vi_use_type = None
        self._vi_vin = None
        self._vi_width = None

    @property
    def engine_no(self):
        return self._engine_no

    @engine_no.setter
    def engine_no(self, value):
        self._engine_no = value
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
    def vi_ac(self):
        return self._vi_ac

    @vi_ac.setter
    def vi_ac(self, value):
        self._vi_ac = value
    @property
    def vi_grant_date(self):
        return self._vi_grant_date

    @vi_grant_date.setter
    def vi_grant_date(self, value):
        self._vi_grant_date = value
    @property
    def vi_gross_mass(self):
        return self._vi_gross_mass

    @vi_gross_mass.setter
    def vi_gross_mass(self, value):
        self._vi_gross_mass = value
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
    def vi_model_name(self):
        return self._vi_model_name

    @vi_model_name.setter
    def vi_model_name(self, value):
        self._vi_model_name = value
    @property
    def vi_owner_name(self):
        return self._vi_owner_name

    @vi_owner_name.setter
    def vi_owner_name(self, value):
        self._vi_owner_name = value
    @property
    def vi_register_date(self):
        return self._vi_register_date

    @vi_register_date.setter
    def vi_register_date(self, value):
        self._vi_register_date = value
    @property
    def vi_type(self):
        return self._vi_type

    @vi_type.setter
    def vi_type(self, value):
        self._vi_type = value
    @property
    def vi_use_type(self):
        return self._vi_use_type

    @vi_use_type.setter
    def vi_use_type(self, value):
        self._vi_use_type = value
    @property
    def vi_vin(self):
        return self._vi_vin

    @vi_vin.setter
    def vi_vin(self, value):
        self._vi_vin = value
    @property
    def vi_width(self):
        return self._vi_width

    @vi_width.setter
    def vi_width(self, value):
        self._vi_width = value


    def to_alipay_dict(self):
        params = dict()
        if self.engine_no:
            if hasattr(self.engine_no, 'to_alipay_dict'):
                params['engine_no'] = self.engine_no.to_alipay_dict()
            else:
                params['engine_no'] = self.engine_no
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
        if self.vi_ac:
            if hasattr(self.vi_ac, 'to_alipay_dict'):
                params['vi_ac'] = self.vi_ac.to_alipay_dict()
            else:
                params['vi_ac'] = self.vi_ac
        if self.vi_grant_date:
            if hasattr(self.vi_grant_date, 'to_alipay_dict'):
                params['vi_grant_date'] = self.vi_grant_date.to_alipay_dict()
            else:
                params['vi_grant_date'] = self.vi_grant_date
        if self.vi_gross_mass:
            if hasattr(self.vi_gross_mass, 'to_alipay_dict'):
                params['vi_gross_mass'] = self.vi_gross_mass.to_alipay_dict()
            else:
                params['vi_gross_mass'] = self.vi_gross_mass
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
        if self.vi_model_name:
            if hasattr(self.vi_model_name, 'to_alipay_dict'):
                params['vi_model_name'] = self.vi_model_name.to_alipay_dict()
            else:
                params['vi_model_name'] = self.vi_model_name
        if self.vi_owner_name:
            if hasattr(self.vi_owner_name, 'to_alipay_dict'):
                params['vi_owner_name'] = self.vi_owner_name.to_alipay_dict()
            else:
                params['vi_owner_name'] = self.vi_owner_name
        if self.vi_register_date:
            if hasattr(self.vi_register_date, 'to_alipay_dict'):
                params['vi_register_date'] = self.vi_register_date.to_alipay_dict()
            else:
                params['vi_register_date'] = self.vi_register_date
        if self.vi_type:
            if hasattr(self.vi_type, 'to_alipay_dict'):
                params['vi_type'] = self.vi_type.to_alipay_dict()
            else:
                params['vi_type'] = self.vi_type
        if self.vi_use_type:
            if hasattr(self.vi_use_type, 'to_alipay_dict'):
                params['vi_use_type'] = self.vi_use_type.to_alipay_dict()
            else:
                params['vi_use_type'] = self.vi_use_type
        if self.vi_vin:
            if hasattr(self.vi_vin, 'to_alipay_dict'):
                params['vi_vin'] = self.vi_vin.to_alipay_dict()
            else:
                params['vi_vin'] = self.vi_vin
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
        o = EtcVehicleInfo()
        if 'engine_no' in d:
            o.engine_no = d['engine_no']
        if 'plate_color' in d:
            o.plate_color = d['plate_color']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'vi_ac' in d:
            o.vi_ac = d['vi_ac']
        if 'vi_grant_date' in d:
            o.vi_grant_date = d['vi_grant_date']
        if 'vi_gross_mass' in d:
            o.vi_gross_mass = d['vi_gross_mass']
        if 'vi_height' in d:
            o.vi_height = d['vi_height']
        if 'vi_length' in d:
            o.vi_length = d['vi_length']
        if 'vi_model_name' in d:
            o.vi_model_name = d['vi_model_name']
        if 'vi_owner_name' in d:
            o.vi_owner_name = d['vi_owner_name']
        if 'vi_register_date' in d:
            o.vi_register_date = d['vi_register_date']
        if 'vi_type' in d:
            o.vi_type = d['vi_type']
        if 'vi_use_type' in d:
            o.vi_use_type = d['vi_use_type']
        if 'vi_vin' in d:
            o.vi_vin = d['vi_vin']
        if 'vi_width' in d:
            o.vi_width = d['vi_width']
        return o


