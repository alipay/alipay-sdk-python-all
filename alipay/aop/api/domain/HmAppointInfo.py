#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HmAppointInfo(object):

    def __init__(self):
        self._appoint_age = None
        self._appoint_birthday = None
        self._appoint_certificate_no = None
        self._appoint_certificate_type = None
        self._appoint_city = None
        self._appoint_description = None
        self._appoint_gender = None
        self._appoint_hospital = None
        self._appoint_hospital_department = None
        self._appoint_name = None
        self._appoint_number = None
        self._appoint_service_type = None
        self._appoint_time = None

    @property
    def appoint_age(self):
        return self._appoint_age

    @appoint_age.setter
    def appoint_age(self, value):
        self._appoint_age = value
    @property
    def appoint_birthday(self):
        return self._appoint_birthday

    @appoint_birthday.setter
    def appoint_birthday(self, value):
        self._appoint_birthday = value
    @property
    def appoint_certificate_no(self):
        return self._appoint_certificate_no

    @appoint_certificate_no.setter
    def appoint_certificate_no(self, value):
        self._appoint_certificate_no = value
    @property
    def appoint_certificate_type(self):
        return self._appoint_certificate_type

    @appoint_certificate_type.setter
    def appoint_certificate_type(self, value):
        self._appoint_certificate_type = value
    @property
    def appoint_city(self):
        return self._appoint_city

    @appoint_city.setter
    def appoint_city(self, value):
        self._appoint_city = value
    @property
    def appoint_description(self):
        return self._appoint_description

    @appoint_description.setter
    def appoint_description(self, value):
        self._appoint_description = value
    @property
    def appoint_gender(self):
        return self._appoint_gender

    @appoint_gender.setter
    def appoint_gender(self, value):
        self._appoint_gender = value
    @property
    def appoint_hospital(self):
        return self._appoint_hospital

    @appoint_hospital.setter
    def appoint_hospital(self, value):
        self._appoint_hospital = value
    @property
    def appoint_hospital_department(self):
        return self._appoint_hospital_department

    @appoint_hospital_department.setter
    def appoint_hospital_department(self, value):
        self._appoint_hospital_department = value
    @property
    def appoint_name(self):
        return self._appoint_name

    @appoint_name.setter
    def appoint_name(self, value):
        self._appoint_name = value
    @property
    def appoint_number(self):
        return self._appoint_number

    @appoint_number.setter
    def appoint_number(self, value):
        self._appoint_number = value
    @property
    def appoint_service_type(self):
        return self._appoint_service_type

    @appoint_service_type.setter
    def appoint_service_type(self, value):
        self._appoint_service_type = value
    @property
    def appoint_time(self):
        return self._appoint_time

    @appoint_time.setter
    def appoint_time(self, value):
        self._appoint_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.appoint_age:
            if hasattr(self.appoint_age, 'to_alipay_dict'):
                params['appoint_age'] = self.appoint_age.to_alipay_dict()
            else:
                params['appoint_age'] = self.appoint_age
        if self.appoint_birthday:
            if hasattr(self.appoint_birthday, 'to_alipay_dict'):
                params['appoint_birthday'] = self.appoint_birthday.to_alipay_dict()
            else:
                params['appoint_birthday'] = self.appoint_birthday
        if self.appoint_certificate_no:
            if hasattr(self.appoint_certificate_no, 'to_alipay_dict'):
                params['appoint_certificate_no'] = self.appoint_certificate_no.to_alipay_dict()
            else:
                params['appoint_certificate_no'] = self.appoint_certificate_no
        if self.appoint_certificate_type:
            if hasattr(self.appoint_certificate_type, 'to_alipay_dict'):
                params['appoint_certificate_type'] = self.appoint_certificate_type.to_alipay_dict()
            else:
                params['appoint_certificate_type'] = self.appoint_certificate_type
        if self.appoint_city:
            if hasattr(self.appoint_city, 'to_alipay_dict'):
                params['appoint_city'] = self.appoint_city.to_alipay_dict()
            else:
                params['appoint_city'] = self.appoint_city
        if self.appoint_description:
            if hasattr(self.appoint_description, 'to_alipay_dict'):
                params['appoint_description'] = self.appoint_description.to_alipay_dict()
            else:
                params['appoint_description'] = self.appoint_description
        if self.appoint_gender:
            if hasattr(self.appoint_gender, 'to_alipay_dict'):
                params['appoint_gender'] = self.appoint_gender.to_alipay_dict()
            else:
                params['appoint_gender'] = self.appoint_gender
        if self.appoint_hospital:
            if hasattr(self.appoint_hospital, 'to_alipay_dict'):
                params['appoint_hospital'] = self.appoint_hospital.to_alipay_dict()
            else:
                params['appoint_hospital'] = self.appoint_hospital
        if self.appoint_hospital_department:
            if hasattr(self.appoint_hospital_department, 'to_alipay_dict'):
                params['appoint_hospital_department'] = self.appoint_hospital_department.to_alipay_dict()
            else:
                params['appoint_hospital_department'] = self.appoint_hospital_department
        if self.appoint_name:
            if hasattr(self.appoint_name, 'to_alipay_dict'):
                params['appoint_name'] = self.appoint_name.to_alipay_dict()
            else:
                params['appoint_name'] = self.appoint_name
        if self.appoint_number:
            if hasattr(self.appoint_number, 'to_alipay_dict'):
                params['appoint_number'] = self.appoint_number.to_alipay_dict()
            else:
                params['appoint_number'] = self.appoint_number
        if self.appoint_service_type:
            if hasattr(self.appoint_service_type, 'to_alipay_dict'):
                params['appoint_service_type'] = self.appoint_service_type.to_alipay_dict()
            else:
                params['appoint_service_type'] = self.appoint_service_type
        if self.appoint_time:
            if hasattr(self.appoint_time, 'to_alipay_dict'):
                params['appoint_time'] = self.appoint_time.to_alipay_dict()
            else:
                params['appoint_time'] = self.appoint_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HmAppointInfo()
        if 'appoint_age' in d:
            o.appoint_age = d['appoint_age']
        if 'appoint_birthday' in d:
            o.appoint_birthday = d['appoint_birthday']
        if 'appoint_certificate_no' in d:
            o.appoint_certificate_no = d['appoint_certificate_no']
        if 'appoint_certificate_type' in d:
            o.appoint_certificate_type = d['appoint_certificate_type']
        if 'appoint_city' in d:
            o.appoint_city = d['appoint_city']
        if 'appoint_description' in d:
            o.appoint_description = d['appoint_description']
        if 'appoint_gender' in d:
            o.appoint_gender = d['appoint_gender']
        if 'appoint_hospital' in d:
            o.appoint_hospital = d['appoint_hospital']
        if 'appoint_hospital_department' in d:
            o.appoint_hospital_department = d['appoint_hospital_department']
        if 'appoint_name' in d:
            o.appoint_name = d['appoint_name']
        if 'appoint_number' in d:
            o.appoint_number = d['appoint_number']
        if 'appoint_service_type' in d:
            o.appoint_service_type = d['appoint_service_type']
        if 'appoint_time' in d:
            o.appoint_time = d['appoint_time']
        return o


