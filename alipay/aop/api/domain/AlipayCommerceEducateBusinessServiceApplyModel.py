#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateBusinessServiceApplyModel(object):

    def __init__(self):
        self._campus_name = None
        self._city_code = None
        self._district_code = None
        self._isv_name = None
        self._isv_telephone = None
        self._province_code = None
        self._school_name = None
        self._school_pid = None
        self._school_property = None
        self._school_std_code = None
        self._school_type = None
        self._smid = None

    @property
    def campus_name(self):
        return self._campus_name

    @campus_name.setter
    def campus_name(self, value):
        self._campus_name = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def isv_name(self):
        return self._isv_name

    @isv_name.setter
    def isv_name(self, value):
        self._isv_name = value
    @property
    def isv_telephone(self):
        return self._isv_telephone

    @isv_telephone.setter
    def isv_telephone(self, value):
        self._isv_telephone = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def school_name(self):
        return self._school_name

    @school_name.setter
    def school_name(self, value):
        self._school_name = value
    @property
    def school_pid(self):
        return self._school_pid

    @school_pid.setter
    def school_pid(self, value):
        self._school_pid = value
    @property
    def school_property(self):
        return self._school_property

    @school_property.setter
    def school_property(self, value):
        self._school_property = value
    @property
    def school_std_code(self):
        return self._school_std_code

    @school_std_code.setter
    def school_std_code(self, value):
        self._school_std_code = value
    @property
    def school_type(self):
        return self._school_type

    @school_type.setter
    def school_type(self, value):
        self._school_type = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value


    def to_alipay_dict(self):
        params = dict()
        if self.campus_name:
            if hasattr(self.campus_name, 'to_alipay_dict'):
                params['campus_name'] = self.campus_name.to_alipay_dict()
            else:
                params['campus_name'] = self.campus_name
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.isv_name:
            if hasattr(self.isv_name, 'to_alipay_dict'):
                params['isv_name'] = self.isv_name.to_alipay_dict()
            else:
                params['isv_name'] = self.isv_name
        if self.isv_telephone:
            if hasattr(self.isv_telephone, 'to_alipay_dict'):
                params['isv_telephone'] = self.isv_telephone.to_alipay_dict()
            else:
                params['isv_telephone'] = self.isv_telephone
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.school_name:
            if hasattr(self.school_name, 'to_alipay_dict'):
                params['school_name'] = self.school_name.to_alipay_dict()
            else:
                params['school_name'] = self.school_name
        if self.school_pid:
            if hasattr(self.school_pid, 'to_alipay_dict'):
                params['school_pid'] = self.school_pid.to_alipay_dict()
            else:
                params['school_pid'] = self.school_pid
        if self.school_property:
            if hasattr(self.school_property, 'to_alipay_dict'):
                params['school_property'] = self.school_property.to_alipay_dict()
            else:
                params['school_property'] = self.school_property
        if self.school_std_code:
            if hasattr(self.school_std_code, 'to_alipay_dict'):
                params['school_std_code'] = self.school_std_code.to_alipay_dict()
            else:
                params['school_std_code'] = self.school_std_code
        if self.school_type:
            if hasattr(self.school_type, 'to_alipay_dict'):
                params['school_type'] = self.school_type.to_alipay_dict()
            else:
                params['school_type'] = self.school_type
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateBusinessServiceApplyModel()
        if 'campus_name' in d:
            o.campus_name = d['campus_name']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'isv_name' in d:
            o.isv_name = d['isv_name']
        if 'isv_telephone' in d:
            o.isv_telephone = d['isv_telephone']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'school_name' in d:
            o.school_name = d['school_name']
        if 'school_pid' in d:
            o.school_pid = d['school_pid']
        if 'school_property' in d:
            o.school_property = d['school_property']
        if 'school_std_code' in d:
            o.school_std_code = d['school_std_code']
        if 'school_type' in d:
            o.school_type = d['school_type']
        if 'smid' in d:
            o.smid = d['smid']
        return o


