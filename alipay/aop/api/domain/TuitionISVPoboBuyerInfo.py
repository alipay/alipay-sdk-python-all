#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TuitionISVPoboBuyerInfo(object):

    def __init__(self):
        self._academic_year = None
        self._date_of_birth = None
        self._email = None
        self._first_name = None
        self._full_name = None
        self._last_name = None
        self._phone_area_code = None
        self._phone_number = None
        self._student_id = None

    @property
    def academic_year(self):
        return self._academic_year

    @academic_year.setter
    def academic_year(self, value):
        self._academic_year = value
    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        self._date_of_birth = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value
    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        self._full_name = value
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value
    @property
    def phone_area_code(self):
        return self._phone_area_code

    @phone_area_code.setter
    def phone_area_code(self, value):
        self._phone_area_code = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        self._student_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.academic_year:
            if hasattr(self.academic_year, 'to_alipay_dict'):
                params['academic_year'] = self.academic_year.to_alipay_dict()
            else:
                params['academic_year'] = self.academic_year
        if self.date_of_birth:
            if hasattr(self.date_of_birth, 'to_alipay_dict'):
                params['date_of_birth'] = self.date_of_birth.to_alipay_dict()
            else:
                params['date_of_birth'] = self.date_of_birth
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
        if self.first_name:
            if hasattr(self.first_name, 'to_alipay_dict'):
                params['first_name'] = self.first_name.to_alipay_dict()
            else:
                params['first_name'] = self.first_name
        if self.full_name:
            if hasattr(self.full_name, 'to_alipay_dict'):
                params['full_name'] = self.full_name.to_alipay_dict()
            else:
                params['full_name'] = self.full_name
        if self.last_name:
            if hasattr(self.last_name, 'to_alipay_dict'):
                params['last_name'] = self.last_name.to_alipay_dict()
            else:
                params['last_name'] = self.last_name
        if self.phone_area_code:
            if hasattr(self.phone_area_code, 'to_alipay_dict'):
                params['phone_area_code'] = self.phone_area_code.to_alipay_dict()
            else:
                params['phone_area_code'] = self.phone_area_code
        if self.phone_number:
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        if self.student_id:
            if hasattr(self.student_id, 'to_alipay_dict'):
                params['student_id'] = self.student_id.to_alipay_dict()
            else:
                params['student_id'] = self.student_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TuitionISVPoboBuyerInfo()
        if 'academic_year' in d:
            o.academic_year = d['academic_year']
        if 'date_of_birth' in d:
            o.date_of_birth = d['date_of_birth']
        if 'email' in d:
            o.email = d['email']
        if 'first_name' in d:
            o.first_name = d['first_name']
        if 'full_name' in d:
            o.full_name = d['full_name']
        if 'last_name' in d:
            o.last_name = d['last_name']
        if 'phone_area_code' in d:
            o.phone_area_code = d['phone_area_code']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        if 'student_id' in d:
            o.student_id = d['student_id']
        return o


