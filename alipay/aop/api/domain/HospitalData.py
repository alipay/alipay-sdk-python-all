#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HospitalData(object):

    def __init__(self):
        self._country_key_department = None
        self._hospital_addr = None
        self._hospital_alias = None
        self._hospital_city = None
        self._hospital_district = None
        self._hospital_grade = None
        self._hospital_id = None
        self._hospital_lat = None
        self._hospital_lgt = None
        self._hospital_logo = None
        self._hospital_name = None
        self._hospital_optag = None
        self._hospital_province = None
        self._hospital_standard_code = None
        self._hospital_tel = None
        self._hospital_type = None
        self._hospital_work_time = None
        self._key_department = None
        self._province_key_department = None

    @property
    def country_key_department(self):
        return self._country_key_department

    @country_key_department.setter
    def country_key_department(self, value):
        self._country_key_department = value
    @property
    def hospital_addr(self):
        return self._hospital_addr

    @hospital_addr.setter
    def hospital_addr(self, value):
        self._hospital_addr = value
    @property
    def hospital_alias(self):
        return self._hospital_alias

    @hospital_alias.setter
    def hospital_alias(self, value):
        self._hospital_alias = value
    @property
    def hospital_city(self):
        return self._hospital_city

    @hospital_city.setter
    def hospital_city(self, value):
        self._hospital_city = value
    @property
    def hospital_district(self):
        return self._hospital_district

    @hospital_district.setter
    def hospital_district(self, value):
        self._hospital_district = value
    @property
    def hospital_grade(self):
        return self._hospital_grade

    @hospital_grade.setter
    def hospital_grade(self, value):
        self._hospital_grade = value
    @property
    def hospital_id(self):
        return self._hospital_id

    @hospital_id.setter
    def hospital_id(self, value):
        self._hospital_id = value
    @property
    def hospital_lat(self):
        return self._hospital_lat

    @hospital_lat.setter
    def hospital_lat(self, value):
        self._hospital_lat = value
    @property
    def hospital_lgt(self):
        return self._hospital_lgt

    @hospital_lgt.setter
    def hospital_lgt(self, value):
        self._hospital_lgt = value
    @property
    def hospital_logo(self):
        return self._hospital_logo

    @hospital_logo.setter
    def hospital_logo(self, value):
        self._hospital_logo = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def hospital_optag(self):
        return self._hospital_optag

    @hospital_optag.setter
    def hospital_optag(self, value):
        self._hospital_optag = value
    @property
    def hospital_province(self):
        return self._hospital_province

    @hospital_province.setter
    def hospital_province(self, value):
        self._hospital_province = value
    @property
    def hospital_standard_code(self):
        return self._hospital_standard_code

    @hospital_standard_code.setter
    def hospital_standard_code(self, value):
        self._hospital_standard_code = value
    @property
    def hospital_tel(self):
        return self._hospital_tel

    @hospital_tel.setter
    def hospital_tel(self, value):
        self._hospital_tel = value
    @property
    def hospital_type(self):
        return self._hospital_type

    @hospital_type.setter
    def hospital_type(self, value):
        self._hospital_type = value
    @property
    def hospital_work_time(self):
        return self._hospital_work_time

    @hospital_work_time.setter
    def hospital_work_time(self, value):
        self._hospital_work_time = value
    @property
    def key_department(self):
        return self._key_department

    @key_department.setter
    def key_department(self, value):
        self._key_department = value
    @property
    def province_key_department(self):
        return self._province_key_department

    @province_key_department.setter
    def province_key_department(self, value):
        self._province_key_department = value


    def to_alipay_dict(self):
        params = dict()
        if self.country_key_department:
            if hasattr(self.country_key_department, 'to_alipay_dict'):
                params['country_key_department'] = self.country_key_department.to_alipay_dict()
            else:
                params['country_key_department'] = self.country_key_department
        if self.hospital_addr:
            if hasattr(self.hospital_addr, 'to_alipay_dict'):
                params['hospital_addr'] = self.hospital_addr.to_alipay_dict()
            else:
                params['hospital_addr'] = self.hospital_addr
        if self.hospital_alias:
            if hasattr(self.hospital_alias, 'to_alipay_dict'):
                params['hospital_alias'] = self.hospital_alias.to_alipay_dict()
            else:
                params['hospital_alias'] = self.hospital_alias
        if self.hospital_city:
            if hasattr(self.hospital_city, 'to_alipay_dict'):
                params['hospital_city'] = self.hospital_city.to_alipay_dict()
            else:
                params['hospital_city'] = self.hospital_city
        if self.hospital_district:
            if hasattr(self.hospital_district, 'to_alipay_dict'):
                params['hospital_district'] = self.hospital_district.to_alipay_dict()
            else:
                params['hospital_district'] = self.hospital_district
        if self.hospital_grade:
            if hasattr(self.hospital_grade, 'to_alipay_dict'):
                params['hospital_grade'] = self.hospital_grade.to_alipay_dict()
            else:
                params['hospital_grade'] = self.hospital_grade
        if self.hospital_id:
            if hasattr(self.hospital_id, 'to_alipay_dict'):
                params['hospital_id'] = self.hospital_id.to_alipay_dict()
            else:
                params['hospital_id'] = self.hospital_id
        if self.hospital_lat:
            if hasattr(self.hospital_lat, 'to_alipay_dict'):
                params['hospital_lat'] = self.hospital_lat.to_alipay_dict()
            else:
                params['hospital_lat'] = self.hospital_lat
        if self.hospital_lgt:
            if hasattr(self.hospital_lgt, 'to_alipay_dict'):
                params['hospital_lgt'] = self.hospital_lgt.to_alipay_dict()
            else:
                params['hospital_lgt'] = self.hospital_lgt
        if self.hospital_logo:
            if hasattr(self.hospital_logo, 'to_alipay_dict'):
                params['hospital_logo'] = self.hospital_logo.to_alipay_dict()
            else:
                params['hospital_logo'] = self.hospital_logo
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.hospital_optag:
            if hasattr(self.hospital_optag, 'to_alipay_dict'):
                params['hospital_optag'] = self.hospital_optag.to_alipay_dict()
            else:
                params['hospital_optag'] = self.hospital_optag
        if self.hospital_province:
            if hasattr(self.hospital_province, 'to_alipay_dict'):
                params['hospital_province'] = self.hospital_province.to_alipay_dict()
            else:
                params['hospital_province'] = self.hospital_province
        if self.hospital_standard_code:
            if hasattr(self.hospital_standard_code, 'to_alipay_dict'):
                params['hospital_standard_code'] = self.hospital_standard_code.to_alipay_dict()
            else:
                params['hospital_standard_code'] = self.hospital_standard_code
        if self.hospital_tel:
            if hasattr(self.hospital_tel, 'to_alipay_dict'):
                params['hospital_tel'] = self.hospital_tel.to_alipay_dict()
            else:
                params['hospital_tel'] = self.hospital_tel
        if self.hospital_type:
            if hasattr(self.hospital_type, 'to_alipay_dict'):
                params['hospital_type'] = self.hospital_type.to_alipay_dict()
            else:
                params['hospital_type'] = self.hospital_type
        if self.hospital_work_time:
            if hasattr(self.hospital_work_time, 'to_alipay_dict'):
                params['hospital_work_time'] = self.hospital_work_time.to_alipay_dict()
            else:
                params['hospital_work_time'] = self.hospital_work_time
        if self.key_department:
            if hasattr(self.key_department, 'to_alipay_dict'):
                params['key_department'] = self.key_department.to_alipay_dict()
            else:
                params['key_department'] = self.key_department
        if self.province_key_department:
            if hasattr(self.province_key_department, 'to_alipay_dict'):
                params['province_key_department'] = self.province_key_department.to_alipay_dict()
            else:
                params['province_key_department'] = self.province_key_department
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HospitalData()
        if 'country_key_department' in d:
            o.country_key_department = d['country_key_department']
        if 'hospital_addr' in d:
            o.hospital_addr = d['hospital_addr']
        if 'hospital_alias' in d:
            o.hospital_alias = d['hospital_alias']
        if 'hospital_city' in d:
            o.hospital_city = d['hospital_city']
        if 'hospital_district' in d:
            o.hospital_district = d['hospital_district']
        if 'hospital_grade' in d:
            o.hospital_grade = d['hospital_grade']
        if 'hospital_id' in d:
            o.hospital_id = d['hospital_id']
        if 'hospital_lat' in d:
            o.hospital_lat = d['hospital_lat']
        if 'hospital_lgt' in d:
            o.hospital_lgt = d['hospital_lgt']
        if 'hospital_logo' in d:
            o.hospital_logo = d['hospital_logo']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'hospital_optag' in d:
            o.hospital_optag = d['hospital_optag']
        if 'hospital_province' in d:
            o.hospital_province = d['hospital_province']
        if 'hospital_standard_code' in d:
            o.hospital_standard_code = d['hospital_standard_code']
        if 'hospital_tel' in d:
            o.hospital_tel = d['hospital_tel']
        if 'hospital_type' in d:
            o.hospital_type = d['hospital_type']
        if 'hospital_work_time' in d:
            o.hospital_work_time = d['hospital_work_time']
        if 'key_department' in d:
            o.key_department = d['key_department']
        if 'province_key_department' in d:
            o.province_key_department = d['province_key_department']
        return o


