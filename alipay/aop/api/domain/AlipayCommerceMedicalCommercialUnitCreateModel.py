#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalCommercialUnitCreateModel(object):

    def __init__(self):
        self._out_product_id_list = None
        self._unit_address = None
        self._unit_city_code = None
        self._unit_contact_number = None
        self._unit_latitude = None
        self._unit_longitude = None
        self._unit_name = None
        self._unit_opening_hours = None
        self._unit_out_code = None
        self._unit_out_pid = None

    @property
    def out_product_id_list(self):
        return self._out_product_id_list

    @out_product_id_list.setter
    def out_product_id_list(self, value):
        if isinstance(value, list):
            self._out_product_id_list = list()
            for i in value:
                self._out_product_id_list.append(i)
    @property
    def unit_address(self):
        return self._unit_address

    @unit_address.setter
    def unit_address(self, value):
        self._unit_address = value
    @property
    def unit_city_code(self):
        return self._unit_city_code

    @unit_city_code.setter
    def unit_city_code(self, value):
        self._unit_city_code = value
    @property
    def unit_contact_number(self):
        return self._unit_contact_number

    @unit_contact_number.setter
    def unit_contact_number(self, value):
        self._unit_contact_number = value
    @property
    def unit_latitude(self):
        return self._unit_latitude

    @unit_latitude.setter
    def unit_latitude(self, value):
        self._unit_latitude = value
    @property
    def unit_longitude(self):
        return self._unit_longitude

    @unit_longitude.setter
    def unit_longitude(self, value):
        self._unit_longitude = value
    @property
    def unit_name(self):
        return self._unit_name

    @unit_name.setter
    def unit_name(self, value):
        self._unit_name = value
    @property
    def unit_opening_hours(self):
        return self._unit_opening_hours

    @unit_opening_hours.setter
    def unit_opening_hours(self, value):
        self._unit_opening_hours = value
    @property
    def unit_out_code(self):
        return self._unit_out_code

    @unit_out_code.setter
    def unit_out_code(self, value):
        self._unit_out_code = value
    @property
    def unit_out_pid(self):
        return self._unit_out_pid

    @unit_out_pid.setter
    def unit_out_pid(self, value):
        self._unit_out_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_product_id_list:
            if isinstance(self.out_product_id_list, list):
                for i in range(0, len(self.out_product_id_list)):
                    element = self.out_product_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_product_id_list[i] = element.to_alipay_dict()
            if hasattr(self.out_product_id_list, 'to_alipay_dict'):
                params['out_product_id_list'] = self.out_product_id_list.to_alipay_dict()
            else:
                params['out_product_id_list'] = self.out_product_id_list
        if self.unit_address:
            if hasattr(self.unit_address, 'to_alipay_dict'):
                params['unit_address'] = self.unit_address.to_alipay_dict()
            else:
                params['unit_address'] = self.unit_address
        if self.unit_city_code:
            if hasattr(self.unit_city_code, 'to_alipay_dict'):
                params['unit_city_code'] = self.unit_city_code.to_alipay_dict()
            else:
                params['unit_city_code'] = self.unit_city_code
        if self.unit_contact_number:
            if hasattr(self.unit_contact_number, 'to_alipay_dict'):
                params['unit_contact_number'] = self.unit_contact_number.to_alipay_dict()
            else:
                params['unit_contact_number'] = self.unit_contact_number
        if self.unit_latitude:
            if hasattr(self.unit_latitude, 'to_alipay_dict'):
                params['unit_latitude'] = self.unit_latitude.to_alipay_dict()
            else:
                params['unit_latitude'] = self.unit_latitude
        if self.unit_longitude:
            if hasattr(self.unit_longitude, 'to_alipay_dict'):
                params['unit_longitude'] = self.unit_longitude.to_alipay_dict()
            else:
                params['unit_longitude'] = self.unit_longitude
        if self.unit_name:
            if hasattr(self.unit_name, 'to_alipay_dict'):
                params['unit_name'] = self.unit_name.to_alipay_dict()
            else:
                params['unit_name'] = self.unit_name
        if self.unit_opening_hours:
            if hasattr(self.unit_opening_hours, 'to_alipay_dict'):
                params['unit_opening_hours'] = self.unit_opening_hours.to_alipay_dict()
            else:
                params['unit_opening_hours'] = self.unit_opening_hours
        if self.unit_out_code:
            if hasattr(self.unit_out_code, 'to_alipay_dict'):
                params['unit_out_code'] = self.unit_out_code.to_alipay_dict()
            else:
                params['unit_out_code'] = self.unit_out_code
        if self.unit_out_pid:
            if hasattr(self.unit_out_pid, 'to_alipay_dict'):
                params['unit_out_pid'] = self.unit_out_pid.to_alipay_dict()
            else:
                params['unit_out_pid'] = self.unit_out_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalCommercialUnitCreateModel()
        if 'out_product_id_list' in d:
            o.out_product_id_list = d['out_product_id_list']
        if 'unit_address' in d:
            o.unit_address = d['unit_address']
        if 'unit_city_code' in d:
            o.unit_city_code = d['unit_city_code']
        if 'unit_contact_number' in d:
            o.unit_contact_number = d['unit_contact_number']
        if 'unit_latitude' in d:
            o.unit_latitude = d['unit_latitude']
        if 'unit_longitude' in d:
            o.unit_longitude = d['unit_longitude']
        if 'unit_name' in d:
            o.unit_name = d['unit_name']
        if 'unit_opening_hours' in d:
            o.unit_opening_hours = d['unit_opening_hours']
        if 'unit_out_code' in d:
            o.unit_out_code = d['unit_out_code']
        if 'unit_out_pid' in d:
            o.unit_out_pid = d['unit_out_pid']
        return o


