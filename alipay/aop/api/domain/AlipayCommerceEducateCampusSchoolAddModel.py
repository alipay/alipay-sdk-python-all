#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateCampusSchoolAddModel(object):

    def __init__(self):
        self._address = None
        self._city_code = None
        self._inst_name = None
        self._inst_pid = None
        self._inst_std_code = None
        self._latitude = None
        self._learning_stage = None
        self._longitude = None
        self._province_code = None
        self._school_property = None
        self._test_mode = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def inst_name(self):
        return self._inst_name

    @inst_name.setter
    def inst_name(self, value):
        self._inst_name = value
    @property
    def inst_pid(self):
        return self._inst_pid

    @inst_pid.setter
    def inst_pid(self, value):
        self._inst_pid = value
    @property
    def inst_std_code(self):
        return self._inst_std_code

    @inst_std_code.setter
    def inst_std_code(self, value):
        self._inst_std_code = value
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
    @property
    def learning_stage(self):
        return self._learning_stage

    @learning_stage.setter
    def learning_stage(self, value):
        self._learning_stage = value
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def school_property(self):
        return self._school_property

    @school_property.setter
    def school_property(self, value):
        self._school_property = value
    @property
    def test_mode(self):
        return self._test_mode

    @test_mode.setter
    def test_mode(self, value):
        self._test_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.inst_name:
            if hasattr(self.inst_name, 'to_alipay_dict'):
                params['inst_name'] = self.inst_name.to_alipay_dict()
            else:
                params['inst_name'] = self.inst_name
        if self.inst_pid:
            if hasattr(self.inst_pid, 'to_alipay_dict'):
                params['inst_pid'] = self.inst_pid.to_alipay_dict()
            else:
                params['inst_pid'] = self.inst_pid
        if self.inst_std_code:
            if hasattr(self.inst_std_code, 'to_alipay_dict'):
                params['inst_std_code'] = self.inst_std_code.to_alipay_dict()
            else:
                params['inst_std_code'] = self.inst_std_code
        if self.latitude:
            if hasattr(self.latitude, 'to_alipay_dict'):
                params['latitude'] = self.latitude.to_alipay_dict()
            else:
                params['latitude'] = self.latitude
        if self.learning_stage:
            if hasattr(self.learning_stage, 'to_alipay_dict'):
                params['learning_stage'] = self.learning_stage.to_alipay_dict()
            else:
                params['learning_stage'] = self.learning_stage
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.school_property:
            if hasattr(self.school_property, 'to_alipay_dict'):
                params['school_property'] = self.school_property.to_alipay_dict()
            else:
                params['school_property'] = self.school_property
        if self.test_mode:
            if hasattr(self.test_mode, 'to_alipay_dict'):
                params['test_mode'] = self.test_mode.to_alipay_dict()
            else:
                params['test_mode'] = self.test_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateCampusSchoolAddModel()
        if 'address' in d:
            o.address = d['address']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'inst_name' in d:
            o.inst_name = d['inst_name']
        if 'inst_pid' in d:
            o.inst_pid = d['inst_pid']
        if 'inst_std_code' in d:
            o.inst_std_code = d['inst_std_code']
        if 'latitude' in d:
            o.latitude = d['latitude']
        if 'learning_stage' in d:
            o.learning_stage = d['learning_stage']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'school_property' in d:
            o.school_property = d['school_property']
        if 'test_mode' in d:
            o.test_mode = d['test_mode']
        return o


