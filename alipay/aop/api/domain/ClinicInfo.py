#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ClinicInfo(object):

    def __init__(self):
        self._appointment_time = None
        self._city_code = None
        self._city_name = None
        self._clinic_category = None
        self._department = None
        self._district_code = None
        self._district_name = None
        self._hospital_address = None
        self._hospital_name = None
        self._medical_record_url_list = None
        self._province_code = None
        self._province_name = None

    @property
    def appointment_time(self):
        return self._appointment_time

    @appointment_time.setter
    def appointment_time(self, value):
        self._appointment_time = value
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
    def clinic_category(self):
        return self._clinic_category

    @clinic_category.setter
    def clinic_category(self, value):
        self._clinic_category = value
    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        self._department = value
    @property
    def district_code(self):
        return self._district_code

    @district_code.setter
    def district_code(self, value):
        self._district_code = value
    @property
    def district_name(self):
        return self._district_name

    @district_name.setter
    def district_name(self, value):
        self._district_name = value
    @property
    def hospital_address(self):
        return self._hospital_address

    @hospital_address.setter
    def hospital_address(self, value):
        self._hospital_address = value
    @property
    def hospital_name(self):
        return self._hospital_name

    @hospital_name.setter
    def hospital_name(self, value):
        self._hospital_name = value
    @property
    def medical_record_url_list(self):
        return self._medical_record_url_list

    @medical_record_url_list.setter
    def medical_record_url_list(self, value):
        if isinstance(value, list):
            self._medical_record_url_list = list()
            for i in value:
                self._medical_record_url_list.append(i)
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.appointment_time:
            if hasattr(self.appointment_time, 'to_alipay_dict'):
                params['appointment_time'] = self.appointment_time.to_alipay_dict()
            else:
                params['appointment_time'] = self.appointment_time
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
        if self.clinic_category:
            if hasattr(self.clinic_category, 'to_alipay_dict'):
                params['clinic_category'] = self.clinic_category.to_alipay_dict()
            else:
                params['clinic_category'] = self.clinic_category
        if self.department:
            if hasattr(self.department, 'to_alipay_dict'):
                params['department'] = self.department.to_alipay_dict()
            else:
                params['department'] = self.department
        if self.district_code:
            if hasattr(self.district_code, 'to_alipay_dict'):
                params['district_code'] = self.district_code.to_alipay_dict()
            else:
                params['district_code'] = self.district_code
        if self.district_name:
            if hasattr(self.district_name, 'to_alipay_dict'):
                params['district_name'] = self.district_name.to_alipay_dict()
            else:
                params['district_name'] = self.district_name
        if self.hospital_address:
            if hasattr(self.hospital_address, 'to_alipay_dict'):
                params['hospital_address'] = self.hospital_address.to_alipay_dict()
            else:
                params['hospital_address'] = self.hospital_address
        if self.hospital_name:
            if hasattr(self.hospital_name, 'to_alipay_dict'):
                params['hospital_name'] = self.hospital_name.to_alipay_dict()
            else:
                params['hospital_name'] = self.hospital_name
        if self.medical_record_url_list:
            if isinstance(self.medical_record_url_list, list):
                for i in range(0, len(self.medical_record_url_list)):
                    element = self.medical_record_url_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.medical_record_url_list[i] = element.to_alipay_dict()
            if hasattr(self.medical_record_url_list, 'to_alipay_dict'):
                params['medical_record_url_list'] = self.medical_record_url_list.to_alipay_dict()
            else:
                params['medical_record_url_list'] = self.medical_record_url_list
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.province_name:
            if hasattr(self.province_name, 'to_alipay_dict'):
                params['province_name'] = self.province_name.to_alipay_dict()
            else:
                params['province_name'] = self.province_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ClinicInfo()
        if 'appointment_time' in d:
            o.appointment_time = d['appointment_time']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'clinic_category' in d:
            o.clinic_category = d['clinic_category']
        if 'department' in d:
            o.department = d['department']
        if 'district_code' in d:
            o.district_code = d['district_code']
        if 'district_name' in d:
            o.district_name = d['district_name']
        if 'hospital_address' in d:
            o.hospital_address = d['hospital_address']
        if 'hospital_name' in d:
            o.hospital_name = d['hospital_name']
        if 'medical_record_url_list' in d:
            o.medical_record_url_list = d['medical_record_url_list']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'province_name' in d:
            o.province_name = d['province_name']
        return o


